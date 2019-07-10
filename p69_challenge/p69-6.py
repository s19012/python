def f(x):
    '''
    Returns x ** 2.
    :param x: int.
    '''
    return x ** 2

print(f(2))


def f(string):
    '''
    :param string: str.
    '''
    print(string)

f("Hello")



def f(x, y, z, a=10, b=11):
    '''
    :param x, y, z, a, b: int.
    '''
    return x + y + z + a + b

result = f(1, 2, 3)
print(result)



def divi(x):
    '''
    :param x: int.
    :return x / 2
    :return x * 4
    '''
    return x / 2

def mul(x):
    return x * 4

y = divi(4)
z = mul(y)

print(z)



def f(x):
    '''
    :param x: str.
    '''
    try:
        return float(x)
    except ValueError:
        print("Invalid input.")

y = f("10.0")
print(y)
