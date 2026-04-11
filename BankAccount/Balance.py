#Start
class Balance:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            self.__balance -= amount
        else:
            print("You don't have enough money to withdraw")
    def get_balance(self):
        return self.__balance