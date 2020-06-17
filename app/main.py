from typing import Union


def foo(x: Union[str, int]) -> Union[int, str]: 
  try: 
    return int(x)
  except ValueError as exc: 
    return x
    
class BankAccount:
    def __init__(self, initial_balance: int = 0) -> None:
        self.balance = initial_balance
    def deposit(self, amount: int) -> None:
        self.balance += amount
    def withdraw(self, amount: int) -> None:
        self.balance -= amount
    def overdrawn(self) -> bool:
        return self.balance < 0

my_account = BankAccount(15)
my_account.withdraw(5)

import itertools
from typing import Iterator

def iter_primes() -> Iterator[int]:
     # An iterator of all numbers between 2 and
     # +infinity
     numbers = itertools.count(2)

     # Generate primes forever
     while True:
         # Get the first number from the iterator
         # (always a prime)
         prime = next(numbers)
         yield prime

         # This code iteratively builds up a chain
         # of filters...
         numbers = filter(prime.__rmod__, numbers)

for p in iter_primes():
    if p > 1000:
        break
    print(foo(p))
    print(BankAccount(p))
