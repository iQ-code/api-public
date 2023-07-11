import requests
import platform
import os
import toml

known_entry_points = {
    "hello",
    "hello_wait",
    "qubo_bf",
    "qubo_cont",
    "qubo_mc",
    "qubo_sa",
    "qbo_ca",
    "tsp_mc",
    "qudo_mc",
    "get",
}


class BaseAPI:
    def __init__(self, group="default", base_url=None, load_config=True):
        self.url_dict = {}
        self.debug = False
        if load_config:
            self.configuration = self.load_configuration()
        else:
            self.configuration = {}
        self.group = group
        self.base_url = self.configuration_value(
            "base_url", base_url, required=True
        ).rstrip(r"\/ ")

    def configuration_filename(self):
        if platform.system() == "Windows":
            path = os.getenv("USERPROFILE")
        else:
            path = os.getenv("HOME")
        return (path if os.path.exists(path) else ".") + "/.iq_config.toml"

    def load_configuration(self):
        configuration = {}
        filename = self.configuration_filename()
        if os.path.exists(filename):
            with open(filename) as fp:
                configuration = toml.load(fp)
        return configuration

    def configuration_value(self, field, default=None, group=None, required=False):
        configuration = self.configuration
        if group is None:
            group = self.group
        if group in configuration:
            group_dict = configuration[group]
            if field in group_dict:
                return group_dict[field]
        if required and default is None:
            raise Exception(
                f"Field '{field}' from group '{group}' absent in configuration file and not provided."
            )
        return default

    def authorization(self):
        raise Exception(
            f"Unauthorized access to Inspiration-Q API. Please obtain credentials first"
        )

    def specialize(self, base_url, entry_points):
        return {k: base_url + "/" + k for k in entry_points}

    def get(self, function, **arguments):
        headers = self.authorization()
        if function not in self.url_dict:
            raise Exception(f"Unknown API function {function}")
        url = self.url_dict[function]
        if self.debug:
            print(
                f"Sending GET request to {url} with header:\n{headers}\n"
                f"and arguments:\n{arguments}"
            )
        r = requests.get(url=url, headers=headers, **arguments)
        if self.debug:
            print(f"Received request Response {r} with content:\n{r.content}")
        if not r.ok:
            raise Exception(f"Error returned from Inspiration-Q API: {r}")
        return r.json()

    def post(self, function, waittime=1, **arguments):
        headers = self.authorization()
        if function not in self.url_dict:
            raise Exception(f"Unknown API function {function}")
        url = self.url_dict[function]
        if self.debug:
            print(
                f"Sending POST request to {url} with header:\n{headers}\n"
                f"and arguments:\n{arguments}"
            )
        r = requests.post(url=url, headers=headers, **arguments)
        if self.debug:
            print(f"Received request Response {r} with content:\n{r.content}")
        if not r.ok:
            raise Exception(f"Error returned from Inspiration-Q API: {r}")
        return r.json()


default_credentials = BaseAPI(base_url="https://127.0.0.1")
