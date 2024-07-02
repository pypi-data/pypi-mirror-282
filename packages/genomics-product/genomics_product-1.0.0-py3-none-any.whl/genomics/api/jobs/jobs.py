from __future__ import annotations

import os.path
import time
import uuid
from typing import List
from typing import Optional

import requests
from tqdm import tqdm

# from genomics.api.hub.hub_response import HubResponse
from genomics.api.api_client import ApiClient
from genomics.api.models import (Status, JobDto, GetJobsRequest, GetjobsResult,
                                 InitiateJobCreationRequest, InitiateJobCreationResult,
                                 JobFileDto, GenericResultDto, GetJobResult, JobResultDto)
from genomics.configs.logger_config import get_logger
from genomics.utils import download_from_presigned_url

CHUNK_SIZE = 5 * 1024 * 1024


class Jobs:
    """Its main purpose is to allow users to add , delete and select inference jobs.

    This does not create a connection, it simply sends separate API requests.

    Examples:
        >>> jobs = Jobs()

        Fetching for jobs with filters
        >>> jobs.select_jobs(status=Status.Extracting)
        >>> jobs.select_jobs(status=Status.Extracting, keyword='job')
        >>> jobs.select_jobs(status=Status.Extracting, keyword='job', page_size=2)
        >>> jobs.select_jobs(page_size=10, page_number=1)
        >>> jobs.select_jobs(model_version_ids=[uuid.UUID("018d5f6c-4de9-191e-109f-e50a18bc8544")])
        >>> jobs.select_jobs(reference_genome_ids=[uuid.UUID("018d5f6c-4de9-191e-109f-e50a18bc8544")])
    """

    def __init__(self, api_client: ApiClient):
        self._api_client = api_client

    def select_jobs(
            self,
            model_version_ids: Optional[List[uuid.UUID]] = None,
            reference_genome_ids: Optional[List[uuid.UUID]] = None,
            page_number: Optional[int] = None,
            page_size: Optional[int] = None,
            status: Optional[Status] = None,
            keyword: Optional[str] = None
    ) -> List[JobDto]:
        """Fetches jobs from the LibraryGene library.

        Args:
            * model_version_ids: The optional list of model version IDs to filter jobs by.
            * reference_genome_ids: The optional list of reference genome IDs to filter
            jobs by.
            * page_number: The page number of the results to retrieve. Defaults to 1.
            * page_size: The number of results to retrieve per page. Defaults to 20.
            * status: The optional job status to filter by. Valid values might include
            Finished, Running, Uploading, Extracting, Canceled, Failed.
            * keyword: The optional keyword to search for within job names.

        Returns:
            A list of jobs.
        """
        payload = GetJobsRequest(
            model_version_ids=model_version_ids,
            reference_genome_ids=reference_genome_ids,
            page_number=page_number,
            page_size=page_size,
            status=status.name,
            keyword=keyword
        )
        response = self._api_client.get("/jobs", payload.dict())
        page = GetjobsResult.parse_obj(response.json())
        data: List[JobDto] = page.result.data
        return data

    def run_job(self, name: str, file_path: str, output_path: str, model_id: str, application: str,
                wait=False) -> str:
        initiate_job_creation_result = self.initiate_job_creation(
            file_path, model_id, name, application
        )
        self.upload_job_file_parts(file_path, initiate_job_creation_result.file_id)
        self.trigger_job_run(initiate_job_creation_result.job_id, name)
        if wait:
            while True:
                get_logger().info(f"fetching {name}....")
                job_details = self.get_job_details(initiate_job_creation_result.job_id)
                if job_details.error_file_url:
                    response = requests.get(job_details.error_file_url, stream=True)
                    response.raise_for_status()
                    error_message = response.text
                    get_logger().error(f"Job failed:\n{error_message}")
                    return error_message
                if job_details.result_file_url:
                    result = download_from_presigned_url(job_details.result_file_url, output_path)
                    return result
                get_logger().info(
                    f"{name} is still running retrying again in 30 seconds.")
                time.sleep(30)

    def initiate_job_creation(
            self, file_path, model_id, name, application
    ) -> JobFileDto:
        file_name = os.path.basename(file_path)
        get_logger().info(f"Initiating {name} with file : {file_name}")
        payload = InitiateJobCreationRequest(
            name=name,
            file_name=file_name,
            model_id=model_id,
            application=application
        )
        response = self._api_client.post(
            "/jobs", payload.dict()
        )
        result = InitiateJobCreationResult.parse_obj(
            response.json()
        )
        if result.error_code:
            raise Exception(result.error_message)
        return result.result

    def upload_job_file_parts(self, file_path, file_id):
        file_size = os.path.getsize(file_path)
        offset = 0
        with open(file_path, 'rb') as file:
            with tqdm(total=file_size, unit='B', unit_scale=True,
                      desc="Uploading File") as pbar:
                while True:
                    chunk = file.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    files = [('FilePart', chunk)]
                    data = {
                        'FileId': str(file_id),
                        'Offset': offset
                    }

                    response = self._api_client.patch(
                        "/jobs/file", files=files, data=data
                    )
                    result = GenericResultDto.parse_obj(
                        response.json()
                    )
                    if result.error_code:
                        raise Exception(result.error_message)
                    pbar.update(len(chunk))
                    offset += 1

    def trigger_job_run(self, job_id, job_name):
        response = self._api_client.patch(
            f"/jobs/{job_id}"
        )

        result = GenericResultDto.parse_obj(
            response.json()
        )
        if result.error_code:
            raise Exception(result.error_message)
        get_logger().info(f"{job_name} started running...")

    def get_job_details(self, job_id) -> JobResultDto:
        response = self._api_client.get(
            f"/jobs/{job_id}"
        )
        result = GetJobResult.parse_obj(response.json())
        if result.error_code:
            raise Exception(result.error_message)
        return result.result
