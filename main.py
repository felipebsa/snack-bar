import os
import json

DATA_FILE = "snack-bar-of-lanlan.json"
products = []
orders = []


def load_data():
    global products, orders
    if not os.path.exists(DATA_FILE):
        products = []
        orders = []
        return
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            products = data.get("products", [])
            orders = data.get("orders", [])
    except (json.JSONDecodeError, OSError) as e:
        print(f"Erro ao carregar dados: {e}")
        products = []
        orders = []


def save_data():
    data = {
        "products": products,
        "orders": orders
    }
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError:
        print(f"Erro ao salvar dados")
