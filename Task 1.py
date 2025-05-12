a= int(input('enter a value: '))

def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
result=factorial(a)
print("factorial of 5 is: ",result)
