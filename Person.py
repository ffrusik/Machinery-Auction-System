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
    def __init__(self, name, phone, bankAccount, address, email, sellerNo):
        super().__init__(name, phone, bankAccount, address, email)
        self._sellerNo = sellerNo

class Buyer(Person):
    def __init__(self, name, phone, bankAccount, address, email, buyerNo, vatNumber):
        super().__init__(name, phone, bankAccount, address, email)
        self._buyerNo = buyerNo
        self._vatNumber = vatNumber

class Auctioneer(Person):
    def __init__(self, name, phone, bankAccount, address, email, auctionId):
        super().__init__(name, phone, bankAccount, address, email)
        self._auctionId = auctionId
