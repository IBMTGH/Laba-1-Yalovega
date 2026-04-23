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
