from abc import ABC, abstractmethod

class FundTransfer(ABC):
    def __init__(self, account_number: int, balance: float):
        self.account_number = account_number
        self.balance = balance

    def validate(self, amount: float) -> bool:
        # check account number is 10 digits
        if len(str(self.account_number)) != 10:
            return False
        
        # check amount is non-negative and less than or equal to balance
        if amount < 0 or amount > self.balance:
            return False
        
        return True

    @abstractmethod
    def transfer(self, amount: float):
        pass


class NEFTransfer(FundTransfer):
    def transfer(self, amount: float):
        if self.validate(amount):
            self.balance -= amount
            print(f"NEF Transfer successful. Amount transferred: {amount}")
            print(f"Remaining balance: {self.balance}")
        else:
            print("NEF Transfer failed. Validation error.")
