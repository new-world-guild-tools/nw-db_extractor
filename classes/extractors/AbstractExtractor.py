from bs4 import BeautifulSoup
import cloudscraper

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