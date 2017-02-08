class BankAccount:
    def __init__(self):
        self.balance = 0

    def balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def accumulate_interest(self):
        self.balance = self.balance*1.02
        return self.balance

class ChildrensAccount(BankAccount):
  def __init__(self):
      super().__init__()

  def accumulate_interest(self):
      return self.balance

class OverdraftAccount(BankAccount):
    def __init__(self):
        super().__init__()

    def withdraw(self, amount):
        diff = self.balance - amount
        print(diff)
        if diff < 0:
            self.balance -= 40
            return self.balance
        else:
            self.balance -= amount
            return self.balance

    def accumulate_interest(self):
        if self.balance < 0:
            return self.balance
        else:
            self.balance = self.balance*1.02
            return self.balance



basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
