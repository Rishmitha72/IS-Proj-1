name = input("What is your name? ")
current_age = input("How old are you right now? ")
current_age = int(current_age)
age_in_2030 = current_age + 4
print(f"Hey {name}, you will be {age_in_2030} years old in 2030!")

total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
share_per_person = total_bill / num_people
print("Total Bill:", total_bill, ". Each person pays:", share_per_person)
print(type(total_bill))
print(type(num_people))
print(type(share_per_person))

item_name = "Laptop"     
quantity = 2             
price = 499.99           
in_stock = True          
print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)
total_cost = quantity * price
print("Total Cost:", total_cost)
print(type(item_name))   
print(type(quantity))    
print(type(price))       
print(type(in_stock))    
print(type(total_cost))