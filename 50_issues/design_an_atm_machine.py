# https://leetcode.com/problems/design-an-atm-machine/
class ATM:
    _nominals = [20, 50, 100, 200, 500]

    def __init__(self):
        self.bills_counts = [0] * 5

    def deposit(self, banknotesCount: list[int]) -> None:
        for i, n in enumerate(banknotesCount):
            self.bills_counts[i] += n

    def commit(self, to_give_bills: list[int]) -> None:
        for i, count in enumerate(to_give_bills):
            self.bills_counts[i] -= count

    def withdraw(self, amount: int) -> list[int]:
        # prepare banknotes for withdrawal
        to_give_bills = [0] * len(self._nominals)

        # greedily select banknotes from largest to smallest
        for i in range(len(self._nominals) - 1, -1, -1):
            to_give = min(amount // self._nominals[i], self.bills_counts[i])
            to_give_bills[i] = to_give
            amount -= to_give * self._nominals[i]

        # failed withdrawal must not modify ATM state
        if amount != 0:
            return [-1]

        # commit the withdrawal only after success
        self.commit(to_give_bills)

        return to_give_bills


atm = ATM()
# because of k = 5
# time complexity O(1)
# memory complexity O(1)

atm.deposit([0,0,1,2,1])
assert atm.withdraw(600) == [0,0,1,0,1]
atm.deposit([0,1,0,1,1])
assert atm.withdraw(600) == [-1]
assert atm.withdraw(550) == [0,1,0,0,1]
