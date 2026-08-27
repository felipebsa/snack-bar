import json
import os
import csv
import shutil
from datetime import datetime

DATA_FILE = "snack_bar_data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        data = {"products": [], "orders": []}
        save_data(data)
        return data

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def find_product(data, code):
    for product in data["products"]:
        if product["code"] == code:
            return product
    return None


def register_product(data):
    print("\n--- Register Product ---")
    code = input("Product code: ").strip()

    if find_product(data, code):
        print("A product with this code already exists.")
        return

    name = input("Product name: ").strip()

    try:
        price = float(input("Price: $"))
        quantity = int(input("Stock quantity: "))
    except ValueError:
        print("Invalid price or quantity. Registration cancelled.")
        return

    product = {
        "code": code,
        "name": name,
        "price": price,
        "quantity": quantity,
    }

    data["products"].append(product)
    save_data(data)
    print(f"Product '{name}' registered successfully!")


def list_products(data):
    print("\n--- Registered Products ---")

    if not data["products"]:
        print("No products registered yet.")
        return

    for product in data["products"]:
        print(
            f"[{product['code']}] {product['name']} - "
            f"${product['price']:.2f} - "
            f"Stock: {product['quantity']}"
        )


def make_order(data):
    print("\n--- New Order ---")

    if not data["products"]:
        print("There are no products registered yet.")
        return

    customer = input("Customer name: ").strip()
    code = input("Product code: ").strip()

    product = find_product(data, code)
    if not product:
        print("Product not found.")
        return

    try:
        quantity = int(input(f"Quantity of '{product['name']}': "))
    except ValueError:
        print("Invalid quantity.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    if quantity > product["quantity"]:
        print(f"Not enough stock. Available: {product['quantity']}")
        return

    total_price = quantity * product["price"]
    product["quantity"] -= quantity

    order = {
        "customer": customer,
        "product_code": product["code"],
        "product_name": product["name"],
        "quantity": quantity,
        "total_price": total_price,
        "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
    }

    data["orders"].append(order)
    save_data(data)

    print(f"Order registered! Total: ${total_price:.2f}")


def view_orders(data):
    print("\n--- Orders History ---")

    if not data["orders"]:
        print("No orders registered yet.")
        return

    for order in data["orders"]:
        print(
            f"{order['date']} - Customer: {order['customer']} - "
            f"{order['quantity']}x {order['product_name']} "
            f"- ${order['total_price']:.2f}"
        )


# ---------- Extra features ----------

def search_product_by_name(data):
    print("\n--- Search Product by Name ---")

    if not data["products"]:
        print("No products registered yet.")
        return

    term = input("Type part of the product name: ").strip().lower()
    found = [p for p in data["products"] if term in p["name"].lower()]

    if not found:
        print("No product matches that name.")
        return

    for product in found:
        print(
            f"[{product['code']}] {product['name']} - "
            f"${product['price']:.2f} - "
            f"Stock: {product['quantity']}"
        )


def update_price(data):
    print("\n--- Update Product Price ---")
    code = input("Product code: ").strip()

    product = find_product(data, code)
    if not product:
        print("Product not found.")
        return

    try:
        new_price = float(input(f"New price for '{product['name']}': $"))
    except ValueError:
        print("Invalid price.")
        return

    product["price"] = new_price
    save_data(data)
    print("Price updated successfully!")


def remove_product(data):
    print("\n--- Remove Product ---")
    code = input("Product code: ").strip()

    product = find_product(data, code)
    if not product:
        print("Product not found.")
        return

    confirm = input(f"Are you sure you want to remove '{product['name']}'? (y/n): ").strip().lower()
    if confirm != "y":
        print("Removal cancelled.")
        return

    data["products"].remove(product)
    save_data(data)
    print("Product removed successfully!")


def sales_report(data):
    print("\n--- Sales Report ---")

    if not data["orders"]:
        print("No sales yet.")
        return

    total_revenue = sum(order["total_price"] for order in data["orders"])
    total_items = sum(order["quantity"] for order in data["orders"])

    print(f"Total orders: {len(data['orders'])}")
    print(f"Total items sold: {total_items}")
    print(f"Total revenue: ${total_revenue:.2f}")


def best_selling_product(data):
    print("\n--- Best-Selling Product ---")

    if not data["orders"]:
        print("No sales yet.")
        return

    sales_by_product = {}
    for order in data["orders"]:
        name = order["product_name"]
        sales_by_product[name] = sales_by_product.get(name, 0) + order["quantity"]

    best_name = max(sales_by_product, key=sales_by_product.get)
    print(f"Best seller: {best_name} ({sales_by_product[best_name]} units sold)")


def total_sold_today(data):
    print("\n--- Total Sold Today ---")

    today = datetime.now().strftime("%d/%m/%Y")
    today_orders = [o for o in data["orders"] if o["date"].startswith(today)]

    if not today_orders:
        print("No sales today.")
        return

    total_today = sum(order["total_price"] for order in today_orders)
    print(f"Orders today: {len(today_orders)}")
    print(f"Total sold today: ${total_today:.2f}")


def export_report_csv(data):
    print("\n--- Export Report to CSV ---")

    if not data["orders"]:
        print("No orders to export.")
        return

    filename = "orders_report.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Customer", "Product Code", "Product", "Quantity", "Total"])
        for order in data["orders"]:
            writer.writerow([
                order["date"],
                order["customer"],
                order["product_code"],
                order["product_name"],
                order["quantity"],
                f"{order['total_price']:.2f}",
            ])

    print(f"Report exported to '{filename}'.")


def backup_data():
    print("\n--- Backup Data File ---")

    if not os.path.exists(DATA_FILE):
        print("There is no data file to back up yet.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}.json"
    shutil.copy(DATA_FILE, backup_name)
    print(f"Backup created: '{backup_name}'.")


# ---------- Menu ----------

def show_menu():
    print("\n===== SNACK BAR SYSTEM =====")
    print("1 - Register product")
    print("2 - List products")
    print("3 - Make order")
    print("4 - View orders history")
    print("5 - Search product by name")
    print("6 - Update product price")
    print("7 - Remove product")
    print("8 - Sales report")
    print("9 - Best-selling product")
    print("10 - Total sold today")
    print("11 - Export report to CSV")
    print("12 - Backup data file")
    print("0 - Exit")


def main():
    data = load_data()

    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        match option:
            case "1":
                register_product(data)
            case "2":
                list_products(data)
            case "3":
                make_order(data)
            case "4":
                view_orders(data)
            case "5":
                search_product_by_name(data)
            case "6":
                update_price(data)
            case "7":
                remove_product(data)
            case "8":
                sales_report(data)
            case "9":
                best_selling_product(data)
            case "10":
                total_sold_today(data)
            case "11":
                export_report_csv(data)
            case "12":
                backup_data()
            case "0":
                print("Goodbye! See you next time.")
                break
            case _:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
