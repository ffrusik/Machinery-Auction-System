from Payment import Payment
from Person import Buyer, Seller, Staff, Auctioneer
from Lot import Vehicle, NonVehicle
from Sale import Sale
import pickle
from datetime import date


class MachineryAuctionSystem:
    def __init__(self):
        self._buyers = []
        self._sellers = []
        self._employees = []
        self._lots = []
        self._sales = []
        self._payments = []

    # Registration helpers

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

    # Lookup helpers

    def find_buyer(self, buyer_no):
        for b in self._buyers:
            if b.get_buyer_number() == buyer_no:
                return b
        return None

    def find_seller(self, seller_no):
        for s in self._sellers:
            if s.get_seller_no() == seller_no:
                return s
        return None

    def find_lot(self, lot_no):
        for l in self._lots:
            if l.get_lot_number() == lot_no:
                return l
        return None

    # Persistence

    def save_data(self):
        data = {
            "buyers":    self._buyers,
            "sellers":   self._sellers,
            "employees": self._employees,
            "lots":      self._lots,
            "sales":     self._sales,
            "payments":  self._payments,
            "buyer_next_id":  Buyer._next_id,
            "seller_next_id": Seller._next_id,
        }
        with open("auction_data.pkl", "wb") as fh:
            pickle.dump(data, fh)
        print("Data saved.")

    def load_data(self):
        try:
            with open("auction_data.pkl", "rb") as fh:
                data = pickle.load(fh)
            self._buyers    = data.get("buyers", [])
            self._sellers   = data.get("sellers", [])
            self._employees = data.get("employees", [])
            self._lots      = data.get("lots", [])
            self._sales     = data.get("sales", [])
            self._payments  = data.get("payments", [])
            # Restore counters so IDs never repeat
            Buyer._next_id  = data.get("buyer_next_id", 1)
            Seller._next_id = data.get("seller_next_id", 1)
            print("Previous data loaded successfully.")
        except FileNotFoundError:
            print("No previous data found - starting fresh.")

    # Menu actions

    def _register_buyer(self):
        print("\n--- Register a New Buyer ---")
        name        = input("Name: ")
        phone       = input("Phone: ")
        bank_acc    = input("Bank Account: ")
        address     = input("Address: ")
        email       = input("Email: ")
        vat_number  = input("VAT Number (leave blank if none): ")
        b = Buyer(name, phone, bank_acc, address, email, vat_number)
        self.register_buyer(b)
        print(f"\nBuyer registered. Buyer No: {b.get_buyer_number()}")

    def _register_seller(self):
        print("\n--- Register a New Seller ---")
        name     = input("Name: ")
        phone    = input("Phone: ")
        bank_acc = input("Bank Account: ")
        address  = input("Address: ")
        email    = input("Email: ")
        s = Seller(name, phone, bank_acc, address, email)
        self.register_seller(s)
        print(f"\nSeller registered. Seller No: {s.get_seller_no()}")

    def _register_employee(self):
        print("\n--- Register a New Employee ---")
        name     = input("Name: ")
        phone    = input("Phone: ")
        bank_acc = input("Bank Account: ")
        address  = input("Address: ")
        email    = input("Email: ")
        position = input("Position: ")
        salary   = float(input("Salary: "))
        logon_id = input("Logon ID: ")
        password = input("Password: ")
        pps_no   = input("PPS Number: ")
        e = Staff(name, phone, bank_acc, address, email,
                  position, salary, logon_id, password, pps_no)
        self.register_employee(e)
        print(f"\nEmployee '{name}' registered.")

    def _create_lot(self):
        print("\n--- Create a Lot ---")

        # Auto-assign the next lot number (0–5000, reused per auction date)
        used = {l.get_lot_number() for l in self._lots}
        next_no = 0
        while next_no in used and next_no <= 5000:
            next_no += 1
        if next_no > 5000:
            print("Maximum lot numbers reached (5000).")
            return

        print(f"Lot number will be: {next_no}")

        # Validate seller
        try:
            seller_no = int(input("Seller No: "))
        except ValueError:
            print("Invalid seller number.")
            return
        if not self.find_seller(seller_no):
            print("Seller not found.")
            return

        lot_type = input("Type (V=Vehicle / N=Non-Vehicle): ").strip().upper()
        if lot_type == "V":
            reg      = input("Registration: ")
            make     = input("Make: ")
            model    = input("Model: ")
            year     = input("Year: ")
            hours    = input("Hours Used: ")
            lot = Vehicle(next_no, seller_no, reg, make, model, year, hours)
        elif lot_type == "N":
            desc = input("Description: ")
            lot = NonVehicle(next_no, seller_no, desc)
        else:
            print("Invalid type.")
            return

        self.create_lot(lot)
        print(f"\nLot #{next_no} created.")

    def _view_lots_by_date(self):
        print("\n--- View Lots for a Date ---")
        date_str = input("Enter auction date (YYYY-MM-DD): ").strip()

        if not self._lots:
            print("No lots in the system.")
            return

        # set of lot numbers sold on this date
        lots_sold = {s.get_lot_no() for s in self._sales if s.get_date() == date_str}

        print(f"\nAll lots for auction date {date_str}:")
        print("-" * 60)
        for lot in self._lots:
            status = "[SOLD]     " if lot.get_lot_number() in lots_sold else "[AVAILABLE]"
            print(f"{status} {lot.display()}")

    def _record_sale(self):
        print("\n--- Record a Sale ---")
        date_str = input("Auction date (YYYY-MM-DD): ").strip()
        try:
            site_no  = int(input("Site No: "))
            lot_no   = int(input("Lot No: "))
            buyer_no = int(input("Buyer No: "))
            amount   = float(input("Sale Amount (€): "))
        except ValueError:
            print("Invalid input.")
            return

        lot   = self.find_lot(lot_no)
        buyer = self.find_buyer(buyer_no)

        if not lot:
            print("Lot not found.")
            return
        if not buyer:
            print("Buyer not found.")
            return

        # Check lot isn't already sold on this date
        for s in self._sales:
            if s.get_lot_no() == lot_no and s.get_date() == date_str:
                print("That lot is already sold on this date.")
                return

        # Snapshot current rates at time of sale
        sale = Sale(site_no, date_str, lot_no, buyer_no, amount,
                    Sale.COMMISSION_RATE, Sale.VAT_RATE)
        self.record_sale(sale)
        print(f"\nSale recorded. {sale.display(buyer.has_vat())}")

    def _modify_lot(self):
        print("\n--- Modify a Lot ---")
        try:
            lot_no = int(input("Lot No to modify: "))
        except ValueError:
            print("Invalid input.")
            return
        lot = self.find_lot(lot_no)
        if not lot:
            print("Lot not found.")
            return
        print(f"Current: {lot.display()}")

        if isinstance(lot, Vehicle):
            reg   = input(f"Registration [{lot.get_registration()}]: ").strip()
            make  = input(f"Make [{lot.get_make()}]: ").strip()
            model = input(f"Model [{lot.get_model()}]: ").strip()
            year  = input(f"Year [{lot.get_year()}]: ").strip()
            hours = input(f"Hours Used [{lot.get_hours_used()}]: ").strip()
            if reg:   lot.set_registration(reg)
            if make:  lot.set_make(make)
            if model: lot.set_model(model)
            if year:  lot.set_year(year)
            if hours: lot.set_hours_used(hours)
        else:
            desc = input(f"Description [{lot.get_description()}]: ").strip()
            if desc: lot.set_description(desc)

        print("Lot updated.")

    def _delete_lot(self):
        print("\n--- Delete a Lot ---")
        try:
            lot_no = int(input("Lot No. to delete: "))
        except ValueError:
            print("Invalid input.")
            return
        lot = self.find_lot(lot_no)
        if not lot:
            print("Lot not found.")
            return
        self._lots.remove(lot)
        print(f"Lot #{lot_no} deleted.")

    def _change_buyer_details(self):
        print("\n--- Change Buyer Details ---")
        try:
            buyer_no = int(input("Buyer No: "))
        except ValueError:
            print("Invalid input.")
            return
        buyer = self.find_buyer(buyer_no)
        if not buyer:
            print("Buyer not found.")
            return
        print(f"Current: {buyer.display()}")
        name    = input(f"Name [{buyer.get_name()}]: ").strip()
        phone   = input(f"Phone [{buyer.get_phone()}]: ").strip()
        bank    = input(f"Bank Account [{buyer.get_bank_account()}]: ").strip()
        address = input(f"Address [{buyer.get_address()}]: ").strip()
        email   = input(f"Email [{buyer.get_email()}]: ").strip()
        vat     = input(f"VAT Number [{buyer.get_vat_number()}]: ").strip()
        if name:    buyer.set_name(name)
        if phone:   buyer.set_phone(phone)
        if bank:    buyer.set_bank_account(bank)
        if address: buyer.set_address(address)
        if email:   buyer.set_email(email)
        if vat:     buyer.set_vat_number(vat)
        print("Buyer updated.")

    def _delete_buyer(self):
        print("\n--- Remove a Buyer ---")
        try:
            buyer_no = int(input("Buyer No: "))
        except ValueError:
            print("Invalid input.")
            return
        buyer = self.find_buyer(buyer_no)
        if not buyer:
            print("Buyer not found.")
            return
        # only remove if no purchases
        has_purchases = False

        for s in self._sales:
            if s.get_buyer_no() == buyer_no:
                has_purchases = True
                break
            
        if has_purchases:
            print("Cannot remove buyer - they have purchases on record.")
            return
        self._buyers.remove(buyer)
        print(f"Buyer #{buyer_no} removed.")

    def _buyer_invoice(self):
        #Show all unpaid lots for a buyer on a given date, with commission and VAT totals.
        print("\n--- Buyer Invoice ---")
        try:
            buyer_no = int(input("Buyer No: "))
        except ValueError:
            print("Invalid.")
            return
        date_str = input("Auction date (YYYY-MM-DD): ").strip()

        buyer = self.find_buyer(buyer_no)
        if not buyer:
            print("Buyer not found.")
            return

        unpaid = []

        for s in self._sales:
            if s.get_buyer_no() == buyer_no:
                if s.get_date() == date_str:
                    if not s.is_paid():
                        unpaid.append(s)

        if not unpaid:
            print("No unpaid lots found for that buyer on that date.")
            return

        print(f"\n{'='*60}")
        print(f"  INVOICE - {buyer.get_name()} (Buyer #{buyer_no})")
        print(f"  Date: {date_str}")
        print(f"{'='*60}")
        grand_total = 0
        for s in unpaid:
            lot = self.find_lot(s.get_lot_no())
            desc = lot.display() if lot else f"Lot #{s.get_lot_no()}"
            print(f"\n  {desc}")
            print(f"  Sale Price:  €{s.get_amount():.2f}")
            print(f"  Commission:    €{s.get_commission():.2f}")
            vat = s.get_vat(buyer.has_vat())
            print(f"  VAT:           €{vat:.2f}" +
                  (" (exempt)" if buyer.has_vat() else ""))
            total = s.get_total(buyer.has_vat())
            print(f"  Line total:    €{total:.2f}")
            grand_total += total

        print(f"\n{'='*60}")
        print(f"  TOTAL DUE: €{grand_total:.2f}")
        print(f"{'='*60}\n")

    def _seller_invoice(self):
        "Self-billing invoice for a seller - all lots sold and amounts due to them."
        print("\n--- Seller Invoice ---")
        try:
            seller_no = int(input("Seller No: "))
        except ValueError:
            print("Invalid.")
            return

        seller = self.find_seller(seller_no)
        if not seller:
            print("Seller not found.")
            return

        seller_lots = {l.get_lot_number() for l in self._lots
                       if l.get_seller_no() == seller_no}
        sold = [s for s in self._sales if s.get_lot_no() in seller_lots]

        if not sold:
            print("No sold lots found for this seller.")
            return

        print(f"\n{'='*60}")
        print(f"  SELLER INVOICE - {seller.get_name()} (Seller #{seller_no})")
        print(f"{'='*60}")
        grand = 0
        for s in sold:
            lot = self.find_lot(s.get_lot_no())
            desc = lot.display() if lot else f"Lot #{s.get_lot_no()}"
            due = s.get_amount() - s.get_commission()
            print(f"\n  {desc}")
            print(f"  Sale Price:  €{s.get_amount():.2f}")
            print(f"  Commission:   -€{s.get_commission():.2f}")
            print(f"  Amount due:    €{due:.2f}")
            grand += due
        print(f"\n{'='*60}")
        print(f"  TOTAL DUE TO SELLER: €{grand:.2f}")
        print(f"{'='*60}\n")

    def _accept_payment(self):
        #Accept payment from a buyer; amount must match what's owed.
        print("\n--- Accept Payment ---")
        try:
            buyer_no = int(input("Buyer No: "))
        except ValueError:
            print("Invalid.")
            return
        date_str = input("Auction date (YYYY-MM-DD): ").strip()

        buyer = self.find_buyer(buyer_no)
        if not buyer:
            print("Buyer not found.")
            return

        unpaid = []

        for s in self._sales:
            if s.get_buyer_no() == buyer_no:
                if s.get_date() == date_str:
                    if not s.is_paid():
                        unpaid.append(s)

        if not unpaid:
            print("No unpaid lots for that buyer on that date.")
            return

        total_due = sum(s.get_total(buyer.has_vat()) for s in unpaid)
        print(f"Total due: €{total_due:.2f}")

        try:
            amount_paid = float(input("Amount tendered: €"))
        except ValueError:
            print("Invalid amount.")
            return

        if round(amount_paid, 2) != round(total_due, 2):
            print(f"Payment rejected - amount must be exactly €{total_due:.2f}.")
            return

        site_no = unpaid[0].get_site_no()
        payment = Payment(date_str, site_no, buyer_no, amount_paid)
        self.process_payment(payment)

        for s in unpaid:
            s.set_paid(True)

        print(f"Payment of €{amount_paid:.2f} accepted. Lots marked as paid.")

    def _change_rates(self):
        print("\n--- Change Commission / VAT Rates ---")
        print(f"Current Commission Rate: {Sale.COMMISSION_RATE*100:.1f}%")
        print(f"Current VAT Rate:        {Sale.VAT_RATE*100:.1f}%")
        try:
            c = input("New Commission % (leave blank to keep): ").strip()
            v = input("New VAT % (leave blank to keep): ").strip()
            if c: 
                Sale.COMMISSION_RATE = float(c) / 100
            if v: 
                Sale.VAT_RATE        = float(v) / 100
        except ValueError:
            print("Invalid rate.")
            return
        print("Rates updated (only affects future sales).")

    # Main loop

    def start_auction(self):
        self.load_data()
        print("\n=== Welcome to the Machinery Auction System ===")

        while True:
            print("""
                    --- Main Menu ---
                    1.  Register a Buyer
                    2.  Register a Seller
                    3.  Register an Employee
                    4.  Create a Lot
                    5.  View Lots for a Date
                    6.  Record a Sale
                    7.  Modify a Lot
                    8.  Delete a Lot
                    9.  Change Buyer Details
                    10.  Remove a Buyer (if no purchases)
                    11.  Buyer Invoice (unpaid lots)
                    12.  Seller Invoice
                    13.  Accept Payment from Buyer
                    14.  Change Commission / VAT Rates
                    0.  Save & Exit
                    """)
            choice = input("Choice: ").strip()

            match choice:
                case '1':  self._register_buyer()
                case '2':  self._register_seller()
                case '3':  self._register_employee()
                case '4':  self._create_lot()
                case '5':  self._view_lots_by_date()
                case '6':  self._record_sale()
                case '7':  self._modify_lot()
                case '8':  self._delete_lot()
                case '9':  self._change_buyer_details()
                case '10': self._delete_buyer()
                case '11': self._buyer_invoice()
                case '12': self._seller_invoice()
                case '13': self._accept_payment()
                case '14': self._change_rates()
                case '0':
                    self.save_data()
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice - please enter a number from the menu.")


if __name__ == "__main__":
    system = MachineryAuctionSystem()
    system.start_auction()