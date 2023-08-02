def say_hello(n1, n2, n3, n4) :
    languages = [n1, n2, n3, n4]
    for name in languages :
        print(f"Hello {name}")

say_hello("Python", "Java", "Js", "C++")
# say_hello("Python", "Java", "Js", "C++", "C") # will occur error
# Hello Python
# Hello Java
# Hello Js
# Hello C++
