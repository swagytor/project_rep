class BankAccount:
    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'Вы успешно сняли {amount}$')
        else:
            print('Ошибка: На счёте недостаточно средств!')

    def get_balance(self):
        return self.__balance
