
# --------------------Tuple Rules--------------------
# 1- Tuple Items Are Enclosed in Parentheses ()
# 2- You Can Remove The Parentheses If You Want
# 3- Tuple Are Ordered, To Use Index To Access Ite
# 4- Tuple Are Immutable => You Can not Add or Deletel
# 5- Tuple Items Is Not Unique
# 6- Tuple Can Have Different Data Types
# 7- Operators Used in Strings and Lists Available In Tuples

# Tuple Syntax & Type Test
tuple_1 = ("Python", "JS")
tuple_2 = "Python", "JS"
print(tuple_1) # ('Python', 'JS')
print(tuple_2) # ('Python', 'JS')
print(type(tuple_1)) # tuple
print(type(tuple_2)) # tuple


# Tuple Are Immutable 
tuple_1 = ("Python", "JS", "C++")

tuple_1[1] = "C#" # Error
# TypeE
