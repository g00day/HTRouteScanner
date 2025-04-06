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