from .bare import iQBareAPI

class iQRapidAPI(iQBareAPI):
    
    def __init__(self, rapidapi_key):
        super(iQRapidAPI, self).__init__('https://inspiration-q.p.rapidapi.com')
        self.rapidapi_key = rapidapi_key

    def authorization(self):
        return {
            'x-rapidapi-host': 'inspiration-q.p.rapidapi.com',
            'x-rapidapi-key': self.rapidapi_key
        }

    
def rapidapi_credentials(rapidapi_key):
    return iQRapidAPI(rapidapi_key)
