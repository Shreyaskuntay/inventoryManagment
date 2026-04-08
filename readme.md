# Inventory & Sales Management System

A simple Python program to manage product inventory and record sales using text files as a database.

## Files

| File                     | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `main.py`                | Main program                                     |
| `inventory database.txt` | Stores product data (auto-created on run)        |
| `sales database.txt`     | Stores sales records (auto-updated on each sale) |

## How It Works

1. **Inventory database** is initialised with 4 products on every run
2. User enters a **product ID** and **quantity**
3. Program checks stock and prints a receipt
4. **Inventory** is updated with the new stock level
5. **Sale is recorded** in the sales database

## Products

| ID  | Name       | Price | Stock |
| --- | ---------- | ----- | ----- |
| 1   | milkybar   | 10    | 100   |
| 2   | fivestar   | 30    | 20    |
| 3   | honeybar   | 50    | 20    |
| 4   | proteinbar | 100   | 10    |

## How to Run

Make sure you have Python installed, then:

```bash
python main.py
```

## Example Usage

```
Enter product ID: 1
Enter product quantity: 5
----------------------------------------
Name           : milkybar
Price          : 10
Req Quantity   : 5
----------------------------------------
Total Price    : 50
```

## Requirements

- Python 3.x
- No external libraries needed
