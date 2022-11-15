print("A")
try:
    result = 5 + 5
    print("B")
except ValueError:
    print("C")
except TypeError:
    print("D")
else:
    print("E")
print("F")