# Assingment-4

# Create a class Bank with a class variable bank_name.
#  Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.


class Bank:
    bank_name = "Meezan Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder} , Bank: {self.bank_name}")

account1 = Bank("Ibrahim")
account2 = Bank("Saima")
account3 = Bank("Faiza")

account1.display()
account2.display()
account3.display()
        
Bank.change_bank_name("HBL")

account1.display()
account2.display()
account3.display()