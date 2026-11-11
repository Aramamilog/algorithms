from abc import ABC, abstractmethod
from typing import List


class Hardware(ABC):
    @abstractmethod
    def get_bills_counts(self) -> List[int]:
        """
        Возвращает количество купюр по номиналам:
        [50, 100, 500, 1000, 5000].

        Метод работает медленно и создаёт шум.
        """
        pass

    @abstractmethod
    def give_bills(self, bills_counts: List[int]) -> None:
        """Загружает указанные купюры в бокс выдачи."""
        pass


class MyATM:

    _nominals = [50, 100, 500, 1000, 5000]

    def __init__(self, hardware: Hardware):
        self.hardware = hardware

    def withdraw(self, amount: int) -> bool:
        # краевые случаи
        if amount <= 0 or amount % self._nominals[0] != 0:
            return False

        # копия актуального кол-ва купюр
        nominals_count = self.hardware.get_bills_counts()
        # заготовка под выдачу
        # 10550 -> [1, 0, 1, 0, 2]
        to_give_bills = [0] * len(self._nominals)

        for i in range(len(self._nominals) - 1, -1, -1):
            to_give = min(amount // self._nominals[i], nominals_count[i])
            to_give_bills[i] = to_give
            amount -= to_give * self._nominals[i]

        if not amount:
            self.hardware.give_bills(to_give_bills)

        return amount == 0

        # проверка amount == 0 + ловушка на переусложение guard expression


class MockHardware(Hardware):
    """Тестовая реализация интерфейса Hardware."""

    def __init__(self, bills_counts: List[int]):
        self.bills_counts = bills_counts.copy()
        self.given: List[List[int]] = []

    def get_bills_counts(self) -> List[int]:
        return self.bills_counts.copy()

    def give_bills(self, bills_counts: List[int]) -> None:
        assert len(bills_counts) == len(self.bills_counts)
        assert all(
            0 <= count <= available
            for count, available in zip(bills_counts, self.bills_counts)
        )

        for i, count in enumerate(bills_counts):
            self.bills_counts[i] -= count

        self.given.append(bills_counts.copy())


def test_atm():
    hardware = MockHardware([1, 5, 0, 1, 5])
    atm = MyATM(hardware)

    # Успешная выдача.
    assert atm.withdraw(6500) is True
    assert hardware.given == [[0, 5, 0, 1, 1]]
    assert hardware.bills_counts == [1, 0, 0, 0, 4]

    # Невозможно собрать сумму оставшимися купюрами.
    assert atm.withdraw(100) is False
    assert hardware.bills_counts == [1, 0, 0, 0, 4]

    # Некорректные суммы.
    for amount in [0, -50, 75]:
        assert atm.withdraw(amount) is False

    # При отказах новых выдач не было.
    assert hardware.given == [[0, 5, 0, 1, 1]]

    # Снятие последней купюры и повторная попытка.
    hardware = MockHardware([0, 0, 0, 0, 1])
    atm = MyATM(hardware)
    assert atm.withdraw(5000) is True
    assert atm.withdraw(5000) is False

    print("Все тесты пройдены")


if __name__ == "__main__":
    test_atm()
