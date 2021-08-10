from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(minconn = 1,
                                            maxconn = 1, 
                                            database='restaurants', 
                                            user='sedalofski', 
                                            password='123456', 
                                            host="localhost")

class ConnectionFromPool:
    def __init__(self):
        self.connection = None
    
    def __enter__(self):   # when enter 'with' block
        self.connection = connection_pool.getconn()
        return self.connection
    
    def __exit__(self, exc_type , exc_val, exc_tb):  # when exit 'with' block
        self.connection.commit()
        connection_pool.putconn(self.connection)
