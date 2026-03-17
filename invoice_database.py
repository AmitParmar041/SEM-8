import mysql.connector
from openpyxl import Workbook

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="invoice_database"
)

cursor = conn.cursor()

conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        invoice_number VARCHAR(10),
        customer_name VARCHAR(50),
        mobile_no VARCHAR(10)
    )
""")
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        prod_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        item_name VARCHAR(50),
        price INT(50),
        quantity INT(20),
        total_amount INT(50)
    )
""")
conn.commit()


def create_invoice(invoice_no, customer_name, mobileno):
    cursor.execute(
        "INSERT INTO customer (invoice_number, customer_name, mobile_no) VALUES (%s, %s, %s)",
        (invoice_no, customer_name, mobileno))
        
    conn.commit()
    return cursor.lastrowid

def add_invoice_item(customer_id, item_name, price, quantity, total_amount):

    cursor.execute(
        "INSERT INTO product (customer_id,item_name, price, quantity, total_amount) VALUES (%s, %s, %s, %s, %s)",
        (customer_id, item_name, price, quantity, total_amount))
    conn.commit()
    return cursor.lastrowid

def display_users_details():
    invoice_no = input("enter the invoice number: ")

    cursor.execute(
        "SELECT * FROM customer WHERE invoice_number = %s",(invoice_no,)
    )
    customer = cursor.fetchone()

    if customer is None:
        print("Invoice not Found")
        return
    
    customer_id = customer[0]

    print("\nCustmoer Details")
    print("----------------------")

    print("Invoice Number:", customer[1])
    print("Customer Name:", customer[2])
    print("Mobile Number:", customer[3])

    cursor.execute(
        "SELECT item_name, price, quantity, total_amount FROM product WHERE customer_id = %s",
        (customer_id,)
    )
    items = cursor.fetchall()

    print("\nproduct details")
    print("Item Name\tPrice\tQuantity\tTotal")

    grand_total = 0

    for item in items:
        print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}\t{item[3]}")
        grand_total += item[3]

    print("\nGrand Total:", grand_total)

def delete_users_details():
    invoice_no = input("enter the invoice number: ")

    cursor.execute(
        "SELECT * FROM customer WHERE invoice_number = %s",(invoice_no,)
    )
    customer = cursor.fetchone()

    if customer is None:
        print("Invoice not Found")
        return
    
    customer_id = customer[0]

    cursor.execute(
        "DELETE FROM product WHERE customer_id = %s",(customer_id,)
    )
    cursor.execute(
        "DELETE FROM customer WHERE customer_id = %s",(customer_id,)
    )
    conn.commit()
    print("Invoice deleted done")

def update_users_details():
    invoice_no = input("enter the invoice number: ")

    cursor.execute(
        "SELECT * FROM customer WHERE invoice_number = %s",(invoice_no,)
    )
    customer = cursor.fetchone()

    if customer is None:
        print("Invoice not Found")
        return
    
    customer_id = customer[0]
    print("\nold customer details")
    print("Customer Name:", customer[2])
    print("Mobile Number:", customer[3])
    
    new_name = input("Enter the new customer name: ")
    new_mobileno = input("Enter the new mobile number: ")

    if new_name == "":
        new_name = customer[2]
    if new_mobileno == "":
        new_mobileno = customer[3]

    cursor.execute(
        "UPDATE customer SET customer_name = %s, mobile_no = %s WHERE customer_id = %s", (new_name, new_mobileno, customer_id)
    )
    conn.commit()

    items = cursor.fetchall()

    for item in items:
        print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}\t{item[3]}")

    item_name = input("Enter the product name for update: ")

    if item_name != customer_id:
        print("enter the valid name")
    else:
        return

    item_name = input("Enter the product name for update: ")

    if item_name != "":
        cursor.execute(
            "SELECT  item_name, price, quantity FROM product WHERE item_name = %s",(item_name,)
        )

        product = cursor.fetchone()

        if product is None:
            print("product not found")
            return

        new_price = input("Enter the new price: ")
        while not new_price.isdigit():
            print("Invalid input")
            new_price = input("Enter the new price: ")

        new_quantity = input("Enter the new quantity: ")
        while not new_quantity.isdigit():
            print("Invalid input")
            new_quantity = input("Enter the new quantity: ")

        total_amount = int(new_price) * int(new_quantity)

        cursor.execute(
            "UPDATE product SET price = %s, quantity = %s, total_amount = %s WHERE item_name = %s",
            (new_price, new_quantity, total_amount, item_name)
        )
        conn.commit()

        print("Invoice updated")


while True:
    print("1. New Invoice")
    print("2. View Items Details")
    print("3.Delete the Invoice")
    print("4.Update the Invoice")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        
        invoice_no = input("Enter the invoice number: ")
        customer_name = input("Enter your good name: ")

        mobileno = input("Enter phone number: ")
        while not (mobileno.isdigit() and len(mobileno) == 10 and mobileno[0] in ['7','8','9']):
            print("Invalid phone number")
            mobileno = input("Enter phone number: ")

        customer_id = create_invoice(invoice_no, customer_name, mobileno)

    
        while True:
            print("\n1.Add the Product")
            print("2.Exit")

            choice = input("Enter your choice:")

            if choice == "1":
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
            
                add_invoice_item(customer_id, item_name, price, quantity, total_amount)
            elif choice == "2":
                break

            else:
                print("Invalid choice")

    elif choice == "2":
        display_users_details()
        

    elif choice == "3":
        delete_users_details()

    elif choice == "4":
        update_users_details()

    elif choice == "5":
        break

    else:
        print("Invalid Choice")

conn.close()