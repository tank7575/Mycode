def add(a, b):
    print(">>> a=", a, "b=", b)
    print(f"ADDING {a} + {b}")
    print("<<< exit add")
    return a + b

def subtract(a, b):
    print(">>> a=", a, "b=", b)
    print(f"SUBTRACTING {a} - {b}")
    print("<<< exit subtract")
    return a - b

def multiply(a, b):
    print(">>> a=", a,  "b=", b)
    print(f"MULTIPLYING {a} * {b}")
    print("<<< exit multiply")
    return a * b

def divide(a, b):
    print(">>> a=", a, "b=", b)
    print(f"DIVIDING {a} / {b}")
    print("<<< exit divide")
    return a / b


print("Lets do some math with just functions!")

age = add(30, 5)
print(">>>> age=", age)
height = subtract(78, 4)
print(">>>> height=", height)
weight = multiply(90, 2)
print(">>>> weight=", weight)
iq = divide(100, 2)
print(">>>> iq=", iq)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anywayself.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
