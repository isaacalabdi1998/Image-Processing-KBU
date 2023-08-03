def addation(x, y) :
    return x * y

print(addation(2, 4)) # 8
print(addation(4, 4)) # 16
print(addation(5, 5)) # 25


# 2.2 function with multiple Arguments 
# It accept unlimited Arguments

def say_hello(*languages) :
    for name in languages :
        print(f"Hello {name}")

say_hello("Python", "Java", "Js", "C++", "C") # will occur error
# Hello Python
# Hello Java
# Hello Js
# Hello C++
# Hello C
