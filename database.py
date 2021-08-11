from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(minconn = 1,
                                            maxconn = 1, 
                                            database='restaurants', 
                                            user='sedalofski', 
                                            password='123456', 
                                            host="localhost")

class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def __enter__(self):   # when enter 'with' block
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exception_type , exception_value, exception_traceback):  # when exit 'with' block
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)
