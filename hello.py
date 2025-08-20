# print("Hello")
# print("World")
# print("This is a Python script.")
# print("Goodbye")    
d=0
for a in range(1, 101):
    for b in range(a, 101):
        if a%3 == 0 :
            d= a**2 + b**2 
        for c in range(1, 101):
            if d == c**2:              
                print(a, b, c)