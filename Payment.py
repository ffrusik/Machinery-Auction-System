class Payment:
    def __init__(self, auction_date, site_number, buyer_number, amount_paid):
        self._auction_date = auction_date
        self._site_number = site_number
        self._buyer_number = buyer_number
        self._amount_paid = amount_paid

    def get_auction_date(self):
        return self._auction_date

    def get_site_number(self):
        return self._site_number

    def get_buyer_number(self):
        return self._buyer_number

    def get_amount_paid(self):
        return self._amount_paid