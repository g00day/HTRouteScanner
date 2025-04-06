# HTRouteScanner

#### HTRouteScanner is a small python tool that provides opportunity to parse all routes in hyper text interfaces for the purpose of checking it for errors


### HTRouteScanner uses:
- Python programming language
- [requests](https://github.com/psf/requests)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

### How does it work  
##### **Scanner takes some parameters:**
1.`entry point`. The  page from where the scanning will be started  
2.`black list`. A list of pages that will be ignored while scanning  
3.`routes_credentials`. A dictionary of pages that are need to be requested with some specific credentials(_HTTP methods, data, headers, etc_).


Scanner will parse all routes under each `a` element recursively storing all routes that have already scanned using `memo` list and ignoring foreign resources, routes that were passed in `black list` and requesting some routes differently if they were passed in `routes_credentials`.

if it faces *not OK HTTP status code* or *redirecting to another routes* it saves it into `error_list`.

After scanning scanner will return a two lists: list of scanned routes(`memo`) and `error_list`(the list of ScanningError)

If there is a route that's in the `routes_credentials` dict then it will firstly be executed as it descripted in routes_credentials. And if the 4-th element in routes_credentials[URL] is None or false then it will be also executed typically using `GET HTTP` method.


### Examples

```python
from scanner import HTRouteScanner
"""  
    What if we just want to check all routes given as links
    using GET http method only. Let's see:
"""

host = "http://localhost:8000/"

entry_point = f"{host}page1/" # initialize an entry point variable from where the scanning will be started
black_list = [f"{host}page3/"] # initialize a black list. Here you may pass pages that will be avoided of scanning

scanner = HTRouteScanner(entry_point, black_list=black_list) # pass all variables while initializing the object of HTRouteScanner
scanned, error_list = scanner.start() # starting the scanning

print(scanner, error_list)
```

**the example with passing routes_credential:**

```python
from scanner import HTRouteScanner
"""  
    Let's see what if you want to request routes with some credentials

"""

host = "http://localhost:8000/"

entry_point = f"{host}page1/" # initialize an entry point variable from where the scanning will be started

"""
to pass route credential you need to make a dict that contains:
"route": [<http method>, <data>, <header's dict>, <to avoid GET method?>]
for instance -> {
    "/page1/" : ['POST', {"name": "Arseniy", "pk": 1}, {"Authorization": "Token <some token>"}, True]
}
"""

routes_credentials = {
    f"{host}page5/": ["POST", {"name": "Arseniy", "pk": 1}, None, True]
}

scanner = HTRouteScanner(entry_point, routes_credentials=routes_credentials) # pass all variables while initializing the object of HTRouteScanner
scanned, error_list = scanner.start() # starting the scanning

print(scanned, error_list) 
```


to see more examples with explanations you may see `samples/` dir


### Installation

You may install HTRouteScanner using git cloning  
Soon it will be installable with `pip`

```bash
    git clone https://github.com/g00day/HTRouteScanner
```
    
### Support

For support, email dgood4133@gmail.com

