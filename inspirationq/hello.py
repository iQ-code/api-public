from .api.credentials import default_credentials

def hello(credentials=default_credentials):
    r = credentials.get('hello')
    return r['message']
