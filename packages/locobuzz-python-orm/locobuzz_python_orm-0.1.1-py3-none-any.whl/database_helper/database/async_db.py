from collections import namedtuple
from threading import Lock

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


class AsyncDatabase:
    _instance = None
    _lock = Lock()

    def __new__(cls, connection_string, min_connections=5, max_connections=10, **engine_kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(AsyncDatabase, cls).__new__(cls)
                # Remove explicit poolclass setting
                engine_kwargs.setdefault('pool_size', min_connections)
                engine_kwargs.setdefault('max_overflow', max_connections - min_connections)
                cls.engine = create_async_engine(connection_string, **engine_kwargs)
                cls.SessionFactory = sessionmaker(cls.engine, expire_on_commit=False, class_=AsyncSession)
                cls.scoped_session = cls.SessionFactory
        return cls._instance

    async def __aenter__(self):
        self.session = self.scoped_session()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def execute_query(self, query, is_update: bool = False):
        """Execute a SQL Alchemy ORM query and return the result asynchronously."""
        async with self.session.begin():
            result = await self.session.execute(query)
            if is_update:
                await self.session.commit()
            return result.fetchall()

    async def query_dataframe(self, query):
        """Execute a query and return results as a Pandas DataFrame asynchronously."""
        try:
            import pandas as pd
        except ImportError:
            raise ImportError(
                "Pandas is required to use query_dataframe(). Please install it with 'pip install pandas'.")

        async with self.session.begin():
            result = await self.session.execute(query)
            df = pd.DataFrame(result.fetchall())
            df.columns = result.keys()
            return df

    async def query_tuples(self, query):
        """Execute a query and return results as a list of tuples asynchronously."""
        return await self.execute_query(query)

    async def query_named_tuples(self, query, name="Result"):
        """Execute a query and return results as a list of named tuples asynchronously."""
        tuples = await self.execute_query(query)
        if tuples:
            # Retrieving column names from the first Row object
            Result = namedtuple(name, tuples[0]._mapping.keys())
            return [Result(*t) for t in tuples]
        return []

    async def close(self):
        """Close the database engine and release all connections."""
        await self.engine.dispose()


# Example usage:
if __name__ == "__main__":
    import asyncio
    from sqlalchemy import text
    import urllib.parse


    async def main():
        # Checking with mysql connection
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
        connection_string = f"mssql+aioodbc://{username}:{encoded_password}@{host}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
        db = AsyncDatabase(connection_string, min_connections=1, max_connections=1)
        query = text("SELECT * FROM mstCategories")

        async with db as database:
            result = await database.query_tuples(query)
            print(result)  # List of tuples output
            try:
                df = await database.query_dataframe(query)
                print(df)  # DataFrame output
            except ImportError:
                pass
            named_result = await database.query_named_tuples(query)
            print(named_result)  # List of named tuples output

        await db.close()


    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()  # Close the loop only after all async operations are done
