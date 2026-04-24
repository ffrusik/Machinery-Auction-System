class Lot:
    def __init__(self, lot_number, seller_no):
        self._lot_number = lot_number
        self._seller_no = seller_no

    def get_lot_number(self):  
        return self._lot_number
    def get_seller_no(self):   
        return self._seller_no

    def display(self):
        return f"Lot #{self._lot_number} | Seller: {self._seller_no}"


class Vehicle(Lot):
    def __init__(self, lot_number, seller_no, registration,
                 make, model, year, hours_used):
        super().__init__(lot_number, seller_no)
        self._registration = registration
        self._make = make
        self._model = model
        self._year = year
        self._hours_used = hours_used

    def get_registration(self): 
        return self._registration
    def get_make(self):         
        return self._make
    def get_model(self):        
        return self._model
    def get_year(self):         
        return self._year
    def get_hours_used(self):   
        return self._hours_used

    def set_registration(self, r): 
        self._registration = r
    def set_make(self, m):         
        self._make = m
    def set_model(self, m):        
        self._model = m
    def set_year(self, y):         
        self._year = y
    def set_hours_used(self, h):   
        self._hours_used = h

    def display(self):
        return (f"[Vehicle] Lot #{self._lot_number} | "
                f"{self._year} {self._make} {self._model} | "
                f"Reg: {self._registration} | Hours: {self._hours_used} | "
                f"Seller: {self._seller_no}")


class NonVehicle(Lot):
    def __init__(self, lot_number, seller_no, description):
        super().__init__(lot_number, seller_no)
        self._description = description

    def get_description(self):       
        return self._description
    def set_description(self, desc): 
        self._description = desc

    def display(self):
        return (f"[Non-Vehicle] Lot #{self._lot_number} | "
                f"{self._description} | Seller: {self._seller_no}")