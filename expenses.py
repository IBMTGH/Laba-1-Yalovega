import sys
import json
import os

DATA_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"categories": [], "expenses": []}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            data.setdefault("categories", [])
            data.setdefault("expenses", [])
            return data
    except (json.JSONDecodeError, IOError):
        return {"categories": [], "expenses": []}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_category(name):
    data = load_data()

    if name in data["categories"]:
        print(f"Категория '{name}' уже существует.")
        return

    data["categories"].append(name)
    save_data(data)
    print(f"Категория '{name}' добавлена.")


def add_expense(amount_str, category, note):
    try:
        amount = float(amount_str)
        if amount < 0:
            print("Ошибка: сумма не может быть отрицательной.")
            return
    except ValueError:
        print("Ошибка: сумма должна быть числом.")
        return

    data = load_data()

    if category not in data["categories"]:
        print(f"Ошибка: категория '{category}' не найдена. Сначала добавьте её через add-category.")
        return

    data["expenses"].append({"amount": amount, "category": category, "note": note})
    save_data(data)
    print(f"Расход добавлен: {amount:.2f} руб. [{category}] {note}")


def show_list(cat_filter=None):
    data = load_data()
    expenses = data["expenses"]

    if not expenses:
        print("Расходов пока нет.")
        return

    filtered = [e for e in expenses if not cat_filter or e["category"] == cat_filter]

    if not filtered:
        print(f"Нет расходов в категории '{cat_filter}'.")
        return

    print(f"{'Сумма':<10} {'Категория':<12} {'Название'}")
    print("-" * 36)

    for e in filtered:
        print(f"{e['amount']:<10.2f} {e['category']:<12} {e['note']}")


def show_sum(cat_filter=None):
    data = load_data()
    total = sum(e["amount"] for e in data["expenses"] if not cat_filter or e["category"] == cat_filter)

    if cat_filter:
        print(f"Сумма по категории '{cat_filter}': {total:.2f} руб.")
    else:
        print(f"Общая сумма расходов: {total:.2f} руб.") 


        if __name__ == "__main__":
            args = sys.argv

    if len(args) < 2:
        print("Ошибка: не указана команда.")
        sys.exit(1)

    if args[1] == "add-category":
        if len(args) != 3:
            print("Ошибка: укажите название категории.")
            sys.exit(1)
        add_category(args[2])

    else:
        if args[1] == "add":
            if len(args) != 5:
                print("Ошибка: формат команды add <сумма> <категория> <название>")
                sys.exit(1)
            add_expense(args[2], args[3], args[4])

