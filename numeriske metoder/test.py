import math
import numpy as np
import time
i = lambda x: 1/math.cos(x**2)+10

def solve(a,b,f,steps=10000,tol=1E-8):
    x_values = np.linspace(a,b,steps)
    step = (b-a) / steps
    intervals = []
    solutions = []
    for x in x_values[:-1]:
        if f(x) * f(x+step) > 0:
            pass
        elif abs(f(x) * f(x+step)) == 0:
            if f(x) == 0:
                solutions.append(x)
        else:
            #print(f'f(x) = {f(x)}, f(x+1) = {f(x+step)}')
            intervals.append([x,x+step])
    for interval in intervals:
        a = interval[0]
        b = interval[1]
        m = (a+b)/2
        while abs(f(m)) >= tol:
            if f(a)*f(m) < 0:
                b = m
            elif f(b)*f(m) < 0:
                a = m
            m = (a+b)/2
        solutions.append(round(m,5))
    return solutions

tid = time.time()
print(solve(-1000,1000,i,10000))
print(f'det tokk: {time.time()-tid}')