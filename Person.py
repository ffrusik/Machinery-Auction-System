class Person:
    def __init__(self, name, phone, bank_account, address, email):
        self._name = name
        self._phone = phone
        self._bank_account = bank_account
        self._address = address
        self._email = email
        
    def display(self):
        return f"Name: {self._name}, Phone: {self._phone}, Bank Account: {self._bank_account}, Address: {self._address}, Email: {self._email}"
    
    def set_name(self, name):
        self._name = name

    def set_phone(self, phone):
        self._phone = phone

    def set_bank_account(self, bank_account):
        self._bank_account = bank_account

    def set_address(self, address):
        self._address = address

    def set_email(self, email):
        self._email = email

class Staff(Person):
    def __init__(self, name, phone, bank_account, address, email, position, salary, logon_id, password, pps_no):
        super().__init__(name, phone, bank_account, address, email)
        self._position = position
        self._salary = salary
        self._logon_id = logon_id
        self._password = password
        self._pps_no = pps_no

class Seller(Person):
    _sellerNo = 0

    def __init__(self, name, phone, bank_account, address, email):
        super().__init__(name, phone, bank_account, address, email)
        self._sellerNo = Seller.generate_seller_id()

    @staticmethod
    def generate_seller_id():
        Seller._sellerNo += 1
        return Seller._sellerNo

class Buyer(Person):
    _buyer_no = 0

    def __init__(self, name, phone, bank_account, address, email, vat_number):
        super().__init__(name, phone, bank_account, address, email)
        self._vatNumber = vat_number
        self._buyer_no = Buyer.generate_buyer_id()

    @staticmethod
    def generate_buyer_id():
        Buyer._buyer_no += 1
        return Buyer._buyer_no

    def display_user_info(self):
            print(f"User ID: {self._buyer_no}, Name: {self._name}")

    # setters
    def set_vat_number(self, vat_number):
        self._vatNumber = vat_number

class Auctioneer(Person):
    def __init__(self, name, phone, bank_account, address, email, auction_id):
        super().__init__(name, phone, bank_account, address, email)
        self._auction_id = auction_id
