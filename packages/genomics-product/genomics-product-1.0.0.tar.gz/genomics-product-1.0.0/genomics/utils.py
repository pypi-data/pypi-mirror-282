import argparse
import joblib
import time
import uuid

import requests


def restricted_float(value):
    """Validates a float between 0 and 1 (inclusive)."""
    try:
        fvalue = float(value)
        if 0 <= fvalue <= 1:
            return fvalue
        raise argparse.ArgumentTypeError(f"{value} not in range [0, 1]")
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} not a valid floating-point value")


def restricted_int(value):
    """Validates an int between 0 and 5000 (inclusive)."""
    try:
        fvalue = int(value)
        if 0 <= fvalue <= 5000:
            return fvalue
        raise argparse.ArgumentTypeError(f"{value} not in range [0, 5000]")
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} not a valid integer value")


def generate_unique_job_name(prefix="job_") -> str:
    """Generates a unique job name, combining a prefix, UUID, and timestamp.

    Args:
        prefix (str, optional): A custom prefix for the job name. Defaults to "job_".

    Returns:
        str: The generated unique job name.
    """

    unique_id = str(uuid.uuid4())
    timestamp = str(int(time.time()))
    job_name = f"{prefix}{unique_id}_{timestamp}"

    return job_name


def download_from_presigned_url(url, output_path: str):
    """Downloads content from a presigned URL and returns it as a string

    Args:
        url (str): The presigned URL to download from.
        output_path (str, optional): path of result file.

    Returns:
        str: The content of the file as a string.

    Raises:
        RuntimeError: If the download fails.
    """

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(output_path, 'wb') as file:
            file.write(response.content)

        with open(output_path, 'rb') as pickle_file:
            loaded_data = joblib.load(pickle_file)

        return loaded_data

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Download failed: {e}")
