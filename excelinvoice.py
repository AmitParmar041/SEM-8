import random
from openpyxl import Workbook

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
    global customer_name

    new_name = input("Enter new customer name: ")

    if new_name != "":
        customer_name = new_name
        print("Customer name updated Done ✔")

    update_item = input("Enter the update item name: ")

    for item in products:
        if item['Item name'] == update_item:
            
            previous_total = item["Total Amount"]

            new_name = input("Enter new item name: ")
            if new_name != "":
                item["Item name"] = new_name
            
            while True:
                new_price = input("Enter new price: ")

                if new_price == "":
                    break

                elif new_price.isdigit():
                    item["Price"] = int(new_price)
                    break
                else:
                    print("Enter valid input")

            while True:
                new_quantity = input("Enter new quantity: ")

                if new_quantity == "":
                    break 

                elif new_quantity.isdigit():
                    item["Quantity"] = int(new_quantity)
                    break
                else:
                    print("Enter valid input")

            item["Total Amount"] = item["Price"] * item["Quantity"]

            total_bill += item["Total Amount"] - previous_total

            print("Item updated successfully")
            break

    print("Enter a valid Item Name")

def searchItem():
    search_invoice = input("Enter invoice number: ")

    if search_invoice == invoice_number:
        print("Invoice Found")
        display()
    else:
        print("Invoice not found")

def save_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Invoice"


    ws.append(["Customer name", customer_name])
    ws.append([])
    ws.append(["Item name", "Price", "Quantity", "Total Amount"])

    for item in products:
        ws.append([item["Item name"], item["Price"], item["Quantity"], item["Total Amount"]])

    ws.append([])
    ws.append(["Total Amount", "", "", total_bill])

    filename = "invoice.xlsx"
    wb.save(filename)
    print(f"Invoice saved to {filename}")

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

# invoice_number = random.randint(1000, 9999)
invoice_number = input("Enter the invoice number: ")
# print("Invoice number:", invoice_number)

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
    print("5. Search the Item using invoice No.")
    print("6. Save into Excel")
    print("7. Exit")

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
        searchItem()
    elif choice == "6":
        save_excel()
    elif choice == "7":
        break
    else:
        print("Invalid choice")
display()