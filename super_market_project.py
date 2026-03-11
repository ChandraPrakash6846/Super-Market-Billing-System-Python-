# Super Market Billing System
# This program allows users to purchase multiple items,
# applies discounts, and generates a final bill.

# Dictionary storing item details: item_no -> (name, price, unit)
items = {
    1: ("Rice", 50, "kg"),
    2: ("Wheat Flour", 45, "kg"),
    3: ("Sugar", 40, "kg"),
    4: ("Cooking Oil", 140, "litre"),
    5: ("Milk", 60, "litre"),
    6: ("Bread", 30, "packet"),
    7: ("Eggs", 6, "piece"),
    8: ("Soap", 35, "piece"),
    9: ("Shampoo", 120, "bottle"),
    10: ("Biscuits", 25, "packet"),
}

# Takes customer name and phone number with validation
def user_input():
    user_name = input("Enter your name: ")
    user_phone = input("Enter your phone number: ")

    # Validate phone number
    if not user_phone.isdigit() or len(user_phone) != 10:
        print("Invalid phone number. Please enter a 10-digit number.")
        return user_input()

    return user_name, user_phone

# Displays store header
def show_header():
    print("=" * 50)
    print("WELCOME TO STAR DAILY MART".center(50))
    print("=" * 50)
    print("Fresh • Affordable • Trusted\n")

# Displays available items
def show_menu():
    print("-" * 50)
    print("AVAILABLE ITEMS (price per unit)")
    print("-" * 50)
    for no, (name, price, unit) in items.items():
        print(f"{no:2d}. {name:<14} : ₹{price} per {unit}")
    print("-" * 50)

# Takes integer input safely
def input_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")

# Takes float input safely
def input_float(prompt):
    while True:
        try:
            val = float(input(prompt).strip())
            if val <= 0:
                print("Please enter a positive number.")
                continue
            return val
        except ValueError:
            print("Please enter a valid number.")

# Displays discount offers
def discount_offers():
    print("\nToday's Discount Offers:")
    print("1. Buy 5 kg or more of Rice and get 5% off on Rice.")
    print("2. Buy 3 litres or more of Milk and get 10% off on Milk.")
    print("3. Buy 2 packets or more of Biscuits and get 15% off on Biscuits.\n")

# Main function controlling the billing process
def main():
    # Get customer details
    user_name, user_phone = user_input()

    show_header()
    show_menu()
    discount_offers()

    cart = []  # Stores purchased items

    # Loop to add multiple items
    while True:
        item_no = input_int("Enter item number to buy: ")
        if item_no not in items:
            print("Invalid item number. Try again.")
            continue

        name, price, unit = items[item_no]
        qty = input_float(f"Enter quantity of {name} (in {unit}): ")

        # Store item details in cart
        cart.append((item_no, name, price, unit, qty))
        print(f"Added {qty} {unit} of {name} at ₹{price} each.\n")

        more = input("Do you want to add more items? (y/n): ").strip().lower()
        if more not in ("y", "yes"):
            break

    # Print final bill
    print("\n" + "=" * 20 + " FINAL BILL " + "=" * 20)

    subtotal = 0.0      # Total before discount
    grand_total = 0.0   # Total after discount

    # Process each item in cart
    for item_no, name, price, unit, qty in cart:
        original_line = price * qty
        subtotal += original_line

        discount = 0

        # Apply item-specific discounts
        if item_no == 1 and qty >= 5:
            discount = 0.05
            print("5% discount applied on Rice.")
        elif item_no == 5 and qty >= 3:
            discount = 0.10
            print("10% discount applied on Milk.")
        elif item_no == 10 and qty >= 2:
            discount = 0.15
            print("15% discount applied on Biscuits.")

        # Calculate final price after discount
        if discount > 0:
            print(f"Original price: ₹{original_line:.2f}")
            final_line = original_line * (1 - discount)
        else:
            final_line = original_line

        print(f"{name:14}  {qty:6.2f} {unit:<6} x ₹{price:6.2f}  =  ₹{final_line:7.2f}")
        grand_total += final_line

    # Display totals and customer info
    print("-" * 56)
    print(f"Subtotal before discount: ₹{subtotal:.2f}")
    print(f"GRAND TOTAL: ₹{grand_total:7.2f}")
    print("=" * 56)
    print("Thank you for shopping at STAR DAILY MART!".center(56))
    print("Visit Again!".center(56))
    print(f"Customer Name : {user_name}")
    print(f"Phone Number  : {user_phone}")

# Program execution starts here
if __name__ == "__main__":
    main()
