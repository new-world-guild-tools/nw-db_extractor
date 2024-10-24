import os
import http.client

__instance = None


def get_instance():
    global __instance
    if __instance is None:
        __instance = Loader()
    return __instance


class Loader:
    def __init__(self):
        self.__connection = http.client.HTTPSConnection(os.getenv("API_URL"))
        self.__username = os.getenv("API_USERNAME")
        self.__password = os.getenv("API_PASSWORD")

    def connect_to_api(self):
        print("Username: " + str(self.__username))
        print("Password: " + str(self.__password))