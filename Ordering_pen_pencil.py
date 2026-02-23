orders = []   # global list to store all orders
orders1 = []
def pens():
    s = "Welcome to our pen >> pencil shop"
    print(s.center(90))

    b = input("What do you want to buy (pen / pencil): ").lower()

    if b == 'pen':
        print("Pens Available:\n1. Red\n2. Blue\n3. Green")
        c = input("Enter which pen you want: ").lower()

        if c == 'blue':
            print("The cost of the blue pen is $20")
            orders.append("Blue Pen")
            orders1.append(20)
        elif c == 'red':
            print("The cost of the red pen is $35")
            orders.append("Red Pen")
            orders1.append(35)
        elif c == 'green':
            print("The cost of the green pen is $50")
            orders.append("Green Pen")
            orders1.append(50)
        else:
            print("Sorry, we don't have that pen")

    elif b == 'pencil':
        print("Pencils Available:\n1. Apsara\n2. Nataraja")
        d = input("Enter which pencil you want: ").lower()

        if d == 'apsara':
            print("The cost of the Apsara pencil is $100")
            orders.append("Apsara Pencil")
            orders1.append(100)
        elif d == 'nataraja':
            print("The cost of the Nataraja pencil is $400")
            orders.append("Nataraja Pencil")
            orders1.append(400)
        else:
            print("Sorry, we don't have that pencil")

    else:
        print("Invalid choice")

# First order
pens()

# Multiple orders
while True:
    p = input("Do you want to order something more? (y/n): ").lower()
    if p == 'y':
        pens()
    else:
        print("\nThank you! Your total order is:")
        print(orders)
        print(f"The Total cost is {sum(orders1)}")
        break
