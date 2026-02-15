# python restro
menu = {
    'pizza': 40,
    'burger': 67,
    'salad': 90,
    'coffee': 89,
    'green_tea': 90,
}

order_total = 0
ordered_items = []  # List to track what was bought

print("--- Welcome To Python Restro ---")
print("Pizza : 40\nburger : 67\nsalad : 90\ncoffe : 89\ngreen_tea : 90")

while True:
    item = input("\nEnter item name (or type 'done' to finish): ").lower()

    if item == 'done':
        break

    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)  # Add item to our receipt list
        print(f"Added {item}. Current Total: {order_total}")
    else:
        print("Sorry, that item is not on the menu.")

# Final Receipt Printing
print("\n" + "="*20)
print("FINAL RECEIPT")
print(f"Items: {", ".join(ordered_items)}")
print(f"Total Amount: {order_total}")
print("="*20)
