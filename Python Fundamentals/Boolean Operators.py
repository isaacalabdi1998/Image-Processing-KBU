
# Boolean Operators
name = "Ghost"
gender = "M"
age = 25

print(age > 20 and gender == "M" and name == "Ghost") # True
print(age > 20 and gender == "F" and name == "Ghost") # False

print(age > 20 or gender == "M" or name == "Ghost") # True
print(age > 20 or gender == "F" or name == "Ghost") # True

print(age > 20)      # True
print(not age > 20) # False
