import os
import sys

from dotenv import load_dotenv

from api.genomics_client import GenomicsClient

load_dotenv()
api_key = "THFod3BzM3NWeHpLQ2RmbGlyTUNEc0dlTnU4Nkw5Z2FAY2xpZW50cy4yMDI0MDYwNDE2MzM1Mi4vMHRjNFRwL1hQTnRMeFI1S2ZDNTd3PT0="  #os.getenv('API_KEY')
backend_url = "http://localhost:5287/api/v1/"  #os.getenv('BACKEND_URL')


# rt_url = "http://localhost:5287/rt" #os.getenv('RT_URL')


def main():
    genomics_client = GenomicsClient(
        api_key=api_key,
        # rt_url=rt_url,
        backend_url=backend_url)
    result = genomics_client.test_rt()
    print(result)


if __name__ == '__main__':
    main()
