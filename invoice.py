import random
def addItem():
    global total_bill
    item_name = input("Enter item name: ")

    price = input("Enter price: ")
    while not price.isdigit():
        print("Invalid input")
        price = input("Enter price: ")

    quantity = input("Enter quantity: ")
    while not quantity.isdigit():
        print("Invalid input")
        quantity = input("Enter quantity: ")

    total_amount = int(price) * int(quantity)
    total_bill += total_amount

    products.append({
        "Item name": item_name,
        "Price": int(price),
        "Quantity": int(quantity),
        "Total Amount": total_amount
    })

def delete_item():
    global total_bill
    remove_item = input("Enter the name of the item: ")
    for item in products:
        if item['Item name'] == remove_item:
            total_bill -= item["Total Amount"]
            products.remove(item)
            print("Item removed")
            break

def updateItem():
    global total_bill
    update_item = input("Enter the update item name: ")
    for item in products:
        if item['Item name'] == update_item:
            new_price = input("Enter new updated price: ")
            while not new_price.isdigit():
                print("Enter a valid price")
                new_price = input("Enter new updated price: ")

            new_quantity = input("Enter new quantity: ")
            while not new_quantity.isdigit():
                print("Enter a valid number")
                new_quantity = input("Enter new quantity: ")

            previous_total = item["Total Amount"]

            item["Price"] = int(new_price)
            item["Quantity"] = int(new_quantity)
            item["Total Amount"] = int(new_price) * int(new_quantity)

            total_bill += (item["Total Amount"] - previous_total)

            print("Item is updated")

            break
        else:
            print("Entre a valid Item Name")

def display():

    print("-----Invoice Items--------")

    print("Invoice number:", invoice_number)
    print("Customer name:", customer_name)
    print("Mobile No: ", mobileno)
    print("\nItem name\tPrice\tQuantity\tTotal Amount")

    for item in products:
        print(f"{item['Item name']}\t\t{item['Price']}\t{item['Quantity']}\t\t{item['Total Amount']}")
        
    print("\n----------------------------")
    print("Final Total Bill:", total_bill)

products = []
total_bill = 0

invoice_number = random.randint(1000, 9999)
print("Invoice number:", invoice_number)

customer_name = input("Enter customer name: ")

mobileno = input("Enter phone number: ")
while not (mobileno.isdigit() and len(mobileno) == 10):
    print("Invalid phone number")
    mobileno = input("Enter phone number: ")

item_name = input("Enter item name: ")

price = input("Enter price: ")
while not price.isdigit():
    print("Invalid input")
    price = input("Enter price: ")

quantity = input("Enter quantity: ")
while not quantity.isdigit():
    print("Invalid input")
    quantity = input("Enter quantity: ")

total_amount = int(price) * int(quantity)
total_bill += total_amount

products.append({
    "Item name": item_name,
    "Price": int(price),
    "Quantity": int(quantity),
    "Total Amount": total_amount
})
while True:

    print("1. Add Item")
    print("2. Remove Items")
    print("3. Update Items")
    print("4. View Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addItem()
    elif choice == "2":
        delete_item()  
    elif choice == "3":
        updateItem()
    elif choice == "4":
        display()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
display()