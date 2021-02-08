from db_validation import *


class CreateSqlTables:

    @staticmethod
    def primary_user_table():
        try:
            SqlConnection().create_connection()
            SqlConnection().create_table_for_user()
            SqlConnection().create_table_for_user_account()
        except Error:
            print(Error)
            raise Error("Baza danych jest stworzona.")


if __name__ == '__main__':
    CreateSqlTables().primary_user_table()
