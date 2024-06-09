import math

def is_number(number):
    try:
        float(number)
    except ValueError:
        return False
    return True

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(n-1) 

def approx_sin(x, n):
    total = 0
    for i in range(n):
        total += ((-1)**i) * ((x**(2*i + 1)) / (factorial(2*i + 1)))
    return total

def approx_cos(x, n):
    total = 0
    for i in range(n):
        total += ((-1)**i) * ((x**(2*i)) / (factorial(2*i)))
    return total

def approx_sinh(x, n):
    total = 0
    for i in range(n):
        total += ((x**(2*i + 1)) / (factorial(2*i + 1)))
    return total

def approx_cosh(x, n):
    total = 0
    for i in range(n):
        total += ((x**(2*i)) / (factorial(2*i)))
    return total

x = input('Input x = ')
n = input('Input n = ')

if (not is_number(x)) or (not is_number(n)):
    print('Input x and n must be numbers')
elif (not n.isnumeric()) or int(n) <= 0:
    print('Input n must be a integer and n must greater than 0')
else:
    x = float(x)
    n = int(n)
    print('approx_sin(x={x}, n={n}) =', approx_sin(x, n))
    print('approx_cos(x={x}, n={n}) =', approx_cos(x, n))
    print('approx_sinh(x={x}, n={n}) =', approx_sinh(x, n))
    print('approx_cosh(x={x}, n={n}) =', approx_cosh(x, n))