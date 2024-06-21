class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limt):
        """Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g., 'John Bowman')
        bank     the name of the bank (e.g., 'California Savings')
        acnt     the acount identifier (e.g., '5391 0375 9387 5309')
        limit    credit limt (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limt
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)"""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def set_limit(self, limit):
        self._limit = limit

    # 问题：调用charge的时候，使用几个参数？
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:    # if charge would exceed limit,
            return False                           # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount


if __name__ == '__main__':
    cc = CreditCard('Yutong', 
                    'Gonghang', 
                    '8888888888888888', 
                    100000)
    print('_bank', cc.get_bank())
    print('_account', cc.get_account())
    print(cc._limit)
    cc.set_limit(1000000)
    print('_limit', cc.get_limit())

    cc.charge(1000)
    print('The current balance', cc.get_balance())

    cc.charge(10000000)
    print('The current balance', cc.get_balance())
    











