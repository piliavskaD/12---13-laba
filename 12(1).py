import math as m

def f(x):
    return m.pow(m.e, x) + 4 * m.pow(x, 2) - 7

def tab(f, a, b, h):
        
    x = a
    for i in range(a, b+1):
        y = f(x)
        print(format(y, ".3f"))
        x += h

a = int(input("a: "))
b = int(input("b: "))
h = int(input("h: "))        

tab(f, a, b, h)
