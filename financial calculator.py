# Function 1: Calculate Profit
def calculate_profit(selling_price, cost_price):
    profit = selling_price - cost_price
    return profit

# Function 2: Calculate Tax
def calculate_tax(amount, tax_rate):
    tax = amount * (tax_rate / 100)
    return tax

# Function 3: Calculate Discount
def calculate_discount(price, discount_rate):
    discount = price * (discount_rate / 100)
    return discount

# Function 4: Calculate Loan Paymenyt
def calculate_loan(principal, rate, years):
    interest =  principal * (rate / 100) * years
    total = principal + interest
    monthly_payment = total / (years * 12)
    return monthly_payment

# Function to display menu
def display_menu():
    print("\n***** FINANCIAL CALCULATOR *****")
    print("1. Calculate Profit")
    print("2. Calculate Tax")
    print("3. Calculate Discount")
    print("4. Calculate Loan Payment")
    print("5. Exit")


# Main program
while True:
    display_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        selling = float(input("Enter selling price: "))
        cost = float(input("Enter cost price: "))

        result = calculate_profit(selling, cost)
        print(f"Profit: ${result:.2f}")

    elif choice == "2":
        amount = float(input("Enter amount: "))
        rate = float(input("Enter tax rate (%): "))

        result = calculate_tax(amount, rate)
        print(f"Tax: ${result:.2f}")

    elif choice == "3":
        price = float(input("Enter price: "))
        rate = float(input("Enter discount rate (%): "))

        result = calculate_discount(price, rate)
        print(f"Discount: ${result:.2f}")

    elif choice == "4":
        principal = float(input("Enter loan amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        years = float(input("Enter loan period in years: "))

        if years <= 0:
            print("Loan period must be greater than zero.")
        else:
            result = calculate_loan(principal, rate, years)
            print(f"Monthly payment: ${result:.2f}")

    elif choice == "5":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice. Please select 1-5.")