import argparse
import os
import uuid

from dotenv import load_dotenv

from genomics.api.genomics_client import GenomicsClient
from genomics.configs.logger_config import get_logger
from genomics.utils import generate_unique_job_name

try:
    from sys.stdin import buffer as std_in
    from sys.stdout import buffer as std_out
except ImportError:
    from sys import stdin as std_in
    from sys import stdout as std_out

load_dotenv()
api_key = os.getenv('API_KEY')
backend_url = os.getenv('BACKEND_URL')
# rt_url = os.getenv('BACKEND_URL')
genomics_client = GenomicsClient(
    api_key=api_key,
    backend_url=backend_url,
    # rt_url=rt_url
)


# result = genomics_client.test_rt()
# print(result)

def get_options():
    parser = argparse.ArgumentParser(description='Version: 1.0.0')
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    run_parser = subparsers.add_parser(name="run", help="run inference job")
    subparsers.add_parser(name="models", help="get list of models")

    add_run_job_arguments(run_parser)
    args = parser.parse_args()

    return args


def add_run_job_arguments(run_parser):
    run_parser.add_argument('-I', metavar='input', nargs='?',
                            default=std_in,
                            help='path to the input fasta file, defaults to standard in')
    run_parser.add_argument('-O', metavar='output', nargs='?', default=std_out,
                            help='path to the output file, defaults to standard out')
    run_parser.add_argument('-M', metavar='model', required=True,
                            type=uuid.UUID, help='id of the model version')
    run_parser.add_argument('-A', metavar='application', required=True,
                            type=str, help='the genomics task the NT is trained to perform')
    run_parser.add_argument('-N', metavar='job_name', nargs='?',
                            default=generate_unique_job_name(),
                            help='the user-provided name for the job, used for '
                                 'identification and tracking.')
    run_parser.add_argument('--wait', action='store_true',
                            help='Wait for the job run result if this flag is present.')


def main():
    args = get_options()

    if args.command == "run":
        jobs = genomics_client.jobs()
        try:
            result = jobs.run_job(args.N, args.I, args.O, args.M, args.A, args.wait)
            if result:
                get_logger().info(result)
        except Exception as e:
            get_logger().error(e)
    elif args.command == "models":
        models = genomics_client.models()
        try:
            models.list()
        except Exception as e:
            get_logger().error(e)


if __name__ == '__main__':
    main()
