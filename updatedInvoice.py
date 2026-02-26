total_bill = 0

invoice_number = input("Enter the invoice number: ")

customer_name = input("Enter customer name: ")

mobileno = input("Enter phone number: ")
while not (mobileno.isdigit() and len(mobileno) == 10 and mobileno[0] in ['7','8','9']):
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

price = int(price)
quantity = int(quantity)

total_amount = price * quantity

print("\n-----Invoice Details------")

print("Invoice number:", invoice_number)
print("Customer name:", customer_name)
print("Mobile No:", mobileno)
print("Item name:", item_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total Amount:", total_amount)

print("---Enter Updated Details(Optional)---")

new_customer_name = input("Enter new customer name: ")
if new_customer_name != "":
    customer_name = new_customer_name

new_name = input("Enter new item name: ")
if new_name != "":
    item_name = new_name

while True:
    new_price = input("Enter new price: ")

    if new_price == "":
        break
    elif new_price.isdigit():
        price = int(new_price)
        break
    else:
        print("Invalid price")

while True:
    new_quantity = input("Enter new quantity: ")

    if new_quantity == "":
        break
    elif new_quantity.isdigit():
        quantity = int(new_quantity)
        break
    else:
        print("Invalid quantity")

total_amount = price * quantity

print("\n-----Updated Invoice Details------")

print("Invoice number:", invoice_number)
print("Customer name:", customer_name)
print("Mobile No:", mobileno)
print("Item name:", item_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total Amount:", total_amount)