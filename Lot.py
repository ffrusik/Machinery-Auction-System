class Lot:
    def __init__(self,LotNumber,SellerNo):
        self._Lotnumber = LotNumber
        self._SellerNo = SellerNo

    
class Vehicle(Lot):
    def __init__(self, lot_number, seller_no, registration, make, model, year, hours_used):
        super().__init__(lot_number, seller_no)
        self._registration = registration
        self._make = make
        self._model = model
        self._year = year
        self._hours_used = hours_used

class nonVehicle(Lot):
    def __init__(self, lot_number, seller_no, description):
        super().__init__(lot_number, seller_no)
        self._description = description
