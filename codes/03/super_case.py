def __init__(self, customer, bank, acnt, limit, apr):
    super().__init__(customer, bank, acnt, limit)
    self._apr = apr