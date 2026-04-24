class Person:
    def __init__(self, name, phone, bank_account, address, email):
        self._name = name
        self._phone = phone
        self._bank_account = bank_account
        self._address = address
        self._email = email

    def display(self):
        return (f"Name: {self._name}, Phone: {self._phone}, "
                f"Bank Account: {self._bank_account}, "
                f"Address: {self._address}, Email: {self._email}")

    # Getters
    def get_name(self):         
        return self._name
    def get_phone(self):        
        return self._phone
    def get_bank_account(self): 
        return self._bank_account
    def get_address(self):      
        return self._address
    def get_email(self):        
        return self._email

    # Setters
    def set_name(self, name):               
        self._name = name
    def set_phone(self, phone):             
        self._phone = phone
    def set_bank_account(self, ba):         
        self._bank_account = ba
    def set_address(self, address):         
        self._address = address
    def set_email(self, email):             
        self._email = email


class Buyer(Person):
    # Class-level counter - will be synced from file on load
    _next_id = 1

    def __init__(self, name, phone, bank_account, address, email, vat_number=""):
        super().__init__(name, phone, bank_account, address, email)
        self._vat_number = vat_number
        self._buyer_no = Buyer._next_id
        Buyer._next_id += 1

    # Getters
    def get_buyer_number(self):  
        return self._buyer_no
    def get_vat_number(self):    
        return self._vat_number
    def has_vat(self):           
        return self._vat_number.strip() != ""

    # Setters
    def set_vat_number(self, vat): self._vat_number = vat

    def display_user_info(self):
        print(f"Buyer No: {self._buyer_no}, Name: {self._name}, "
              f"VAT: {self._vat_number if self._vat_number else 'None'}")


class Seller(Person):
    _next_id = 1

    def __init__(self, name, phone, bank_account, address, email):
        super().__init__(name, phone, bank_account, address, email)
        self._seller_no = Seller._next_id
        Seller._next_id += 1

    def get_seller_no(self): 
        return self._seller_no

    def display_user_info(self):
        print(f"Seller No: {self._seller_no}, Name: {self._name}")


class Staff(Person):
    def __init__(self, name, phone, bank_account, address, email,
                 position, salary, logon_id, password, pps_no):
        super().__init__(name, phone, bank_account, address, email)
        self._position = position
        self._salary = salary
        self._logon_id = logon_id
        self._password = password
        self._pps_no = pps_no

    def get_position(self):  
        return self._position
    def get_salary(self):    
        return self._salary
    def get_logon_id(self):  
        return self._logon_id
    def get_pps_no(self):    
        return self._pps_no


class Auctioneer(Person):
    def __init__(self, name, phone, bank_account, address, email, company_name):
        super().__init__(name, phone, bank_account, address, email)
        self._company_name = company_name

    def get_company_name(self): 
        return self._company_name