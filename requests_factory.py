import requests

class RequestsFactory:


    def __init__(self):
        pass

    def produce(self, url, credentials=None) -> requests.Response:
        if credentials is not None: 
            resp = requests.request(credentials[0], url, data=credentials[1], headers=credentials[2])
            return resp
        
        resp = requests.get(url)
        return resp
    


        
