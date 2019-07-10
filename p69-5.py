def f(x):
    try:
        return float(x)
    except ValueError:
        print("Invalid input.")

y = f('a')
print(y)
