import json

def load_data():
    try:
        with open('budget_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': 0, 'expenses': []}

def save_data(data):
    with open('budget_data.json', 'w') as file:
        json.dump(data, file)

def add_income(data):
    income = float(input("Enter income amount: "))
    data['income'] += income
    save_data(data)

def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})
    data['income'] -= amount
    save_data(data)

def calculate_budget(data):
    budget = data['income']
    for expense in data['expenses']:
        budget -= expense['amount']
    return budget

def analyze_expenses(data):
    categories = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
    return categories

def main():
    data = load_data()

    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            budget = calculate_budget(data)
            print(f"Remaining budget: {budget}")
        elif choice == '4':
            expenses = analyze_expenses(data)
            print("Expense Analysis:")
            for category, amount in expenses.items():
                print(f"{category}: {amount}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__== '_main_':
    main()