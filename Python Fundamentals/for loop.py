# For Loop
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index in myList :
    if index % 2 == 1 : # Even
        continue
    print(index)
# 2 4 6 8 10




# for loop with list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index in myList :
    if index % 2 == 0:
        print(f"{index} : Is Even")
    elif index %2 == 1:
        print(f"{index} : Is Odd")
    else:
        print(f"{index} : Not Recognised")

# 1  : Is Odd
# 2  : Is Even
# 3  : Is Odd
# 4  : Is Even
# 5  : Is Odd
# 6  : Is Even
# 7  : Is Odd
# 8  : Is Even
# 9  : Is Odd
# 10 : Is Even
