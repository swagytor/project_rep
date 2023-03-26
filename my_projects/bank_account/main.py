import bank_account


def main():
    start_balance = round(float(input('Введите ваш начальный остаток: ')), 2)

    savings = bank_account.BankAccount(start_balance)

    week_pay = round(float(input('Введите, сколько вы получили на этой неделе: ')), 2)

    savings.deposit(week_pay)

    print(f'Ваш счёт на этой неделе составляет: {savings.get_balance()}$')

    cash_out = round(float(input('Введите, сколько вы хотите снять средств: ')), 2)

    savings.withdraw(cash_out)

    print(f'Ваш счёт на этой неделе составляет: {savings.get_balance()}$')


if __name__ == '__main__':
    main()
