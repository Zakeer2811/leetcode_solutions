class Bank:

    def __init__(self, balance: List[int]):
        # Store balances as 1-indexed for easy access
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Check if accounts exist
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        # Check if enough balance
        if self.balance[account1 - 1] < money:
            return False
        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # Check if account exists
        if not (1 <= account <= self.n):
            return False
        # Deposit money
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Check if account exists
        if not (1 <= account <= self.n):
            return False
        # Check if enough balance
        if self.balance[account - 1] < money:
            return False
        # Withdraw money
        self.balance[account - 1] -= money
        return True
