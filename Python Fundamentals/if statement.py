userName = "Memo"
price = 49
age = 18

if age <= 18 :
    print(f"Name : {userName} Normal Price :{price}")
    print(f"Because Your Under 18 The New Price : {price - 18}")
else:
    print(f"Name : {userName} Normal Price :{price}")
    print(f"Because Your Not Under 18 The New Price : {price}")


# Nested IF statements

var = 100

if var < 200:
    print ("Expression value is less than 200")
    if var == 150:
        print("Which is 150")
    elif var == 100:
        print("Which is 100")
    elif var == 50:
        print("Which is 50")
    elif var < 50:
        print("Expression value is less than 50")
elif var >= 200 :
    print("Value is equal or bigger than 200")
else:
    print("Could not find true expression")

# Expression value is less than 200
# Which is 100
