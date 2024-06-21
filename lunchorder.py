def display_menu(menu):
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item.capitalize()}: ${price:.2f}")

def take_order(menu):
    order = {}
    while True:
        display_menu(menu)
        choice = input("Please enter an item you want to order (or type done to finish your order): ").strip().lower()
        if choice == 'done':
            break
        elif choice in menu:
            quantity = int(input(f"How many {choice}s would you like to order? "))
            if choice in order:
                order[choice] += quantity
            else:
                order[choice] = quantity
            display_current_total(order, menu)
        else:
            print("Invalid choice. Please try again.")
    return order
#order total
def calculate_total(order, menu):
    total = 0.0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

def display_order(order, menu):
    print("\nYour Final Order:")
    for item, quantity in order.items():
        print(f"{item.capitalize()}: {quantity} x ${menu[item]:.2f} = ${menu[item] * quantity:.2f}")
    total = calculate_total(order, menu)
    print(f"Total: ${total:.2f}")

def display_current_total(order, menu):
    print("\nCurrent Order:")
    for item, quantity in order.items():
        print(f"{item.capitalize()}: {quantity} x ${menu[item]:.2f} = ${menu[item] * quantity:.2f}")
    total = calculate_total(order, menu)
    print(f"Current Total: ${total:.2f}\n")

def main():
    menu = {
        'burger': 5.99,
        'fries': 2.99,
        'soda': 1.49,
        'salad': 4.99,
        'pizza': 7.99,
    }

    print("Welcome to the lunch order system!")
    order = take_order(menu)
    display_order(order, menu)
    print("Thank you for your order!")

if __name__ == "__main__":
    main()
