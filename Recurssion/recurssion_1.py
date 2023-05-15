# fibonacci series using recurssion

def fib(n):

    if n == 0:
        return 0

    if n == 1 or n == 1:
        return 1

    else:
        return fib(n-1) + fib(n-2)