from classes.extractors.AbstractExtractor import AbstractExtractor
from transformers.TransformItems import *


class ItemsExtractor(AbstractExtractor):
    __path_to_items = "https://fr.nwdb.info/db/items/page/"
    __page = 1

    def __init__(self):
        super().__init__()

    def extract_items(self):
        print("In extract items")
        super().create_connection()
        extraction_response = super().send_get_request(self.__path_to_items + str(self.__page) + ".json")
        page_count = json.loads(extraction_response.text)["pageCount"]
        while self.__page <= page_count:
            read_items_data(extraction_response.text)
            self.__page += 1
            extraction_response = super().send_get_request(self.__path_to_items + str(self.__page) + ".json")

        if extraction_response.status_code != 200:
            print("An error occurred at page " + str(self.__page))
            print("Status code : " + extraction_response.status_code)

