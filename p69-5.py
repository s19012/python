def f(x):
    try:
        return float(x)
    except ValueError:
        print("Invalid input.")

y = f("10.0")
print(y)
