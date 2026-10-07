# 🥪 Snack Bar System

A command-line system to manage a snack bar: product registration, stock control, orders, and sales reports. Built in pure Python (standard library only), with data persisted in a JSON file.

> School project developed at **ETEC Vasco Antonio Venchiarutti** (Systems Development technical course).

---

## Features

**Core**
- Register products (code, name, price, stock quantity)
- List all registered products
- Create orders with automatic stock deduction
- View the full orders history

**Extras**
- Search products by name (partial match, case-insensitive)
- Update a product's price
- Remove a product (with confirmation)
- Sales report: total orders, items sold, and revenue
- Best-selling product
- Total sold today
- Export orders to CSV
- Backup the data file with a timestamp

## Validations

- Duplicate product codes are rejected
- Invalid price or quantity input cancels the operation instead of crashing
- Orders are blocked when the product doesn't exist, the quantity is zero or negative, or there isn't enough stock
- Removing a product requires explicit confirmation

## Requirements

- **Python 3.10+** (the menu uses `match/case`)
- No external dependencies

## How to run

```bash
git clone https://github.com/felipebsa/snack-bar.git
cd snack-bar
python main.py
```

On the first run, the file `snack_bar_data.json` is created automatically.

## Menu

```
===== SNACK BAR SYSTEM =====
1  - Register product
2  - List products
3  - Make order
4  - View orders history
5  - Search product by name
6  - Update product price
7  - Remove product
8  - Sales report
9  - Best-selling product
10 - Total sold today
11 - Export report to CSV
12 - Backup data file
0  - Exit
```

## Generated files

| File | Created by | Description |
| --- | --- | --- |
| `snack_bar_data.json` | First run | Products and orders database |
| `orders_report.csv` | Option 11 | Orders export (date, customer, product, quantity, total) |
| `backup_YYYYMMDD_HHMMSS.json` | Option 12 | Timestamped copy of the data file |

## Data structure

```json
{
    "products": [
        { "code": "01", "name": "Hot dog", "price": 8.5, "quantity": 30 }
    ],
    "orders": [
        {
            "customer": "Maria",
            "product_code": "01",
            "product_name": "Hot dog",
            "quantity": 2,
            "total_price": 17.0,
            "date": "07/10/2026 18:30"
        }
    ]
}
```

## Project structure

```
snack-bar/
├── main.py      # all the logic and the interactive menu
└── README.md
```

## What I practiced

- Functions with a single responsibility
- JSON file persistence (`json`)
- CSV export (`csv`) and file copying (`shutil`)
- Input validation with `try/except`
- Dates and times with `datetime`
- Structural pattern matching (`match/case`)
- Data aggregation with comprehensions and dictionaries

## Possible improvements

- Orders with multiple items
- Low-stock alerts
- Migration from JSON to SQLite
- Automated tests with Pytest
- Separation into modules (data, services, interface)

---

## Author

**Felipe Barbosa Santos** · [GitHub](https://github.com/felipebsa) · [LinkedIn](https://www.linkedin.com/in/felipe-barbosa-santos-b402a33a8/)
