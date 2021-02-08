from db_validation import *


class BankApp:

    @staticmethod
    def main_view():
        actions = {
            "register": 1,
            "login": 2,
            "exit": 3
        }
        return actions

    @staticmethod
    def menu_view(user_id):
        while True:
            msg = int(input('\nWitaj użytkowniku!\n'
                            '1) Stan konta\n'
                            '2) Wpłać pieniądze\n'
                            '3) Wypłać pieniądze\n'
                            '-------------------\n'
                            '4) Wpłać w innej walucie\n'
                            '5) Wypłać w innej walucie\n'
                            '-------------------\n'
                            '6) Historia transakcji\n'
                            '7) Logout\n'))
            actions = {
                "acc_balance": 1,
                "deposit_cash": 2,
                "withdrawal_cash": 3,
                "deposit_in_diff_currency": 4,
                "withdrawal_in_diff_currency": 5,
                "last_transactions": 6
            }

            if msg == actions["acc_balance"]:
                acc = AccountCashManagement(cash_deposit=0, cash_withdrawal=0, user_id=user_id)
                if acc.acc_balance() is None:
                    print('Nie ma środków na koncie')
                else:
                    print(f"Aktualnie masz na koncie: {round(acc.acc_balance(), 2)} zł.\n")

            elif msg == actions["deposit_cash"]:
                amount = float(input("\nIle chcesz wpłacić pieniędzy?: "))
                acc = AccountCashManagement(cash_deposit=amount, cash_withdrawal=0, user_id=user_id)
                acc.deposit_cash()
                print(f"Wpłacono: {amount} PLN\n")

            elif msg == actions["withdrawal_cash"]:
                amount = float(input("\nIle chcesz wypłacić pieniędzy?: "))
                acc = AccountCashManagement(cash_deposit=0, cash_withdrawal=amount, user_id=user_id)
                acc.withdrawal_cash()
                print(f"Wypłacono: {amount} PLN\n")

            elif msg == actions['deposit_in_diff_currency']:
                currency = AccountCashManagement.change_currency()
                amount = float(input("\nIle chcesz wpłacić pieniędzy?: "))
                acc = AccountCashManagement(cash_deposit=amount*currency[0], cash_withdrawal=0, user_id=user_id)
                acc.deposit_cash()
                print(f"Wpłacono: {round(amount * currency[0], 2)} PLN\n")

            elif msg == actions['withdrawal_in_diff_currency']:
                currency = AccountCashManagement.change_currency()
                amount = float(input("\nIle chcesz wypłacić pieniędzy?: "))
                acc = AccountCashManagement(cash_deposit=0, cash_withdrawal=amount, user_id=user_id)
                acc.withdrawal_cash()
                print(f"Wypłacono: {round(amount / currency[0], 2)} {currency[1]}\n")

            elif msg == actions['last_transactions']:
                AccountCashManagement.last_transactions(user_id=user_id)
            else:
                return False

    def login_view(self):
        bank_id = int(input("Nr. Weryfikacyjny: "))
        password = input('Hasło: ')

        form = Login(bank_id, password)

        if form.password_match() and form.bank_id_match():
            self.menu_view(bank_id)
        else:
            return False

    @staticmethod
    def register_model():
        form = RegisterUser(name=input('Imię: '), last_name=input('Nazwisko: '),
                            age=int(input('Wiek: ')), gender=input('Płeć: '),
                            pesel=input('PESEL: '), birth_date=input('Data urodzenia: '),
                            phone_number=input('Numer telefonu: '), password=input('Hasło: '))

        # Weryfikacja użytkownika.
        form.full_name_validation()
        form.hash_password()
        form.birth_date_validation()
        form.age_validation()
        form.sex_validation()

        # form.basic_pesel_validation()
        # form.control_number_validation()

        # Jeśli użytkownik przejdzie weryfikacje zostaje dodany do dazy danych.
        form.add_to_database()
        form.display_user_bank_id(form.pesel)


if __name__ == '__main__':

    while True:
        message = int(input('Opcje:\n'
                            '1) Rejstreacja\n'
                            '2) Login\n'
                            '3) Exit\n'))
        choice = BankApp.main_view()
        if message == choice['register']:

            try:
                BankApp.register_model()
                print('Restracja się powiodła.')
                break
            except ValueError:
                print('Odświeżyć stronę?(t/n)')
                try_again = input('Wystąpił błąd podczas rejstracji. ')

                if try_again == 't':
                    continue
                else:
                    break

        elif message == choice['login']:
            BankApp().login_view()

        elif message == choice['exit']:
            print('Do zobaczenia!')
            break

        else:
            print('Nie ma takiej opcji.')
