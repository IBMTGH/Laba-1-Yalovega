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






def add_category():
    data = load_data()
    name = input("Введите название категории: ").strip()

    if not name:
        print("Ошибка: название не может быть пустым.")
        return

    if name in data["categories"]:
        print(f"Категория '{name}' уже существует.")
        return

    data["categories"].append(name)
    save_data(data)
    print(f"Категория '{name}' добавлена.")


def add_expense():
    data = load_data()

    if not data["categories"]:
        print("Ошибка: сначала добавьте хотя бы одну категорию (пункт 2).")
        return

    amount_str = input("Введите сумму: ").strip()
    try:
        amount = float(amount_str)
        if amount < 0:
            print("Ошибка: сумма не может быть отрицательной.")
            return
    except ValueError:
        print("Ошибка: сумма должна быть числом.")
        return

    print(f"Доступные категории: {', '.join(data['categories'])}")
    category = input("Введите категорию: ").strip()

    if category not in data["categories"]:
        print(f"Ошибка: категория '{category}' не найдена.")
        return

    note = input("Введите название/описание: ").strip()

    data["expenses"].append({"amount": amount, "category": category, "note": note})
    save_data(data)
    print(f"Расход добавлен: {amount:.2f} руб. [{category}] {note}")





def show_list():
    data = load_data()
    expenses = data["expenses"]

    if not expenses:
        print("Расходов пока нет.")
        return

    cat_filter = input("Введите категорию для фильтра (или Enter для всех): ").strip()
    if cat_filter == "":
        cat_filter = None

    filtered = [e for e in expenses if not cat_filter or e["category"] == cat_filter]

    if not filtered:
        print(f"Нет расходов в категории '{cat_filter}'.")
        return

    print(f"\n{'Сумма':<10} {'Категория':<12} {'Название'}")
    print("-" * 36)

    for e in filtered:
        print(f"{e['amount']:<10.2f} {e['category']:<12} {e['note']}")


def show_sum():
    data = load_data()
    cat_filter = input("Введите категорию для подсчёта (или Enter для всех): ").strip()
    if cat_filter == "":
        cat_filter = None

    total = sum(e["amount"] for e in data["expenses"] if not cat_filter or e["category"] == cat_filter)

    if cat_filter:
        print(f"Сумма по категории '{cat_filter}': {total:.2f} руб.")
    else:
        print(f"Общая сумма расходов: {total:.2f} руб.")





if __name__ == "__main__":
    while True:
        print("\n1. Добавить расход")
        print("2. Добавить категорию")
        print("3. Показать расходы")
        print("4. Показать сумму")
        print("0. Выход")

        choice = input("Выберите действие (цифра): ").strip()

        if choice == "0":
            print("Программа завершена.")
            sys.exit(0)

        else:
            if choice == "1":
                add_expense()

            else:
                if choice == "2":
                    add_category()

                else:
                    if choice == "3":
                        show_list()

                    else:
                        if choice == "4":
                            show_sum()

                        else:
                            print("Ошибка: введите число от 0 до 4.")
