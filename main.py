##enter in the database
fd = open("inventory database.txt", "w")
l1 = "1,milkybar,10,100\n2,fivestar,30,20\n3,honeybar,50,20\n4,proteinbar,100,10"
fd.write(l1)
fd.close()

##open inventory db in read mode
fd = open("inventory database.txt", "r")
txt = fd.read()
products = txt.split("\n")
fd.close()
print(products)

found = False
updated_prod_lst = []
sales_lst = []
total = 0

user_name =input("enter your name: ")
user_phone=input("enter your phone number")
product_id = input("Enter product ID: ")
product_quantity = int(input("Enter product quantity: "))
print(20 * "--")

for product in products:
    product_details = product.split(',')
    if product_details[0] == product_id:
        found = True
        if product_quantity <= int(product_details[3]):
            print("Name           :", product_details[1])
            print("Price          :", product_details[2])
            print("Req Quantity   :", product_quantity)
            print(20 * "--")
            total = product_quantity * int(product_details[2])
            print("Total Price    :", total)
            print(20 * "--")
            product_details[3] = str(int(product_details[3]) - product_quantity)
        else:
            print(f"Not enough stock. Only {product_details[3]} available. Want it all?")
            choice = input("Press 'y' for yes or 'n' for no: ")
            if choice == 'y':
                print("Name               :", product_details[1])
                print("Price              :", product_details[2])
                print("Available Quantity :", product_details[3])
                print(20 * "--")
                total = int(product_details[3]) * int(product_details[2])
                print("Total Price        :", total)
                print(20 * "--")
                product_details[3] = '0'

        updated_prod_lst.append(product_details)
        sales_lst.append([product_details[0], product_details[1], str(product_quantity), str(total), user_name, user_phone])
    else:
        updated_prod_lst.append(product.split(','))

if not found:
    print("Product ID not found!")

##update inventory database
fd = open("inventory database.txt", "w")
for i in updated_prod_lst:
    l = (i[0] + "," + i[1] + "," + i[2] + "," + i[3] + '\n')
    fd.write(l)
fd.close()

##update sales database
fd = open("sales database.txt", "a")
for i in sales_lst:
    l = (i[0] + "," + i[1] + "," + i[2] + "," + i[3] + i[4] + "," + i[5] +'\n')
    fd.write(l)
fd.close()

##print sales
print("\n-- Sales Record --")
for i in sales_lst:
    print(i)