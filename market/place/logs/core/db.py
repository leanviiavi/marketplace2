import sqlite3 as sq
from typing import NamedTuple












class Connection(NamedTuple):
    name: str
    connection: sq.Connection
    cursor: sq.Cursor


class Response(NamedTuple):
    id: int
    data: str


class DB:
    def __init__ (self, db_name: str = "test.db") -> None:
        self.db_name = db_name
        self.connection = self.connect()
    

    def connect(self) -> Connection:
        connection = sq.connect(self.db_name)
        cursor = connection.cursor()
        return Connection(name=self.db_name, connection=connection, cursor=cursor)
    

    def execute(self, resp: str) -> Response:
        if (isinstance(resp, str)):
            try:
                resp = self.connection.connection.execute(resp).fetchall()
                self.connection.connection.commit()
                if len(resp) < 1:
                    return "no data"
                return resp

            except:

                try:
                    exec = self.connection.connection.execute(resp)
                    self.connection.connection.commit()

                    return exec

                except:

                    return "bad response"
        else:

            return "bad data"




# Для создания объекта базы
# sql = DB("test.db")

# Для пример создания таблицы
# print(sql.execute("CREATE TABLE test (id int, name varchar(32))"))

# Пример отправки и получения данных
# print(sql.execute('INSERT INTO test (id, name) VALUES (0, "Andrew")'))
# sql.execute('SELECT * FROM test')

# sql = DB()
# print(sql.execute('SELECT * FROM test WHERE'))

# # Заполняем шаблонными данными
# print(sql.execute('CREATE TABLE users (id int, name varchar(32), private_key varchar(256), public_key varchar(256))'))
# sql.execute("DELETE FROM users")
# sql.execute('INSERT INTO users VALUES(0, "Andrew", "fdb9bd65d441a438ebeb973c6fc5c70dec833f18995272a91c849ae45dfe2829", "0x995AFE0263103CCdC8Ba6a015DdBA623321eab4C")')
# sql.execute('INSERT INTO users VALUES(1, "Second", "93be121174ff26c4c79fb49e8b106273b14c8984e0733db82ee37bb9e009cd72", "0x042605ad8f7Eca8d2133f2794E78eEd7E2d9c01d")')

# print(sql.execute("SELECT * FROM users"))


# sql.execute("DELETE FROM nfts2")
# print(sql.execute('CREATE TABLE nfts2 (id int, name varchar(32), price float, user int)'))
# sql.execute('INSERT INTO nfts2 VALUES(0, "product_1", 1, 0)')
# sql.execute('INSERT INTO nfts2 VALUES(1, "product_2", 1, 1)')
# sql.execute('INSERT INTO nfts2 VALUES(2, "product_3", 1, 1)')
# print(sql.execute("SELECT * FROM nfts2"))
# print(sql.execute("SELECT nfts2.name, nfts2.price, users.name FROM nfts2 LEFT JOIN users ON nfts2.user = users.id"))

