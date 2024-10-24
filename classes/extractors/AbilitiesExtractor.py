import logging
from classes.extractors.AbstractExtractor import AbstractExtractor
from utils.Transformer import *


class AbilitiesExtractor(AbstractExtractor):
    __path_to_items = "https://fr.nwdb.info/db/abilities/page/"
    __page = 1

    def __init__(self):
        super().__init__()

    def start_extraction(self):
        logging.info("Extract abilities has started")
        super().create_connection()
        super().extract(self.__path_to_items, self.__page, read_data, create_ability_and_push_it_to_database)

