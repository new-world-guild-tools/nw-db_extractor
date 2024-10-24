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

    def __stop_connection(self):
        self.__connection.close()

    def __send_post_request(self, endpoint, post_data, headers):
        self.__connection.request("POST", endpoint, post_data, headers)
        return self.__connection.getresponse()

    def __send_get_request(self, endpoint, headers):
        self.__connection.request("GET", endpoint, None, headers)
        return self.__connection.getresponse()

    def connect_to_api(self):
        print("Username: " + str(self.__username))
        print("Password: " + str(self.__password))