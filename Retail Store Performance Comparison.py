# Retail Store Performance Comparison System
# Author: Bhargavi Devi
# Description: Compares performance of multiple retail stores based on sales and profit

def add_store_data(stores):
    name = input("Enter store name: ")
    sales = float(input("Enter total sales: "))
    profit = float(input("Enter total profit: "))
    stores[name] = {
        "sales": sales,
        "profit": profit
    }
    print("Store added successfully.\n")


def display_all_stores(stores):
    if not stores:
        print("No store data available.\n")
        return

    print("\nStore Performance Details:")
    print("-" * 40)
    for name, data in stores.items():
        print(f"Store Name : {name}")
        print(f"Sales      : {data['sales']}")
        print(f"Profit     : {data['profit']}")
        print("-" * 40)


def best_sales_store(stores):
    best = max(stores, key=lambda x: stores[x]["sales"])
    return best


def best_profit_store(stores):
    best = max(stores, key=lambda x: stores[x]["profit"])
    return best


def average_sales(stores):
    total = sum(store["sales"] for store in stores.values())
    return total / len(stores)


def average_profit(stores):
    total = sum(store["profit"] for store in stores.values())
    return total / len(stores)


def performance_summary(stores):
    if not stores:
        print("No data to analyze.\n")
        return

    print("\nPerformance Summary")
    print("-" * 40)

    print("Best Sales Store  :", best_sales_store(stores))
    print("Best Profit Store :", best_profit_store(stores))
    print("Average Sales     :", average_sales(stores))
    print("Average Profit    :", average_profit(stores))

    print("-" * 40)


def menu():
    print("\nRetail Store Performance Comparison")
    print("1. Add Store Data")
    print("2. Display All Stores")
    print("3. Performance Summary")
    print("4. Exit")


def main():
    stores = {}

    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_store_data(stores)

        elif choice == "2":
            display_all_stores(stores)

        elif choice == "3":
            performance_summary(stores)

        elif choice == "4":
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.\n")


# Program execution starts here
main()
