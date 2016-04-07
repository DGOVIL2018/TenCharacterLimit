import ps0 #ps0.py file has to be in the same directory as this file
#0
print("\nTesting Program 0.")
print(0 , "is" , ps0.odd_even(0))
print(24 , "is" , ps0.odd_even(24))
print(5 , "is" , ps0.odd_even(5))

#1
print("\nTesting Program 1.")
print("The number of digits in", 43, "is" , ps0.number_digits(43))
print("The number of digits in", 0, "is" , ps0.number_digits(0))
print("The number of digits in", 345, "is" , ps0.number_digits(345))

#2
print("\nTesting Program 2.")

print("The sum of the digits in", 0, "is" , ps0.sum_digits(0))
print("The sum of the digits in", 654, "is" , ps0.sum_digits(654))    
print("The sum of the digits in", 21, "is" , ps0.sum_digits(21))

#3
print("\nTesting Program 3.")
print("The sum of integers less than", 3, "is" , ps0.sum_lessthan(3))
print("The sum of integers less than", 57, "is" , ps0.sum_lessthan(57))
print("The sum of integers less than", 0, "is" , ps0.sum_lessthan(0))
    

#4
print("\nTesting Program 4.")
print("The factorial of ", 0, "is" , ps0.factorial(0))
print("The factorial of ", 1, "is" , ps0.factorial(1))
print("The factorial of ", 5, "is" , ps0.factorial(5))

#5
print("\nTesting Program 5.")

x = 27
y = 3
if ps0.factor(x,y) == True:
    print(y, "is a factor of" , x)
else:
    print(y , "is not a factor of" , x)

x = 5
y = 3
if ps0.factor(x,y) == True:
    print(y, "is a factor of" , x)
else:
    print(y , "is not a factor of" , x)

x = 17
y = 3
if ps0.factor(x,y) == True:
    print(y, "is a factor of" , x)
else:
    print(y , "is not a factor of" , x)
#6
print("\nTesting Program 6.")
x = 2
if ps0.is_Prime(x) == True:
    print(x , "is prime")
else:
    print(x , "is not prime")

x = 21
if ps0.is_Prime(x) == True:
    print(x , "is prime")
else:
    print(x , "is not prime")

x = 53
if ps0.is_Prime(x) == True:
    print(x , "is prime")
else:
    print(x , "is not prime")
    
#7
print("\nTesting Program 7.")
x = 496
if ps0.is_Perfect(x) == True:
    print(x, "is a perfect number")
else:
    print(x, "is not a perfect number")

x = 1
if ps0.is_Perfect(x) == True:
    print(x, "is a perfect number")
else:
    print(x, "is not a perfect number")
#8
print("\nTesting Program 8.")
x = 9
if ps0.divide_by_FactorSum(x) == True:
    print("The sum of the digits of ",x, "evenly divides into", x)
else:
    print("The sum of the digits of ",x, "does not evenly divide into", x)

x = 13
if ps0.divide_by_FactorSum(x) == True:
    print("The sum of the digits of ",x, "evenly divides into", x)
else:
    print("The sum of the digits of ",x, "does not evenly divide into", x)

x = 21
if ps0.divide_by_FactorSum(x) == True:
    print("The sum of the digits of ",x, "evenly divides into", x)
else:
    print("The sum of the digits of ",x, "does not evenly divide into", x)
