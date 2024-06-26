# Проект "Менеджер транзакций"

Работа над скриптом «Менеджер транзакций».

Этот скрипт представляет собой простой менеджер транзакций, который позволяет пользователю добавлять, редактировать и искать транзакции, а также просматривать текущий баланс, доходы и расходы.

## Технический стек:
- [Python 3.9.10](https://docs.python.org/release/3.9.10/)

## Запуск проекта:
1. Скачайте файл effective_test.py.
2. Установите Python 3.x, если он еще не установлен.
3. Запустите скрипт, выполнив команду python effective_test.py в терминале.

## Использование
1. Показать баланс - отображает текущий баланс, доходы и расходы.
2. Добавить запись - добавляет новую транзакцию.
3. Редактировать запись - редактирует существующую транзакцию.
4. Поиск записи - ищет транзакции по заданному критерию.
5. Выход - выходит из программы.

Введите номер опции, которую вы хотите выбрать, и нажмите Enter.

Для добавления, редактирования и поиска транзакций вам потребуется ввести дату, категорию (доход или расход), сумму и описание транзакции.

## Файл данных
По умолчанию скрипт использует файл data.txt для хранения транзакций. Вы можете изменить имя файла, изменив значение параметра filename при создании экземпляра класса TransactionManager.

Формат файла: 

```
Дата: 2023-10-05
Категория: Доход
Сумма: 100.0
Описание: Зарплата

Дата:  2020-12-05
Категория: Расход
Сумма: 50.0
Описание:  Еда

Дата: 2023-12-15
Категория: Доход
Сумма: 100.0
Описание: Премия
```

Каждая транзакция занимает четыре строки, разделенные пустой строкой. Дата, категория, сумма и описание транзакции разделены двоеточием и пробелом.


[GitHub](https://github.com/TheDoBa) | Разработчик - Vladimir Avizhen
