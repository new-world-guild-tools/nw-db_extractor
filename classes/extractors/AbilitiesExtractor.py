import logging
from classes.extractors.AbstractExtractor import AbstractExtractor
from utils.Transformer import *


class AbilitiesExtractor(AbstractExtractor):
    __path_to_items = "https://fr.nwdb.info/db/abilities/page/"
    __page = 1

    def __init__(self):
        super().__init__()

    def extract_items(self):
        logging.info("Extract abilities has started")
        super().create_connection()
        extraction_response = super().send_get_request(self.__path_to_items + str(self.__page) + ".json")
        page_count = json.loads(extraction_response.text)["pageCount"]
        while self.__page <= page_count:
            if extraction_response.status_code == 200:
                read_data(extraction_response.text, create_ability_and_push_it_to_database)
                self.__page += 1
                extraction_response = super().send_get_request(self.__path_to_items + str(self.__page) + ".json")
            else:
                logging.error("An error occurred at page " + str(self.__page))
                logging.error("Status code returned by nwdb : " + extraction_response.status_code)

        if extraction_response.status_code != 200:
            logging.error("An error occurred at page " + str(self.__page))
            logging.error("Status code returned by nwdb : " + extraction_response.status_code)

