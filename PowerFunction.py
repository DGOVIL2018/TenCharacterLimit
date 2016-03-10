#Dhruv Govil Period 2 March 8 2016
#Power Function Program

def power(base, exponent):
    #test whether inputs are valid integers
    if (base % 1 == 0) and (exponent % 1 == 0) and (exponent >= 0) and (base != 0 or exponent != 0):
        
        answer = 1 #initialize answer for exponent = 0
        
        for i in range(1, exponent + 1):
            answer = answer * base

        return answer

    else:
        return False

#####MAIN PROGRAM BEGINS HERE#####

while True:

    b = (input("Enter an integer base: "))
    e = (input("Enter a non-negative integer exponent: "))
    b = int(b)
    e = int(e)

    result = power(b,e)
    if result == False:
        print("Please enter an integer base and a non-negative integer exponent")
    else:
        print(result)
        
    decision = input("Do you want to continue y/n : ")
    if decision != "y":
        break
    

    
