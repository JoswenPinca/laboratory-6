name = input("Enter your name: ")
age = int(input("Enter your age: "))
status = input("Do you have a membership status? ")

if age >= 1 and age < 18:
    if status == "Yes":
        print(f"Your Fee is 450.00 pesos {name}")
    elif status == "No":
        print(f"Your Fee is 650.00 pesos {name}")
    else:
        print("Invalid Input for Membership")
        
elif age >= 18 and age <= 65:
    if status == "Yes":
        print(f"Your Fee is 550.00 pesos {name}")
    elif status == "No":
        print(f"Your Fee is 750.00 pesos {name}")
    else:
        print("Invalid Input for Membership")
        
elif age > 65 and age <=120:
    if status == "Yes":
        print(f"Your Fee is 550.00 pesos {name}")
    elif status == "No":
        print(f"Your Fee is 750.00 pesos {name}")
    else:
        print("Invalid Input for Membership")
else:
     print("Invalid Input for age")