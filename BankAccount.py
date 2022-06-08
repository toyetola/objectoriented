
class Account:

    def __init__(self):
        #self.accountNumber =
        pass
    _balance = 0.00

    def getAccountNumber(self):
        return 2136688776

    def setter(self, amount, accountNumber):
        validateAccount = self.getAccountNumber()
        if amount > 0 and validateAccount == accountNumber:
            self._balance = self._balance + amount
        return self._balance

    def getBalance(self):
        return self._balance

    def deposit(self, amount, accountNumber):
        return self.setter(amount, accountNumber)

    def withdraw(self, amount, accountNumber):
        validateAccount = self.getAccountNumber()
        if validateAccount != accountNumber:
            return "Please provide the correct account"

        balance = self._balance
        if balance > amount:
            self._balance = self._balance - amount
            return "Take " + str(float(amount)) + " balance is " + str(self._balance)
        return "Not enough balance"


account = Account()
print(account.getAccountNumber())
print(account.getBalance())
print(account.deposit(10000, 2136688776))
print(account.deposit(12000, 2136688776))
print(account.withdraw(12000, 2136688776))
print(account.getBalance())

# Output
# 2136688776
# 0.0
# 10000.0
# 22000.0
# Take 12000.0 balance is 10000.0
# 10000.0



