
from requests import Response

class ScanningError: 
    """  Error instance stores the information abount occured
    error 
    --------------------------------
      HTTP status_code
      request(instance of requests.Response)
      """
    
    def __init__(self, status, response: Response):  
        self.status = status
        self.response = response

    def stringify(self) -> str:
        return f"{self.status} {self.response.url}"
    
