import requests

from bs4 import BeautifulSoup



class RequestsFactory:


    def __init__(self):
        pass

    
    def __get_csrf__(self, soup: BeautifulSoup):
        return soup.find('input', {'name': 'csrfmiddlewaretoken'})


    def produce(self, url, credentials=None) -> requests.Response:
        if credentials is not None: 
            # producing GET req to check if the CSRF TOKEN is passed on this route
            resp_GET = requests.get(url)
            soup = BeautifulSoup(resp_GET.text, 'html.parser')    # soupify the response
            csrf = self.__get_csrf__(soup)

            if csrf is not None:
                # passing CSRF token
                credentials[1]["csrfmiddlewaretoken"] = csrf['value']


            resp = requests.request(credentials[0], url, data=credentials[1], headers=credentials[2])
            return resp
        
        resp = requests.get(url)
        return resp
    


        

        
