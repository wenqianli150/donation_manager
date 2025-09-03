from datetime import datetime
from collections import defaultdict

# ---------------------------
# Data storage
# ---------------------------
donations = []
distributions = []

# ---------------------------
# Functions
# ---------------------------

def register_donation():
    donor_name = input("Enter donor's name: ")
    donation_type = input("Enter donation type (money, food, clothing, etc.): ").lower()
    quantity = float(input("Enter quantity/amount: "))
    date = input("Enter date (YYYY-MM-DD) [leave empty for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    donations.append({
        "donor_name": donor_name,
        "donation_type": donation_type,
        "quantity": quantity,
        "date": date
    })
    print(f"✅ Donation registered: {donor_name} -> {quantity} {donation_type} on {date}\n")

def distribute_donation():
    donation_type = input("Enter donation type to distribute: ").lower()
    quantity = float(input("Enter quantity/amount to distribute: "))
    date = input("Enter date (YYYY-MM-DD) [leave empty for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    distributions.append({
        "donation_type": donation_type,
        "quantity": quantity,
        "date": date
    })
    print(f"✅ Distributed: {quantity} {donation_type} on {date}\n")

def generate_inventory_report():
    inventory = defaultdict(float)
    for d in donations:
        inventory[d['donation_type']] += d['quantity']
    for dist in distributions:
        inventory[dist['donation_type']] -= dist['quantity']
    print("\n--- Inventory Report ---")
    for donation_type, qty in inventory.items():
        print(f"{donation_type.capitalize()}: {qty}")
    print("------------------------\n")

def generate_donor_report():
    donor_totals = defaultdict(float)
    for d in donations:
        donor_totals[d['donor_name']] += d['quantity']
    print("\n--- Donor Report ---")
    for donor, total in donor_totals.items():
        print(f"{donor}: {total}")
    print("--------------------\n")

def main_menu():
    while True:
        print("=== Shelter Donation Manager ===")
        print("1. Register Donation")
        print("2. Distribute Donation")
        print("3. Generate Inventory Report")
        print("4. Generate Donor Report")
        print("5. Exit")
        choice = input("Select an option (1-5): ")
        print()
        if choice == '1':
            register_donation()
        elif choice == '2':
            distribute_donation()
        elif choice == '3':
            generate_inventory_report()
        elif choice == '4':
            generate_donor_report()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.\n")

# ---------------------------
# Entry point
# ---------------------------
if __name__ == "__main__":
    main_menu()
