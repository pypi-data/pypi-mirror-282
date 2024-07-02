import os
import uuid

from dotenv import load_dotenv

from genomics.api.genomics_client import GenomicsClient
from genomics.utils import generate_unique_job_name

load_dotenv()
api_key = os.getenv('API_KEY')
backend_url = os.getenv('BACKEND_URL')
genomics_client = GenomicsClient(
    api_key=api_key,
    backend_url=backend_url
)


def main():
    jobs = genomics_client.jobs()

    result = jobs.run_job(
        generate_unique_job_name(),
        "path/to/file",
        uuid.UUID("018de127-b827-9a64-0e28-74e57614b53b")
    )

    # result = get_access_token()
    print(result)


if __name__ == '__main__':
    main()
