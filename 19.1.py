__author__ = 'Topper121'

def f(n):
    a = 0
    if n == 1:
        return 6
    else:
        return 0.5 * f(n-1) + 4

for i in range(1,11):
    a = f(i)
    print("n = %i , a = %f" % (i, a))

def fibbo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)

for i in range(1,11):
    print(fibbo(i))