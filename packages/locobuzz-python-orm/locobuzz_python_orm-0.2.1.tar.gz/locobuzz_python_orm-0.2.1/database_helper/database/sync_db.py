import urllib
from collections import namedtuple
from threading import Lock

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session


class SyncDatabase:
    _instance = None
    _lock = Lock()

    def __new__(cls, connection_string, min_connections=1, max_connections=1, **engine_kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(SyncDatabase, cls).__new__(cls)
                engine_kwargs.setdefault('pool_size', min_connections)
                engine_kwargs.setdefault('max_overflow', max_connections - min_connections)
                cls.engine = create_engine(connection_string, **engine_kwargs)
                cls.SessionFactory = sessionmaker(bind=cls.engine)
                cls.scoped_session = scoped_session(cls.SessionFactory)
        return cls._instance

    def __enter__(self):
        self.session = self.scoped_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def execute_query(self, query, is_update: bool = False):
        """Execute a SQL Alchemy ORM query and return the result."""
        try:
            result = self.session.execute(query)
            if is_update:
                self.session.commit()
            return result.fetchall()
        except Exception as e:
            self.session.rollback()
            raise e

    def query_dataframe(self, query):
        """Execute a query and return results as a Pandas DataFrame."""
        try:
            import pandas as pd
        except ImportError:
            raise ImportError("Pandas is required to use query_dataframe(). Please install it with 'pip install pandas'.")

        try:
            result = self.session.execute(query)
            df = pd.DataFrame(result.fetchall())
            df.columns = result.keys()
            return df
        finally:
            self.session.close()

    def query_tuples(self, query):
        """Execute a query and return results as a list of tuples."""
        return self.execute_query(query)

    def query_named_tuples(self, query, name="Result"):
        """Execute a query and return results as a list of named tuples."""
        tuples = self.execute_query(query)
        if tuples:
            Result = namedtuple(name, tuples[0].keys())
            return [Result(*t) for t in tuples]
        return []

    def close(self):
        """Close the database engine and release all connections."""
        self.engine.dispose()


# Example usage:
if __name__ == "__main__":
    # Assuming you have a valid connection string and ORM query
    username = "admin"
    password = "Mysql@12345"
    host = "43.205.214.5"
    database = "test"

    username = "sa"
    password = "Mssql1@1234"
    database = "master"

    # URL encode the password
    encoded_password = urllib.parse.quote(password)

    # Construct the connection string
    connection_string = f"mssql+pyodbc://{username}:{encoded_password}@{host}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
    db = SyncDatabase(connection_string, min_connections=1, max_connections=1)
    query = text("SELECT * FROM mstCategories")

    with db as database:
        result = database.query_tuples(query)
        print(result)  # List of tuples output
        # df = database.query_dataframe(query)
        # print(df)  # DataFrame output
        named_result = database.query_named_tuples(query)
        print(named_result)  # List of named tuples output

    db.close()