import inspirationq.api.bare
import unittest

common_credentials = inspirationq.api.bare.bare_credentials("http://127.0.0.1:3000/")

import sys
import os.path

for core_location in ["../../api/core/tests", "../api/core/tests"]:
    if os.path.exists(core_location):
        sys.path += os.path.realpath(core_location)


class BaseAPITest(unittest.TestCase):

    credentials = common_credentials
