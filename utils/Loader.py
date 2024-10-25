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
        self.__connection_token = None

    def __send_request(self, request_type, endpoint, headers, data: None):
        self.__connection.request(request_type, endpoint, data, headers)
        return self.__connection.getresponse()

    def __stop_connection(self):
        self.__connection.close()

    def send_post_request(self, endpoint, post_data, headers):
        return self.__send_request("POST", endpoint, headers, post_data)

    def send_get_request(self, endpoint, headers):
        return self.__send_request("POST", endpoint, headers, None)

    def send_patch_request(self, endpoint, patch_data, headers):
        return self.__send_request("POST", endpoint, headers, patch_data)

    def __connect_to_api(self):
        print("Username: " + str(self.__username))
        print("Password: " + str(self.__password))