import psycopg2

database_manager_instance = None

class DatabaseManager:
    def __init__(self):
        self.__connection = self.__connect_to_database()

    def __connect_to_database(self):
        try:
            with psycopg2.connect() as conn:
                return conn
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)


def get_instance():
    global database_manager_instance
    if database_manager_instance is None:
        database_manager_instance = DatabaseManager()
    return database_manager_instance