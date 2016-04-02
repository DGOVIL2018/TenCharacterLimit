#0
def odd_even(number):

    numType = ""

    if number % 2 == 0:
        numType = "Even"
    
    else:
        numType = "Odd"

    return numType
#1
def number_digits(x):
    if x == 0:
        count = 0 #I am treating 0 as having no digits, because it is valueless
    else:
        count = 1
        while x > 0:
            x = x // 10
            if x != 0:
                count = count + 1
    return count
#2
def sum_digits(x):
    if x == 0:
        sum = 0 
    else:
        sum = 0
        while x > 0:
            sum = sum + (x % 10)
            x = x // 10
            
    return sum
#3
def sum_lessthan(x):
    if x == 0:
        sum = 0
        
    else:
        sum = 0
        for i in range(1,x):
            sum = sum + i
            
    return sum
#4
def factorial(x):
    if x == 0:
        f = 1
        
    else:
        f = 1
        for i in range(1,x+1):
            f = f*i
            
    return f
#5
#This program asks for two positive integers and tells if the second integer is a factor of the first integer
print("This program asks for two positive integers and tells if the second integer is a factor of the first integer.")

def factor(dividend,divisor):
  
    if dividend % divisor == 0: #condition to determine if divisor is a factor of the dividend
        return True
    else:
        return False
#6
def is_Prime(n):

    primeStatus = True

    if n == 2:
        primeStatus = True
    else:
        primeStatus = True
        for i in range(2, (n//2) + 1): #testing divisibility by numbers from 2 to half the number
            if n % i == 0:
                primeStatus = False

    return primeStatus
#7
def is_Perfect(n):

    sum = 0

    for i in range(1,(n//2)+ 1): #test for all possible proper factors of n
        if n % i == 0:
            sum = sum + i #increment sum variable by each proper factor value

    if n == sum:
        return True
    else:
        return False
#8
def factor(dividend,divisor):
  
    if dividend % divisor == 0: #condition to determine if divisor is a factor of the dividend
        return True
    else:
        return False

def sum_digits(x):
    if x == 0:
        sum = 0 
    else:
        sum = 0
        while x > 0:
            sum = sum + (x % 10)
            x = x // 10
            
