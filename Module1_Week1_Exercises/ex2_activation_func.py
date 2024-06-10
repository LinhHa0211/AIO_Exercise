import math
def is_number(number):
    try:
        float(number)
    except ValueError:
        return False
    return True

def sigmoid(x):
    return 1/(1 + math.exp(-x))

def relu(x):
    if x <= 0:
        return 0
    else:
        return x
    
def elu(x, alpha = 0.01):
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x    

def exercise2():
    x = input('Input x = ')
    if not is_number(x):
        print(f'x must be a number')
    else:   
        x = float(x)
        func_name = input('Input activation Function (sigmoid|relu|elu): ')
        if func_name.lower() == 'sigmoid':
            print(f'sigmoid: f({x}) = {sigmoid(x)}')
        elif func_name.lower() == 'relu':
            print(f'relu: f({x}) = {relu(x)}')
        elif func_name.lower() == 'elu':
            print(f'elu: f({x}) = {elu(x)}')
        else:
            print(f'{func_name} is not supported')

exercise2()