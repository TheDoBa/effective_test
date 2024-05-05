import re


class Transaction:
    """
    Инициализирует новую транзакцию.

    :param date: дата транзакции(строка)
    :param category: категория транзакции(строка)
    :param amount: сумма транзакции(число)
    :param description: описание транзакции(строка)
    """

    def __init__(
        self,
            date: str,
            category: str,
            amount: float,
            description: str
    ):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


class TransactionManager:
    """
    Инициализирует менеджер транзакций.

    :param filename: имя файла для сохранения и загрузки данных(строка)
    """

    def __init__(self, filename: str = "data.txt"):
        self.filename = filename
        self.transactions = self.load_transactions()

    def load_transactions(self) -> list:
        """
        Загружает список транзакций из файла.

        :return: список транзакций (список объектов Transaction)
        """
        transactions = []
        try:
            lines = self.read_file()
            transactions = self.parse_transactions(lines)
        except FileNotFoundError:
            print(
                f"Файл {self.filename} не найден. Новый список будет создан."
            )
            self.create_file()
        return transactions

    def save_transactions(self) -> None:
        """
        Сохраняет список транзакций в файл.
        """
        try:
            transactions_data = self.prepare_transactions_data()
            self.write_file(transactions_data)
            print(f"Данные успешно сохранены в {self.filename}.")
        except Exception as e:
            print(f"Произошла ошибка при сохранении данных: {e}")

    def read_file(self) -> list:
        """
        Читает данные из файла.

        :return: данные из файла (список строк)
        """
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.readlines()

    def parse_transactions(self, lines: list) -> list:
        """
        Парсит строки из фала в объекты Transaction.

        :param lines: строки из файла (список str)
        :return: список транзакций (список объектов Transaction)
        """
        transactions = []
        transaction_data = []
        for line in lines:
            if line.strip():
                transaction_data.append(line.strip())
            else:
                transaction = self.create_transaction(transaction_data)
                transactions.append(transaction)
                transaction_data = []
        if transaction_data:
            transaction = self.create_transaction(transaction_data)
            transactions.append(transaction)
        return transactions

    def create_transaction(self, transaction_data: list) -> Transaction:
        """
        Создает объект Transaction из предоставленных данных.

        :param transaction_data: данные для создания транзакции (список str)
        :return: объект Transaction
        """
        date = transaction_data[0].split(": ")[1]
        category = transaction_data[1].split(": ")[1]
        amount = float(transaction_data[2].split(": ")[1])
        description = transaction_data[3].split(": ")[1]
        return Transaction(date, category, amount, description)

    def create_file(self) -> None:
        """
        Создает новый файл.
        """
        with open(self.filename, "w", encoding="utf-8"):
            pass

    def prepare_transactions_data(self) -> list:
        """
        Подготовка данных для записи в файл.

        :return: данные для записи (список str)
        """
        transactions_data = []
        for transaction in self.transactions:
            transactions_data.append(f"Дата: {transaction.date}\n")
            transactions_data.append(f"Категория: {transaction.category}\n")
            transactions_data.append(f"Сумма: {transaction.amount}\n")
            transactions_data.append(
                f"Описание: {transaction.description}\n\n")
        return transactions_data

    def write_file(self, transactions_data: list) -> None:
        """
        Записывает данные в файл.

        :param transactions_data: данные для записи (список str)
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            for data in transactions_data:
                file.write(data)

    def show_balance(self):
        """
        Показывает баланс и доходы и расходы.
        """
        income = 0
        expenses = 0
        for transaction in self.transactions:
            if transaction.category.lower() == "доход":
                income += transaction.amount
            elif transaction.category.lower() == "расход":
                expenses += transaction.amount
        balance = income - expenses

        print(f"Баланс: {balance}")
        print(f"Доходы: {income}")
        print(f"Расходы: {expenses}")

    def add_transaction(self):
        """
        Добавляет новую транзакцию в список.
        """
        while True:
            try:
                print("Cntrl+C. Для выхода в главное меню.")
                date = self.validate_date(
                    input("Введите дату транзакции (гггг-мм-дд): "))
                category = self.validate_category(
                    input("Категория (Доход или Расход): "))
                amount = self.validate_amount(input("Сумма: "))
                description = input("Описание транзакции: ")

                new_transaction = Transaction(
                    date, category, amount, description
                )
                self.transactions.append(new_transaction)
                print("Запись успешно добавлена.")
                break
            except ValueError:
                print("Некорректные данные. Попробуйте ещё раз.")
            except KeyboardInterrupt:
                print("Выход в главное меню.")
                break

    def change_transaction(self):
        """
        Редактирует существующую транзакцию в списке.
        """
        while True:
            try:
                print("Список транзакций:")
                print("Cntrl+C. Для выхода в главное меню.")
                for index, transaction in enumerate(
                    self.transactions,
                    start=1
                ):
                    print(
                        f"{index}. Дата: {transaction.date}, "
                        f"Категория: {transaction.category}, "
                        f"Сумма: {transaction.amount}, "
                        f"Описание: {transaction.description}"
                    )
                index = int(input("Выберите транзакцию для изменения: ")) - 1

                if index < 0 or index >= len(self.transactions):
                    print("Некорректный индекс. Попробуйте ещё раз.")
                    continue
                transaction = self.transactions[index]

                print("Текущие данные:")
                print(
                    f"Дата: {transaction.date}, "
                    f"Категория: {transaction.category}, "
                    f"Сумма: {transaction.amount}, "
                    f"Описание: {transaction.description}"
                )

                date = self.validate_date(
                    input("Введите дату транзакции (гггг-мм-дд): "))
                category = self.validate_category(
                    input("Категория (Доход или Расход): "))
                amount = self.validate_amount(input("Сумма: "))
                description = input("Описание транзакции: ")

                transaction.date = date
                transaction.category = category
                transaction.amount = amount
                transaction.description = description

                print("Запись успешно изменена.")
                break
            except (ValueError, IndexError):
                print("Некорректные данные. Попробуйте ещё раз.")
            except KeyboardInterrupt:
                print("Выход в главное меню.")
                break

    def search_transactions(self):
        """
        Поиск транзакции по заданному критерию.
        """
        while True:
            try:
                print("Выберите критерий поиска:")
                print("1. По категории")
                print("2. По дате")
                print("3. По сумме")
                print("Cntrl+C. Для выхода в главное меню.")
                choice = int(input("Выберите действие: "))

                if choice == 1:
                    category = self.validate_category(
                        input("Категория для поиска (Доход или Расход): "))
                    filter_transactions = [
                        transaction
                        for transaction in self.transactions
                        if transaction.category.lower() == category.lower()
                    ]
                elif choice == 2:
                    date = self.validate_date(
                        input("Дата для поиска (гггг-мм-дд): "))
                    filter_transactions = [
                        transaction
                        for transaction in self.transactions
                        if transaction.date == date
                    ]
                elif choice == 3:
                    amount = self.validate_amount(input("Сумма для поиска: "))
                    filter_transactions = [
                        transaction
                        for transaction in self.transactions
                        if transaction.amount == amount
                    ]
                else:
                    print("Некорректный ввод. Попробуйте ещё раз.")
                    continue

                if filter_transactions:
                    print("Результаты поиска:")
                    for transaction in filter_transactions:
                        print(
                            f"Дата: {transaction.date}, "
                            f"Категория: {transaction.category}, "
                            f"Сумма: {transaction.amount}, "
                            f"Описание: {transaction.description}"
                        )
                else:
                    print("Ничего не найдено.")
                break
            except (ValueError, IndexError):
                print("Некорректные данные. Попробуйте ещё раз.")
            except KeyboardInterrupt:
                print("Выход в главное меню.")
                break

    @staticmethod
    def validate_date(date):
        """
        Проверяет корректность формата даты.

        :param date: дата в формате "гггг-мм-дд"(строка)
        :return: дата в формате "гггг-мм-дд"(строка)
        :raise ValueError: если формат даты некорректен
        """
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            raise ValueError(
                "Некорректный формат даты. Используйте формат гггг-мм-дд.")
        return date

    @staticmethod
    def validate_category(category):
        """
        Проверяет корректность категории.

        :param category: категория (доход или расход)(строка)
        :return: категория (доход или расход)(строка)
        :raise ValueError: если категория некорректна
        """
        category = category.lower()
        if category not in ["доход", "расход"]:
            raise ValueError("Категория должна быть 'Доход' или 'Расход'.")
        return category

    @staticmethod
    def validate_amount(amount):
        """
        Проверяет корректность суммы.

        :param amount: сумма (число)
        :return: сумма (число)
        :raise ValueError: если сумма некорректна
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Некорректное значение суммы.")
        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля.")
        return amount

    def run(self):
        """
        Запуск меню.
        """
        while True:
            print("Меню:")
            print("-----------------")
            print("1. Показать баланс")
            print("2. Добавить запись")
            print("3. Редактировать запись")
            print("4. Поиск записи")
            print("5. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                self.show_balance()
            elif choice == "2":
                self.add_transaction()
            elif choice == "3":
                self.change_transaction()
            elif choice == "4":
                self.search_transactions()
            elif choice == "5":
                self.save_transactions()
                print("До свидания!")
                break
            else:
                print("Некорректный ввод. Попробуйте ещё раз.")


if __name__ == "__main__":
    manager = TransactionManager()
    manager.run()
