from .credentials import BaseAPI, known_entry_points

class iQBareAPI(BaseAPI):
    
    def __init__(self, base_url):
        super(iQBareAPI, self).__init__()
        self.base_url = base_url
        self.url_dict = self.specialize(base_url, known_entry_points)

    def authorization(self):
        return { }

    
def bare_credentials(base_url):
    return iQBareAPI(base_url)
