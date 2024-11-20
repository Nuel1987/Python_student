a = 5
b = 0

#print(a/b)

try:
    print(a/b)
except NameError:
    print("Error: We can't divide a number by letter")
except Exception:
    print("Error: It isn't possible to divide number  by zero")
finally:
    print("This block will always execute")