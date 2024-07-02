from __future__ import annotations

from enum import Enum
import uuid
from typing import Any
from typing import Generic
from typing import List
from typing import Optional
from typing import TypeVar

from pydantic import Extra
from pydantic import Field
from pydantic import BaseModel
from pydantic import root_validator
from pydantic.generics import GenericModel

from genomics.api.types import APIExceptionError

DataT = TypeVar("DataT")


class BaseGenomicsModel:
    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = Extra.forbid
        use_enum_values = True


class Status(Enum):
    Finished = "Finished"
    Running = "Running"
    Uploading = "Uploading"
    Extracting = "Extracting"
    Canceled = "Canceled"
    Failed = "Failed"


class JobDto(BaseModel):
    job_id: uuid.UUID
    user_id: str
    file_id: uuid.UUID
    file_name: str
    name: str
    status: str
    total_sequences_count: int
    treated_sequences_count: int
    reference_genome: str
    probability_threshold: float
    window_size_retrieval: int
    model_version: str


class GetJobsRequest(BaseModel):
    model_version_ids: Optional[List[uuid.UUID]] = None
    reference_genome_ids: Optional[List[uuid.UUID]] = None
    page_number: Optional[int] = None
    page_size: Optional[int] = None
    status: Optional[str] = None
    keyword: Optional[str] = None


class InitiateJobCreationRequest(BaseModel):
    name: str
    file_name: str
    model_id: str
    application: str


class PageInfo(BaseModel):
    number: int
    size: int


class GetModelsRequest(BaseModel):
    keyword: Optional[str] = None
    page_info: Optional[PageInfo] = None


class GenericResultDto(GenericModel, Generic[DataT], BaseGenomicsModel):
    status: str
    result: DataT
    error_code: Optional[str] = Field(None)  # noqa: CCE001
    error_message: Optional[str] = Field(None)  # noqa: CCE001

    @root_validator(pre=True)
    @classmethod
    def validate_status(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if "status" not in data:
                return data

            status = data["status"]

            if status is None:
                return data

            assert isinstance(status, str), "status must be a string"

            status = status.lower()
            if status != "success":
                error_code = data.get("error_code") or data.get("errorCode")
                error_message = data.get("error_message") or data.get("errorMessage")
                raise APIExceptionError(error_code=error_code, message=error_message)
        return data


class GenericFiltersSortsData(GenericModel, Generic[DataT], BaseGenomicsModel):
    data: List[DataT]
    page_number: int
    page_size: int
    total_size: int


class GenericListData(GenericModel, Generic[DataT], BaseGenomicsModel):
    data: List[DataT]


class JobsDtoPaginatedListDto(GenericFiltersSortsData[JobDto]):
    pass


class GetjobsResult(GenericResultDto[JobsDtoPaginatedListDto]):
    pass


class JobFileDto(GenericModel, BaseGenomicsModel):
    job_id: uuid.UUID
    file_id: uuid.UUID


class ModelsResultDto(GenericModel, BaseGenomicsModel):
    id: str
    name: str




class JobResultDto(GenericModel, BaseGenomicsModel):
    name: str
    status: str
    model: str
    fasta_file_url: str
    result_file_url: str
    error_file_url: str
    created_on: str


class InitiateJobCreationResult(GenericResultDto[JobFileDto]):
    pass


class GetJobResult(GenericResultDto[JobResultDto]):
    pass


class GetModelsResult(BaseModel):
    result: GenericListData[ModelsResultDto]
    status_code: Any
    status: str
    error_message: Any
    error_code: Any


