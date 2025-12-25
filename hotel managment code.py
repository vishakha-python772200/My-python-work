print("\n--- Welcome to Hotel Management System ---\n")

# Menu with prices (Dictionary)
menu = {
    "Maharaja-special thali": 300,
    "Indian-food": 180,
    "Italian-food": 220,
    "South-indian-food": 150,
    "Fast-food": 120,
    "Chiness-food": 160,
    "Panjabi-food": 200
}

order_items = []
order_prices = []
GST_RATE = 18.0  # Total GST
# CGST and SGST will be half of total GST
CGST_RATE = GST_RATE / 2
SGST_RATE = GST_RATE / 2 

# Show Menu
print("ITEM\t\t\tPRICE")
print("---------------------------------")
for item, price in menu.items():
    print(item, "\t", price)
print("---------------------------------\n")

# Take orders
n = int(input("How many times you want to order? : "))

for i in range(n):
    items = input("Enter your order (comma separated): ").split(",")

    for item in items:
        item = item.strip()

        if item in menu:
            order_items.append(item)
            order_prices.append(menu[item])
            print(item, "added")
        else:
            print(item, "not available ")

# Bill calculation
subtotal = sum(order_prices)
CGST = subtotal * (CGST_RATE / 100)
SGST = subtotal * (SGST_RATE / 100)
total = subtotal + CGST + SGST

# Bill Receipt
print("\n========== BILL RECEIPT ==========")
print("Item\t\t\tPrice")
print("---------------------------------")

for i in range(len(order_items)):
    print(order_items[i], "\t", order_prices[i])

print("---------------------------------")
print("Subtotal\t\t", round(subtotal, 2))
print(f"CGST ({CGST_RATE}%)\t\t", round(CGST, 2))
print(f"SGST ({SGST_RATE}%)\t\t", round(SGST, 2))
print("---------------------------------")
print("Total Amount\t\t", round(total, 2))
print("=================================")
print("Thank you! Visit again")
