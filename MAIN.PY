# =============================================================================
# Project       : Personal Net Worth & Expense Tracker
# Author        : DHRUV KUMAR SHARMA
# Roll No       : 25BAI10952
# Domain        : Finance & Banking
# =============================================================================

import csv
import os
from datetime import datetime

# --------------------- CLASSES ---------------------
class Asset:
    def __init__(self, name, value, category="General"):
        self.name = name
        self.value = float(value)
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d")

class Liability:
    def __init__(self, name, amount, due_date):
        self.name = name
        self.amount = float(amount)
        self.due_date = due_date

class Expense:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = float(amount)
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")

# --------------------- FILE PATHS ---------------------
os.makedirs("data", exist_ok=True)
ASSET_FILE = "data/assets.csv"
LIABILITY_FILE = "data/liabilities.csv"
EXPENSE_FILE = "data/expenses.csv"

# --------------------- LOAD DATA ---------------------
def load_assets():
    assets = []
    if os.path.exists(ASSET_FILE):
        with open(ASSET_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if len(row) >= 3:
                    assets.append(Asset(row[0], row[1], row[2]))
    return assets

def load_liabilities():
    liabilities = []
    if os.path.exists(LIABILITY_FILE):
        with open(LIABILITY_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) >= 3:
                    liabilities.append(Liability(row[0], row[1], row[2]))
    return liabilities

def load_expenses():
    expenses = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if len(row) >= 3:
                    expenses.append(Expense(row[0], row[1], row[2]))
    return expenses

# --------------------- SAVE DATA ---------------------
def save_assets(assets):
    with open(ASSET_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Value", "Category", "Date"])
        for a in assets:
            writer.writerow([a.name, a.value, a.category, a.date])

def save_liabilities(liabilities):
    with open(LIABILITY_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Amount", "Due Date"])
        for l in liabilities:
            writer.writerow([l.name, l.amount, l.due_date])

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Amount", "Description", "Date"])
        for e in expenses:
            writer.writerow([e.category, e.amount, e.description, e.date])

# --------------------- MENU FUNCTIONS ---------------------
def add_asset(assets):
    print("\n=== Add Asset ===")
    name = input("Asset Name: ")
    value = float(input("Value: "))
    category = input("Category (e.g., Cash, Property): ")
    assets.append(Asset(name, value, category))
    save_assets(assets)
    print("Asset added!")

def add_liability(liabilities):
    print("\n=== Add Liability ===")
    name = input("Liability Name: ")
    amount = float(input("Amount: "))
    due = input("Due Date (YYYY-MM-DD): ")
    liabilities.append(Liability(name, amount, due))
    save_liabilities(liabilities)
    print("Liability added!")

def add_expense(expenses):
    print("\n=== Add Expense ===")
    cat = input("Category (Food/Transport/etc.): ")
    amt = float(input("Amount: "))
    desc = input("Description: ")
    expenses.append(Expense(cat, amt, desc))
    save_expenses(expenses)
    print("Expense added!")

def view_assets(assets):
    print("\n=== Assets ===")
    for a in assets:
        print(f"{a.name} | ₹{a.value} | {a.category} | {a.date}")

def view_liabilities(liabilities):
    print("\n=== Liabilities ===")
    for l in liabilities:
        print(f"{l.name} | ₹{l.amount} | Due: {l.due_date}")

def view_expenses(expenses):
    print("\n=== Expenses ===")
    for e in expenses:
        print(f"{e.date} | {e.category} | ₹{e.amount} | {e.description}")

def generate_report(assets, liabilities, expenses):
    total_assets = sum(a.value for a in assets)
    total_liab = sum(l.amount for l in liabilities)
    total_exp = sum(e.amount for e in expenses)
    net_worth = total_assets - total_liab

    print("\n" + "="*50)
    print("           FINANCIAL REPORT")
    print("="*50)
    print(f"Total Assets      : ₹{total_assets:,.2f}")
    print(f"Total Liabilities : ₹{total_liab:,.2f}")
    print(f"Total Expenses    : ₹{total_exp:,.2f}")
    print(f"NET WORTH         : ₹{net_worth:,.2f}")
    print("="*50)

# --------------------- MAIN LOOP ---------------------
def main():
    assets = load_assets()
    liabilities = load_liabilities()
    expenses = load_expenses()

    while True:
        print("\n" + "="*40)
        print("   PERSONAL FINANCE TRACKER")
        print("="*40)
        print("1. Add Asset")
        print("2. Add Liability")
        print("3. Add Expense")
        print("4. View Assets")
        print("5. View Liabilities")
        print("6. View Expenses")
        print("7. Generate Report")
        print("8. Exit")
        print("-"*40)
        
        ch = input("Choose (1-8): ").strip()
        
        if ch == "1": add_asset(assets)
        elif ch == "2": add_liability(liabilities)
        elif ch == "3": add_expense(expenses)
        elif ch == "4": view_assets(assets)
        elif ch == "5": view_liabilities(liabilities)
        elif ch == "6": view_expenses(expenses)
        elif ch == "7": generate_report(assets, liabilities, expenses)
        elif ch == "8": print("Goodbye!"); break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()
