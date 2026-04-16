from Payment import Payment
from Person import *
import pickle

class MachineryAuctionSystem:
    def __init__(self):
        self._buyers = []
        self._sellers = []
        self._employees = []
        self._lots = []
        self._sales = []
        self._payments = []

    def register_buyer(self, buyer):
        self._buyers.append(buyer)

    def register_seller(self, seller):
        self._sellers.append(seller)

    def register_employee(self, employee):
        self._employees.append(employee)

    def create_lot(self, lot):
        self._lots.append(lot)

    def record_sale(self, sale):
        self._sales.append(sale)

    def process_payment(self, payment):
        self._payments.append(payment)

    def change_buyer_details(self, buyer_no, name = None, phone = None, bank_account = None, address = None, email = None):
        for i in self._buyers:
            if i.get_buyer_number() == buyer_no:
                i.set_name(name if name is not None else i.get_name())
                i.set_phone(phone if phone is not None else i.get_phone())
                i.set_bank_account(bank_account if bank_account is not None else i.get_bank_account())
                i.set_address(address if address is not None else i.get_address())
                i.set_email(email if email is not None else i.get_email())
                break
       


machinery_auction_system = MachineryAuctionSystem()
