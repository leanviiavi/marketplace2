from web3 import Web3






# Создание экземпляра
# app = App()

# Наша транзакция
# res_transaction = app.transaction("0x042605ad8f7Eca8d2133f2794E78eEd7E2d9c01d", "0x995AFE0263103CCdC8Ba6a015DdBA623321eab4C", "93be121174ff26c4c79fb49e8b106273b14c8984e0733db82ee37bb9e009cd72", 10)

# Результат
# print(res_transaction)




'''


    Логика транзакций




'''

class App:
    def __init__(self):
        self.URL = "http://127.0.0.1:7545"
        self.web3 = Web3(Web3.HTTPProvider(self.URL))

    '''

        Формируем запрос от 1 до 2 аккаунта
        Берем приватный ключ первого аккаунта


    '''

    def infoCoins(self, user_hash: str) -> float:
        return self.web3.eth.get_balance(user_hash)


    def transaction(self, ac_1: str, ac_2: str, private_key: str, price: float):
        self.account_1 = ac_1
        self.account_2 = ac_2
        self.price = price

        self.private_key = private_key
        '''

            Формируем саму транзакцию


        '''
        self.nonce = self.web3.eth.getTransactionCount(self.account_1)

        self.transaction = {
            'nonce': self.nonce,
            'to': self.account_2,
            'value': self.web3.toWei(self.price, 'ether'),
            'gas':2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        }

        '''
        
            Запускаем нашу транзацкию и возвращаем результат (хэш транзакции)
        
        
        '''
        try:
            self.signed_tx = self.web3.eth.account.sign_transaction(self.transaction, self.private_key)
            return self.web3.toHex(self.web3.eth.send_raw_transaction(self.signed_tx.rawTransaction))
        except:
            return "bad transaction"



class Auth:
    def __init__(self, id: int = -1):
        self.id = id
    
    def oauth(self):
        if self.id != -1 or self.id != None:
            return "good"
        else:
            return "bad"