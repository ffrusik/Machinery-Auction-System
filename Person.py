class Person:
    def __init__(self, name, phone, bankAccount, address, email):
        self._name = name
        self._phone = phone
        self._bankAccount = bankAccount
        self._address = address
        self._email = email
    def display(self):
        return f"Name: {self._name}, Phone: {self._phone}, Bank Account: {self._bankAccount}, Address: {self._address}, Email: {self._email}"

class Staff(Person):
    def __init__(self, name, phone, bankAccount, address, email, position, salary, logonID, password, ppsNo):
        super().__init__(name, phone, bankAccount, address, email)
        self._position = position
        self._salary = salary
        self._logonID = logonID
        self._password = password
        self._ppsNo = ppsNo

class Seller(Person):
    _sellerNo = 0

    def __init__(self, name, phone, bankAccount, address, email):
        super().__init__(name, phone, bankAccount, address, email)
        self._sellerNo = Seller.generate_seller_id()

    @staticmethod
    def generate_seller_id():
        Seller._sellerNo += 1
        return Seller._sellerNo

class Buyer(Person):
    _buyerNo = 0

    def __init__(self, name, phone, bankAccount, address, email, vatNumber):
        super().__init__(name, phone, bankAccount, address, email)
        self._vatNumber = vatNumber
        self._buyerNo = Buyer.generate_buyer_id()

    @staticmethod
    def generate_buyer_id():
        Buyer._buyerNo += 1
        return Buyer._buyerNo

    def display_user_info(self):
            print(f"User ID: {self._buyerNo}, Name: {self._name}")

class Auctioneer(Person):
    def __init__(self, name, phone, bankAccount, address, email, auctionId):
        super().__init__(name, phone, bankAccount, address, email)
        self._auctionId = auctionId
