from Payment import Payment
from Person import *
from Lot import Lot, Vehicle, nonVehicle
from Sale import Sale
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

    def save_data(self):
        with open("buyers.txt", "wb") as fh:
            pickle.dump(self._buyers, fh)
        with open("sellers.txt", "wb") as fh:
            pickle.dump(self._sellers, fh)
        with open("employees.txt", "wb") as fh:
            pickle.dump(self._employees, fh)
        with open("lots.txt", "wb") as fh:
            pickle.dump(self._lots, fh)
        with open("sales.txt", "wb") as fh:
            pickle.dump(self._sales, fh)
        with open("payments.txt", "wb") as fh:
            pickle.dump(self._payments, fh)

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
        
        while True:
            print("\n--- Main Menu ---")
            print("1. Register as a Buyer")
            print("2. Register as a Seller")
            print("3. Register as an Employee")
            print("4. Create a Lot")
            print("5. Place a Bid")
            print("6. View Auction Results")
            print("7. Exit")
            
            choice = input("\nEnter your choice (1-7): ")
            
            match choice:
                case '1':
                    print("\n--- Register a New Buyer ---")
                    name = input("Enter Name: ")
                    phone = input("Enter Phone: ")
                    bank_account = input("Enter Bank Account: ")
                    address = input("Enter Address: ")
                    email = input("Enter Email: ")
                    vat_number = input("Enter VAT Number (leave blank if none): ")
                    
                    new_buyer = Buyer(name, phone, bank_account, address, email, vat_number)
                    self.register_buyer(new_buyer)
                    print("\nSuccess! Buyer registered.")
                    new_buyer.display_user_info()

                case '2':
                    print("\n--- Register a New Seller ---")
                    name = input("Enter Name: ")
                    phone = input("Enter Phone: ")
                    bank_account = input("Enter Bank Account: ")
                    address = input("Enter Address: ")
                    email = input("Enter Email: ")
                    
                    new_seller = Seller(name, phone, bank_account, address, email)
                    self.register_seller(new_seller)
                    print(f"\nSuccess! Seller '{name}' registered with Seller ID: {new_seller._sellerNo}")

                case '3':
                    print("\n--- Register a New Employee ---")
                    name = input("Enter Name: ")
                    phone = input("Enter Phone: ")
                    bank_account = input("Enter Bank Account: ")
                    address = input("Enter Address: ")
                    email = input("Enter Email: ")
                    position = input("Enter Position: ")
                    salary = input("Enter Salary: ")
                    logon_id = input("Enter Logon ID: ")
                    password = input("Enter Password: ")
                    pps_no = input("Enter PPS Number: ")
                    
                    new_employee = Staff(name, phone, bank_account, address, email, position, salary, logon_id, password, pps_no)
                    self.register_employee(new_employee)
                    print(f"\nSuccess! Employee '{name}' registered.")

                case '4':
                    print("\n--- Create a Lot ---")
                    lot_type = input("Is this a Vehicle or Non-Vehicle? (v/n): ").lower()
                    lot_number = input("Enter Lot Number: ")
                    seller_no = int(input("Enter Seller Number (ID): "))
                    
                    if lot_type == 'v':
                        registration = input("Enter Registration: ")
                        make = input("Enter Make: ")
                        model = input("Enter Model: ")
                        year = input("Enter Year: ")
                        hours_used = input("Enter Hours Used: ")
                        new_lot = Vehicle(lot_number, seller_no, registration, make, model, year, hours_used)
                        self.create_lot(new_lot)
                        print(f"\nSuccess! Vehicle Lot '{lot_number}' created.")
                    elif lot_type == 'n':
                        description = input("Enter Description: ")
                        new_lot = nonVehicle(lot_number, seller_no, description)
                        self.create_lot(new_lot)
                        print(f"\nSuccess! Non-Vehicle Lot '{lot_number}' created.")
                    else:
                        print("Invalid lot type selected.")

                case '5':
                    print("\n--- Record a Sale (Place a Bid) ---")
                    site_no = input("Enter Site Number: ")
                    date = input("Enter Date (YYYY-MM-DD): ")
                    lot_no = input("Enter Lot Number: ")
                    buyer_no = int(input("Enter Buyer Number (ID): "))
                    amount = float(input("Enter Sale Amount: "))
                    commission = float(input("Enter Commission: "))
                    vat = float(input("Enter VAT: "))
                    paid = input("Is it paid? (y/n): ").lower() == 'y'
                    
                    new_sale = Sale(site_no, date, lot_no, buyer_no, amount, commission, vat, paid)
                    self.record_sale(new_sale)
                    print("\nSuccess! Sale recorded.")
                    
                    if paid:
                        new_payment = Payment(date, site_no, buyer_no, amount)
                        self.process_payment(new_payment)
                        print("Payment processed and recorded.")

                case '6':
                    print("\n--- View Auction Results ---")
                    if not self._sales:
                        print("No sales recorded yet.")
                    else:
                        print("Recorded Sales:")
                        for sale in self._sales:
                            print(f"Lot No: {sale.lot_no} | Buyer No: {sale.buyer_no} | Amount: €{sale.amount} | Date: {sale.date} | Paid: {sale.paid}")

                case '7':
                    print("\nSaving data and exiting...")
                    self.save_data()
                    print("Exiting...")
                    break

                case _:
                    print("\nInvalid choice. Please pick 1-7.")

machinery_auction_system = MachineryAuctionSystem()
machinery_auction_system.start_auction()
