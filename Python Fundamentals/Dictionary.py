# 1- Dict Items Are Enclosed in Curly Braces
# 2- Dict Items Are Contains Key : Value
# 3- Dict Key Need To Be Immutable => (Number, String, Tuple) 
#    List Not Allowedl
# 4- Dict Value Can Have Any Data Types
# 5- Dict Key Need To Be Unique
# 6- Dict Is Not Ordered You Access Its Element With Keyl

# 1D Dictionary
users = {
    "name" : "Python",
    "age" : 30,
    "country" : "USA",
    "skills" : ["C++", "Java"],
    "age" : 20
    # age:20 value will depend and 
    # the old age:30 will not depend
}

print(users)
# {'name': 'Python', 'age': 20, 'country': 'USA', 'skills': ['C++', 'Java']}

print(users["age"])     # 20
print(users.get("age")) # 20

print(users.keys())
# dict_keys(['name', 'age', 'country', 'skills'])

print(users.values())
# dict_values(['Python', 20, 'USA', ['C++', 'Java']])




# 2D Dictionary
languages = {
    "IOS" : {
        "name" : "swift",
        "Progress" : "40%"
    },
    "Android" : {
        "name" : "Java",
        "Progress" : "70%"
    },
    "Flutter" : {
        "name" : "Dart",
        "Progress" : "75%"
    }   
}

print(languages)
print(languages['IOS']) # {'name': 'swift', 'Progress': '40%'}
print(languages['IOS']['name']) # swift
print(languages['IOS']['Progress']) # 40%

# Dictionary Length
print(len(languages)) # 3
print(len(languages["Android"])) # 2
