import json


expenses = []
incomes = []
balance = 0

def add_expense(category, amount):
    expenses.append({"category": category, "amount": amount})
    global balance
    balance -= amount

def add_income(category, amount):
    incomes.append({"category": category, "amount": amount})
    global balance
    balance += amount

def show_expenses():
    totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount
    for category, total in totals.items():
            print(f'{category}: {total}')

def save_data():
    data = {
        "balance": balance,
        "expenses": expenses,
        "incomes": incomes
    }
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data():
    global balance, expenses, incomes
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            balance = data['balance']
            expenses = data['expenses']
            incomes = data['incomes']
    except FileNotFoundError:
        pass

load_data()
while True:
    print('===MoneyBase===')
    print('1.Добвить расход с категорией')
    print("2.Добвить доход")
    print('3.Показать баланс')
    print('4.Показать расходы по категориям')
    print('5.Сохранить баланс')
    print('6.Выйти')
    choice = input("Выбери действие: ")
    if choice == '1':
        category = input("Категория (еда/транспорт/учёба): ")
        amount = int(input("Сумма: "))
        add_expense(category, amount)
        save_data()

    elif choice == '2':
        category = input("Источник дохода (зарплата/фриланс/подарок): ")
        amount = int(input("Сумма: "))
        add_income(category, amount)
        save_data()

    elif choice == '3':
        print(f'Текущий баланс: {balance}')
    elif choice == '4':
        print('Расходы по категориям:')
        show_expenses()
    elif choice == '5':
        print('Сохранено')
    elif choice == '6':
        save_data()
        break
    else:
        print('Невозможно совершить действие')