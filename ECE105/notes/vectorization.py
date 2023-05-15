import timeit
import numpy as np
import matplotlib.pyplot as plt
import math
import random
"""
single program multiple data (SPMD) programming
we want f(array) -> each memeber of array is now e^a[i]

this can be processes in parallel (run instance of code in each of processing cores)
ECEC413

Heavyside step function f(x) = {1, x>=0; 0, x<0 }
failed attempt"""

def powerdeco(func):
    def wrapper():
        print("--------I AM AWAKE I AM POWERFUL I AM ME--------")
        func()
        print("--------I AM SLEEPING but im still me!--------")
    return wrapper 
def H(x: list):
    if x >= 0:
        return 1
    else:
        return 0


def where_showcase(n):
    print(n)
    print(np.where(n > 0, -2, 2))
'''timing
    big O notation
        ex bubble sort is O(n^2)
        ex quick sort is O(n)
'''
def factorial(num):
    return num * factorial(num-1) if num > 0 else 1
def swave(t):
    tOUT = np.floor(t)
    tOUT = np.mod(t,2)
    return tOUT
    
@powerdeco
def iAMhim():
    # ? what if we customize the class behavior for comparisons ?
    # ? isnt mod operator slow what about np.mod? are there bitmasks in python?
    # ? Is the set up for a paralleism typically worth it in the long run ?
    ax = plt.subplot(111)
    size = 10
    ori = np.linspace(0,size)
    x = np.round(ori)
    y = swave(x)
    print(ori)
    print(y)
    ax.plot(ori,y)
    # print(x,type(x))
    # print(y,type(y))
    plt.show()

if __name__ == "__main__":
    iAMhim()