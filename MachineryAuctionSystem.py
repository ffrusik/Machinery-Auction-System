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

    def change_buyer_details(self, buyer_no, name = None, phone = None, bank_account = None, address = None, email = None, vat_number = None):
        for i in self._buyers:
            if i.get_buyer_number() == buyer_no:
                i.set_name(name if name is not None else i.get_name())
                i.set_phone(phone if phone is not None else i.get_phone())
                i.set_bank_account(bank_account if bank_account is not None else i.get_bank_account())
                i.set_address(address if address is not None else i.get_address())
                i.set_email(email if email is not None else i.get_email())
                i.set_vat_number(vat_number if vat_number is not None else i.get_vat_number())
                break

    def start_auction(self):
        try:
            fh = open("buyers.txt", "rb")
        except FileNotFoundError:
            print("buyers were not found")
        else:
            self._buyers = pickle.load(fh)
            fh.close()

        try:
            fh = open("sellers.txt", "rb")
            self._sellers = pickle.load(fh)
            fh.close()
        except FileNotFoundError:
            print("sellers were not found")

        try:
            fh = open("employees.txt", "rb")
            self._employees = pickle.load(fh)
            fh.close()
        except FileNotFoundError:
            print("employees were not found")

        try:
            fh = open("lots.txt", "rb")
            self._lots = pickle.load(fh)
            fh.close()
        except FileNotFoundError:
            print("lots were not found")

        try:
            fh = open("sales.txt", "rb")
            self._sales = pickle.load(fh)
            fh.close()
        except FileNotFoundError:
            print("sales were not found")

        try:
            fh = open("payments.txt", "rb")
            self._payments = pickle.load(fh)
            fh.close()
        except FileNotFoundError:
            print("payments were not found")

        print("Machinery Auction System: ")
        print("Welcome to the auction!")
        print("1. Register as a Buyer")
        print("2. Register as a Seller")
        print("3. Register as an Employee")
        print("4. Create a Lot")
        print("5. Place a Bid")
        print("6. View Auction Results")
        print("7. Exit")

machinery_auction_system = MachineryAuctionSystem()
machinery_auction_system.start_auction()
