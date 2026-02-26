products = []
total_bill = 0

invoice_number = input("Enter the invoice number: ")

customer_name = input("Enter customer name: ")

mobileno = input("Enter phone number: ")
while not (mobileno.isdigit() and len(mobileno) == 10 and mobileno[0] in ['7','8','9']):
    print("Invalid phone number")
    mobileno = input("Enter phone number: ")

seller_state = input("Enter the seller's State Name: ")

buyer_state = input("Enter the buyer's State Name: ")

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

# total_bill += total_amount

print("-----Details------")

print("Invoice number:", invoice_number)
print("Customer name:", customer_name)
print("Mobile No: ", mobileno)
print("Seller's State:", seller_state)
print("Buyer's State:", buyer_state)
print("Item name: ", item_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total Amount without GST:", total_amount)

# print("GST final Amount:", gst_total)
if seller_state == buyer_state:
    cgst = 0.09*total_amount
    sgst = 0.09*total_amount
    print("CGST: ", cgst)
    print("SGST: ", sgst)
    total_amount = total_amount + cgst + sgst
    print("Total Amount with GST:", total_amount)
    
else:
    igst = 0.18*total_amount
    print("IGST: ", igst)
    total_amount = total_amount + igst
    print("Total Amount with GST:", total_amount)