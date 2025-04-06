import requests

from functools import lru_cache
from typing import Dict, List


import utils

from requests_factory import RequestsFactory

from exceptions.black_list_exceptions import EntryPointInBlackListException


class HTRouteScanner:
    def __init__(self, entry_point: str,
                 black_list: list=[],
                 routes_credentials: Dict[str, List] = {}, 
                 ):
        """ __init__ method takes takes parameters:  
          entry_point - entry point of scanning  
          black_list - a list of routes that are needed to be avoided of scanning  
          routes_credentials - a dictionary of routes where the route given as the key
            and value is a list of all needed data to produce request like:  
            route: [<http method>, <data>, <header's dict>, <to avoid GET method?>]
            for instance -> {
              "/page1/" : ['POST', {"name": "Arseniy", "pk": 1}, {"Authorization": "Token <some token>"}, True]
            }
          """
        if entry_point in black_list:
            # check if there is no entry_point value in black list :)
            raise EntryPointInBlackListException(f"The entry point {entry_point} is in black_list", entry_point)

        self.entry_point = entry_point

        self.routes_credentials = routes_credentials

        self._black_list = black_list
        self._requests_factory = RequestsFactory()
        self._memo = []
        self._error_list = []


    def start(self) -> tuple[list, list]:
        """ Starting the scanning  
            ---------------------  
            takes: 
              1. to_stringify_errors(defaultly False, returns the original requests.Response obj)  
            returns the:  
              1. page scanned  
              2. list of errors occured  
              
        """
        entry_point = self.entry_point
        
        self._memo = []
        self._error_list = []

        self.__scanning(entry_point)


        return self._memo, self._error_list
    

    @lru_cache
    def __scanning(self, url: str):
        """ Scanning method 
          ------------------
          """
        requests_factory = self._requests_factory
        
        if self.is_url_to_avoid(url): return 

        self._memo.append(url) # appending url into the list of already scanned urls
        
        if url in self.routes_credentials:
            credentials = self.routes_credentials[url]

            resp = requests_factory.produce(url, credentials=credentials) # Passing credentials if they were given for the exact URL
            self._handle_response(resp)

            if credentials[3]: return #  avoiding GET method if it is needed


        resp = requests_factory.produce(url)
        self._handle_response(resp)

        routes =  utils.get_routes(self.entry_point, resp)
        for route in routes:
            # scanning all routes that were provided on current page
            self.__scanning(route)

    
    def _handle_response(self, resp: requests.Response):
        error = utils.check_response_and_return_error(resp)
        if error is not None:
            self._error_list.append(error)

        if resp.is_redirect:
            redirect_to = resp.headers['Location']
            self.__scanning(redirect_to)
        

    def is_url_to_avoid(self, url: str) -> bool:
        """ method that returns if given url needs to be avoided  
            while scanning  
            -----------------------------------------------------  
            urls to be avoided:  
            1.urls that were already scanned(are in self._memo)  
            2.included in black list  
        """
        return url in self._memo or url in self._black_list


    def stringify_error_list(self):
        self._error_list = [error.stringify() for error in self._error_list]


    def get_scanned_pages(self) -> list: 
        return self._memo
    
    def get_error_list(self) -> list:
        return self._error_list


