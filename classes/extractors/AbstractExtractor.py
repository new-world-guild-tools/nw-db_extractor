import cloudscraper
import logging
import json

class AbstractExtractor:
    def __init__(self):
        self.__scraper = None

    def create_connection(self):
        self.__scraper = cloudscraper.create_scraper(
            browser={
                "browser": "chrome",
                "platform": "windows",
            },
        )

    def send_get_request(self, path):
        return self.__scraper.get(path)

    def extract(self, path, page, success, success_loader_function):
        extraction_response = self.send_get_request(path + str(page) + ".json")
        page_count = json.loads(extraction_response.text)["pageCount"]
        while page <= page_count:
            if extraction_response.status_code == 200:
                success(extraction_response.text, success_loader_function)
                page += 1
                extraction_response = self.send_get_request(path + str(page) + ".json")
            else:
                logging.error("An error occurred at page " + str(page))
                logging.error("Status code returned by nwdb : " + extraction_response.status_code)

        if extraction_response.status_code != 200:
            logging.error("An error occurred at page " + str(page))
            logging.error("Status code returned by nwdb : " + extraction_response.status_code)