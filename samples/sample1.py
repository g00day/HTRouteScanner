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

print(scanned) # Here is the list of all pages scanned. 
#Pay attention that there is no "http://localhost:8000/page3/" 
#because it was passed in black_list parameter while HTRouteScanner's obj initialization


print(error_list) # Here is the list of errors occured while scanning
# It is provided as the objects of error.scanning_error.ScanningError's instances
# If you don't need a response(requests.Response) to see more details
# you may stringify it using stringify_error_list() method as it shown below:

scanner.stringify_error_list() # stringify error_list field
print(scanner.get_error_list()) # Now the error_list is fully stringified

# also you may get the pages that were scanned and list of errors occured while scanning
# using these methods
print(scanner.get_error_list())
print(scanner.get_scanned_pages())
