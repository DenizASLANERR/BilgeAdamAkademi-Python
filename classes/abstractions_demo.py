from abc import ABC, abstractmethod  # Abstract Base Class


class CreditCard:
    def __init__(self):
        self.bank = ""
        self.card_limit = 0
        self.card_type = ""
        self.installment = False


class CreditCardBuilder(ABC):
    def __init__(self):
        self._credit_card = CreditCard()

    @abstractmethod
    def bank_name_func(self):
        pass

    @abstractmethod
    def card_limit_func(self):
        pass

    @abstractmethod
    def card_type_func(self):
        pass

    @abstractmethod
    def installment_func(self):
        pass


class Maximum(CreditCardBuilder):
    def __init__(self):
        super().__init__()

    def bank_name_func(self):
        self._credit_card.bank = "Is Bankasi"
        return self._credit_card.bank

    def card_limit_func(self):
        self._credit_card.card_limit = 10_000

    def card_type_func(self):
        self._credit_card.card_type = "Visa"
        return self._credit_card.card_type

    def installment_func(self):
        self._credit_card.installment = True
        return self._credit_card.installment


class Bonus(CreditCardBuilder):
    def __init__(self):
        super().__init__()

    def bank_name_func(self):
        self._credit_card.bank = "Garanti Bankasi"
        return self._credit_card.bank

    def card_limit_func(self):
        self._credit_card.card_limit = 20_000

    def card_type_func(self):
        self._credit_card.card_type = "Master Card"
        return self._credit_card.card_type


maximum1 = Maximum()
maximum1.bank_name_func()
maximum1.card_type_func()
maximum1.card_limit_func()
maximum1.installment_func()


bonus1 = Bonus()

