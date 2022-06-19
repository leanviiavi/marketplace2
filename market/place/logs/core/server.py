from .db import DB
from .app import App

class Marketplace:
    def __init__(self, name_db: str = "test.db"):
        self.name_db = name_db

    def load(self):
        db_ = DB(self.name_db)
        return db_.execute("SELECT * FROM nfts")
    
    def loadAccount(self, user_id: int):
        db_ = DB(self.name_db)
        return db_.execute(f"SELECT * FROM nfts WHERE user={user_id}")

    def loadCurrent(self, id: int):
        db_ = DB(self.name_db)
        return db_.execute(f"SELECT * FROM nfts WHERE id={id}")
    
    def info_account_coins(self, user_id: int) -> float:
        db_ = DB(self.name_db)
        app = App()
        user_hash = db_.execute(f"SELECT public_key FROM accounts WHERE id={user_id}")
        return float(app.infoCoins(user_hash=user_hash[0][0])) / 1000000000000000000

    def load_product_users(self, products_id: list) -> list:
        db_ = DB(self.name_db)
        result = []
        for i in products_id:
            result.append(db_.execute(f"SELECT user_nick FROM accounts WHERE id={i[1]}"))
        return result

    def sell(self, current_product_id: int, ac_1: str):
        db_ = DB(self.name_db)
        app = App()

        
        ac_2 = db_.execute(f"SELECT accounts FROM nfts WHERE id='{current_product_id}'")[0][0]
        current_user_key = db_.execute(f"SELECT public_key FROM accounts WHERE id='{ac_1}'")[0][0]
        transfer_user_key = db_.execute(f"SELECT public_key FROM accounts WHERE id='{ac_2}'")[0][0]
        private_key = db_.execute(f"SELECT private_key FROM accounts WHERE id='{ac_1}'")[0][0]
        product_price = db_.execute(f"SELECT price FROM nfts WHERE id='{current_product_id}'")[0][0]

        # print(current_user_id, transfer_user_id, private_key)

        hash_result = app.transaction(current_user_key, transfer_user_key, private_key, product_price)
        return hash_result

    def image_by_id(self, id: int):
        db_ = DB(self.name_db)
        product_name = db_.execute(f"SELECT name FROM nfts WHERE id='{id}'")[0][0]
        return f"logs/img/card/{product_name}"
    

    def create_demo(self):
        db_ = DB("demo3.db")
        
        # CREATE TABLES
            #ACCOUNT

        ac = db_.execute('''CREATE TABLE accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_nick varchar(32),
            private_key varchar(128),
            public_key varchar(128)
            )''')

        print("Создаю аккаунты")
            #NFTS
        
        nfts = db_.execute('''CREATE TABLE nfts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id int,
            price float,
            name varchar(128),
            description varchar(128),
            date_of_upload varchar(32)
            )''')

        print("Создаю NFT")

        print(ac, nfts)
        
        # ACCOUNTS
        db_.execute("INSERT INTO accounts VALUES (0, 'leanviiavi', '93be121174ff26c4c79fb49e8b106273b14c8984e0733db82ee37bb9e009cd72', '0x042605ad8f7Eca8d2133f2794E78eEd7E2d9c01d')")
        db_.execute("INSERT INTO accounts VALUES (1, 'jeka', 'fdb9bd65d441a438ebeb973c6fc5c70dec833f18995272a91c849ae45dfe2829', '0x995AFE0263103CCdC8Ba6a015DdBA623321eab4C')")
        # NFTS
        db_.execute("INSERT INTO nfts VALUES (1, 0, 0.001, 'image-equilibrium.jpg', 'no description data', '18.06.2022')")
        db_.execute("INSERT INTO nfts VALUES (2, 1, 0.005, 'image-equilibrium.jpg', 'no description data 2', '18.06.2022')")

        # RESULT
        print(db_.execute("SELECT * FROM accounts"))
        print(db_.execute("SELECT * FROM nfts"))


        
m = Marketplace()
# res = m.sell(0, ac_1 = 0)
m.create_demo()
# print(res)

        