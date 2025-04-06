

class EntryPointInBlackListException(Exception):
    """ This exception raises in case 
    if the entry_point field was passed in black_list
     while initializing the HTRouteScanner """
    
    def __init__(self, message, entry_point):
        super().__init__(message)
        self.entry_point = entry_point