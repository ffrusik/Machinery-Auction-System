class Sale:

    COMMISSION_RATE = 0.05   # 5%
    VAT_RATE = 0.20          # 20%

    def __init__(self, site_no, date, lot_no, buyer_no, amount,
                 commission_rate=None, vat_rate=None, paid=False):
        self._site_no = site_no
        self._date = date
        self._lot_no = lot_no
        self._buyer_no = buyer_no
        self._amount = amount
        # Snapshot the rates at time of sale so changing rates later won't affect this sale
        self._commission_rate = commission_rate if commission_rate is not None else Sale.COMMISSION_RATE
        self._vat_rate = vat_rate if vat_rate is not None else Sale.VAT_RATE
        self._paid = paid

    # Calculated fields
    def get_commission(self):
        return round(self._amount * self._commission_rate, 2)

    def get_vat(self, buyer_has_vat=False):
        #VAT only applies to buyers without a VAT number.
        if buyer_has_vat:
            return 0.0
        return round(self._amount * self._vat_rate, 2)

    def get_total(self, buyer_has_vat=False):
        return round(self._amount + self.get_commission() + self.get_vat(buyer_has_vat), 2)

    # Getters
    def get_site_no(self):    
        return self._site_no
    def get_date(self):       
        return self._date
    def get_lot_no(self):     
        return self._lot_no
    def get_buyer_no(self):   
        return self._buyer_no
    def get_amount(self):     
        return self._amount
    def is_paid(self):        
        return self._paid

    # Setters
    def set_paid(self, paid): 
        self._paid = paid
    def set_amount(self, a):  
        self._amount = a

    def display(self, buyer_has_vat=False):
        return (f"Lot #{self._lot_no} | Date: {self._date} | "
                f"Amount: €{self._amount:.2f} | "
                f"Commission: €{self.get_commission():.2f} | "
                f"VAT: €{self.get_vat(buyer_has_vat):.2f} | "
                f"Total: €{self.get_total(buyer_has_vat):.2f} | "
                f"Paid: {'Yes' if self._paid else 'No'}")