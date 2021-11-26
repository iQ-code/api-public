import requests

known_entry_points = {
    'hello',
    'qubo_bf',
    'qubo_cont',
    'qubo_mc'
}

class BaseAPI:

    def __init__(self):
        self.url_dict = {}
        self.debug = False

    def authorization(self):
        raise Exception(f'Unauthorized access to Inspiration-Q API. Please obtain credentials first')

    def specialize(self, base_url, entry_points):
        return { k : base_url + '/' + k for k in entry_points }

    def get(self, function, **arguments):
        headers = self.authorization()
        if function not in self.url_dict:
            raise Exception(f'Unknown API function {function}')
        url = self.url_dict[function]
        if self.debug:
            print(f'Sending GET request to {url} with header:\n{headers}\n'
                  f'and arguments:\n{arguments}')
        r = requests.get(url=url, headers=headers, **arguments)
        if self.debug:
            print(f'Received request Response {r} with content:\n{r.content}')
        if not r.ok:
            raise Exception(f'Error returned from Inspiration-Q API: {r}')
        return r.json()

    def post(self, function, **arguments):
        headers = self.authorization()
        if function not in self.url_dict:
            raise Exception(f'Unknown API function {function}')
        url = self.url_dict[function]
        if self.debug:
            print(f'Sending POST request to {url} with header:\n{headers}\n'
                  f'and arguments:\n{arguments}')
        r = requests.post(url=url, headers=headers, **arguments)
        if self.debug:
            print(f'Received request Response {r} with content:\n{r.content}')
        if not r.ok:
            raise Exception(f'Error returned from Inspiration-Q API: {r}')
        return r.json()

default_credentials = BaseAPI()
