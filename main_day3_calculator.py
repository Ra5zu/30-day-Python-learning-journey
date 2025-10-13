def add(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def multi(a, b):
    print(a * b)


def divide(a, b):
    print(a / b)


n1 = float(input("Input your first number:"))
op = input("Input your operation(+, -, *, /:)")
n2 = float(input("Input your second number:"))

if op == "+":
    add(n1, n2)
elif op == "-":
    sub(n1, n2)
elif op == "*":
    multi(n1, n2)
elif op == "/":
    if n2 == 0:
        print("Zero division error. Invalid input.")
    else:
        divide(n1, n2)
else:
    print("Invalid operation")
