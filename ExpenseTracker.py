class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def display(self):
        return f"{self.name} - ${self.amount}"

class CategorizedExpense(Expense):
    def __init__(self, name, amount, category):
        super().__init__(name,amount)
        self.category = category

    def display(self):
        return f"{self.name} - ${self.amount:.2f} ({self.category})"


Expenses = []


def menu():
    print("\n Welcome to the Expense Tracker")
    print("1. add Expense")
    print("2. view Expenses")
    print("3. Total Spent")
    print("4. Quit")



def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount spent: "))
    category = input("Enter category for expense: ")
    Expenses.append({"name": name, "amount": amount, "category": category})
    print("Expense added :)")


def view_expense():
    if not Expenses:
        print("No expenses yet")
    else:
        print("\n---Your Expenses---")
        for e in Expenses:
            print(f"{e['name']} - ${e['amount']:.2f} ({e['category']})")


def total_expense():
    total = sum(e['amount'] for e in Expenses)
    print(total)




def main():
    while True:
        menu()
        choice = input("Enter a number between 1-4: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            print("Goodbye")
            break
        else:
            print("Invalid input")


main()
