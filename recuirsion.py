def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    
num = int(input("Enter a any number :"))
print ("The Factorial Of",num,"Is",factorial(num))