import csv
import os

# Initialize an empty list to store expenditures
expenses = []

# Function to add an expense
def add_expense(category, description, amount, date):
    expenses.append({'category': category, 'description': description, 'amount': amount, 'date': date})

# Function to display all expenses
def display_expenses():
    for i, item in enumerate(expenses, 1):
        print(f"{i}. {item['category']} - {item['description']} - ${item['amount']:.2f} on {item['date']}")

# Function to categorize expenses
def view_by_category(category):
    for item in expenses:
        if item['category'] == category:
            print(f"{item['description']} - ${item['amount']:.2f} on {item['date']}")

# Function to save expenses to a CSV file
def save_expenses():
    with open('expenses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Description', 'Amount', 'Date'])
        for expense in expenses:
            writer.writerow([expense['category'], expense['description'], expense['amount'], expense['date']])

# Function to load expenses from a CSV file
def load_expenses():
    if os.path.exists('expenses.csv'):
        with open('expenses.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)

# Main loop
def main():
    load_expenses()
    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. View expenses by category")
        print("4. Save expenses")
        print("5. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter category: ")
            desc = input("Enter description: ")
            amt = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, desc, amt, date)
            print("Expense added successfully!")
        
        elif choice == '2':
            display_expenses()
        
        elif choice == '3':
            category = input("Enter category: ")
            view_by_category(category)
        
        elif choice == '4':
            save_expenses()
            print("Expenses saved successfully!")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
