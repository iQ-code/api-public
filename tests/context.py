import inspirationq.api.bare
import inspirationq.api.aws
import unittest
import os


def make_default_credentials(url=None):
    if url is None:
        url = os.getenv("IQ_URL")
    if url is None or url == "local":
        return inspirationq.api.bare.bare_credentials("http://127.0.0.1:3000/")
    if url == "aws":
        url = None
    username = os.getenv("IQ_USERNAME")
    password = os.getenv("IQ_PASSWORD")
    if username is None:
        raise Exception(
            "Remote testing requested but environment variable IQ_USERNAME not set"
        )
    if password is None:
        raise Exception(
            "Remote testing requested but environment variable IQ_PASSWORD not set"
        )
    return inspirationq.api.aws.iQAWSAPI(username, password, url)


common_credentials = make_default_credentials()


class BaseAPITest(unittest.TestCase):

    credentials = common_credentials
