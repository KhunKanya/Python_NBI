
class BankAccount:
    def __init__(self, initial_balance=0, interest_rate=0.01):
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):   # Används för att sätta in pengar på kontot
        if amount < 0:
            raise ValueError
        self.balance += amount

    def withdraw(self, amount):  # Används för att ta ut pengar från kontot
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def apply_interest(self):    # Används för att beräkna ränta och lägga till den på kontot.
        self.balance += self.balance * self.interest_rate

    def can_pay_bill(self, amount):  #  Det finns tillräckligt med pengar för att betala räkningen.
        return self.balance >= amount

    def get_balance(self):  # Används för att returnera kontosaldot
        return self.balance
