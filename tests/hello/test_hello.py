import inspirationq.hello
from ..context import BaseAPITest


class TestHello(BaseAPITest):
    def test_hello_world(self):
        inspirationq.hello.hello(self.credentials)
