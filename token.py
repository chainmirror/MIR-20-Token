class MIR20:
    DECIMALS = 6
    TOTAL_UNITS = 1_000_000_000 * (10 ** DECIMALS)

    def __init__(self, deployer):
        self.name = "MIR-20"
        self.symbol = "MIR"
        self.decimals = self.DECIMALS

        # fixed supply
        self._total_supply = self.TOTAL_UNITS

        # assign entire supply to deployer
        self._balances = {deployer: self.TOTAL_UNITS}

    # ---------- Views ----------
    def totalSupply(self):
        return self._total_supply  # in smallest units

    def balanceOf(self, account):
        return self._balances.get(account, 0)

    # ---------- Internal helpers ----------
    def _require(self, cond, msg):
        if not cond:
            raise Exception(msg)

    def _add_balance(self, who, amount):
        self._balances[who] = self._balances.get(who, 0) + amount

    def _sub_balance(self, who, amount):
        bal = self.balanceOf(who)
        self._require(bal >= amount, "Insufficient balance")
        self._balances[who] = bal - amount
        if self._balances[who] == 0:
            # optional cleanup
            self._balances.pop(who, None)

    # ---------- Actions ----------
    def transfer(self, sender, recipient, amount_units):
        amount_units = int(amount_units)
        self._require(amount_units > 0, "Amount must be > 0")
        self._require(sender != recipient, "Sender == recipient")
        self._require(recipient is not None, "Recipient required")

        self._sub_balance(sender, amount_units)
        self._add_balance(recipient, amount_units)
        return True

    def transferMany(self, sender, pairs):
        total = sum(int(a) for _, a in pairs)
        self._require(total > 0, "Total must be > 0")
        self._sub_balance(sender, total)
        for rcpt, amt in pairs:
            self._add_balance(rcpt, int(amt))
        return True

    # ---------- Conversion helpers ----------
    @staticmethod
    def to_units(amount_token):
        return int(round(float(amount_token) * (10 ** MIR20.DECIMALS)))

    @staticmethod
    def to_token(amount_units):
        return amount_units / float(10 ** MIR20.DECIMALS)
