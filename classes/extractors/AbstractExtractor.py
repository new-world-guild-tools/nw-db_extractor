import http.client

class AbstractExtractor:

    def __init__(self):
        self.__connection = http.client.HTTPSConnection("fr.nwdb.info")