def simple_interest():
    print("Simple Interest")
    p = float(input("Enter amount: "))
    r = float(input("Enter rate (%): "))
    t = float(input("Enter time (years): "))
    si = (p * r * t) / 100
    total = p + si
    print(f"You will earn ${si:.2f} interest.")
    prant(f"Final total amount: ${total:.2f}")

def savings_goal():
    print("Saving Goal")
    goal = float(input("Enter your goal amount: "))
    monthly = float(input("How much can you save per month: "))
    months = goal / monthly
    print(f"It will take about {months:.1f} months to reach your goal.")

def budget_check():
    print("Monthly Budget Check")
    income = float(input("What is your monthly income: "))
    expenses = float(input("Enter your monthly expenses: "))
    balance = income - expenses
    if balance > 0:
        print(f"You’ll save ${balance:.2f} this month.")
    else:
        print(f"You’re short by ${abs(balance):.2f} this month.")

def main():
    while True:
        print("\nSimple Financial Calculator")
        print("1. Simple Interest")
        print("2. Savings Goal")
        print("3. Budget Check")
        print("Type 'exit' to quit.")
        
        choice = input("Choose an option (1–3): ").strip().lower()
        
        if choice == "1":
            simple_interest()
        elif choice == "2":
            savings_goal()
        elif choice == "3":
            budget_check()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Can't do, please choose an option from 1-3.")

if __name__ == "__main__":
    main()
