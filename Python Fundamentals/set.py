# ------------- set Rules -------------
# 1- Set Items Are Enclosed in Curly Braces
# 2- Set Items Are Not Ordered And Not Indexed
# 3- Set Indexing and Slicing Cant Be Don
# 4- Set Has Only Immutable Data Types (Numbers, Strings, Tuples) 
#    List and Dict Are Not
# 5- Set Items Is Unique

# Not Ordered And Not Indexed
set_1 = {"Python", "JS", 7}
print(set_1) # {7, 'JS', 'Python'}
print(set_1) # {'Python', 'JS', 7}
print(set_1) # {'JS', 'Python', 7}

# Slicing Cant Be Done
set_2 = {1, 2, 3, 4, 5, 6, 7}
# print(set_2[0:3]) # Error
# TypeError: 'set' object is not subscriptable

print("---------------------------")

# Set Items Is Unique
set_3 = {"JS", "JS", "C++", "Python"}
print(set_3) # {'Python', 'C++', 'JS'}
# will remove the element "JS" because it was repeated more than once
