menu  = {
    'pizza' : 40,
    'pasta' : 30,
    'burger' : 20,
    'salad' : 10,
    "chicken" : 50,
    "chocolate cake" : 25,
}


print("Welcome to our hotel menu!")
print("Here is our menu:")

for item, price in menu.items():
    print(f"{item}: Rs.{price}")


order_total = 0

item_1 = input("Please enter the first item you would like to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} has been added to your order. Current total: Rs.{order_total}")

else:
    print(f"Sorry, {item_1} is not on the menu.")


another_order = input("Would you like to order another item? (yes/no): ")

if another_order == "yes":
    while another_order == "yes":
        item_2 = input("Please enter the second item you would like to order: ")

        if item_2 in menu:
            order_total += menu[item_2]
            print(f"{item_2} has been added to your order. Current total: Rs.{order_total}")
            another_order = input("Would you like to order another item? (yes/no): ")

        else:
            print(f"Sorry, {item_2} is not on the menu. Please try again.")
   

print(f"Your final order total is: Rs.{order_total}")