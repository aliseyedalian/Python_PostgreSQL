from psycopg2 import pool


class Database:
    __connection_pool = None    # __ for private variable

    @classmethod
    def initialize(cls,**kwargs):  # **kwargs means any named parameters
        cls.__connection_pool = pool.SimpleConnectionPool(**kwargs)
    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def put_connection(cls,connection):
        cls.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()




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
