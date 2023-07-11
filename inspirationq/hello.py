from .api.credentials import default_credentials


def hello(credentials=default_credentials):
    r = credentials.post("hello")
    return r["message"]


def hello_wait(credentials=default_credentials):
    r = credentials.post("hello_wait")
    return r["message"]
