from psycopg2 import pool


class Database:
    connection_pool = None

    @classmethod
    def initialize(cls):
        cls.connection_pool = pool.SimpleConnectionPool(minconn = 1,
                                                        maxconn = 10, 
                                                        database='restaurants', 
                                                        user='sedalofski', 
                                                        password='123456', 
                                                        host="localhost")
    @classmethod
    def get_connection(cls):
        return cls.connection_pool.getconn()

    @classmethod
    def put_connection(cls,connection):
        cls.connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.connection_pool.closeall()




class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def __enter__(self):   # when enter 'with' block
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exception_type , exception_value, exception_traceback):  # when exit 'with' block
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.put_connection(self.connection)
