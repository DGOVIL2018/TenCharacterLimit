#Author: Dhruv Govil
#0
def get_gcf(n1,n2):
    '''This function takes two positive integer arguments and returns their greatest common factor'''
    
    new_Factor = 1
    Flag = 0 #to keep track if no factor is found during the loop
    for i in range(2, min(n1,n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            new_Factor = i
            Flag = 1
            break
                
    if Flag == 0:#if no factor is found, then we are done
        return 1 #GCF is 1 when there is no common factor
    if Flag == 1:
        return new_Factor * get_gcf((n1//new_Factor),(n2//new_Factor)) #returns the current factor times the common factors of the remaining quotients


#0--Alterate: Explicitly stored prime factors of each in lists, then compared list for common factors
def prime_factors(m,pl):
    '''This function takes a positive integer argument m and returns a list of its prime factors'''
    primeList = pl
    if m == 1: #terminating case
        return []
    for i in range(2, m+1): #when the lowest factor is found, then break
        if m % i == 0:
            break
    
    primeList.append(i) #append the lowest factor to the prime list
    return primeList + prime_factors(m//i,[]) #return the prime factors found plus the prime factors of the remaining quotient via recursive call 
    #note that the prime_factors function returns the factors in ascending order
            


def get_gcf_alt(L1,L2):
    '''This function takes two positive integer arguments and returns their greatest common factor'''
    new_Factor = 1
    Flag = 0
    for i in range(0, len(L1)):
        for j in range(0, len(L2)):
            if L1[i] == L2[j]:        #if a common factor is found, then store it in new factor, and flag that a factor was found
                new_Factor = L1[i]
                k = i #using 
                l = j
                Flag = 1
                break
    if Flag == 0: #if no factor is found, then we are done
        return 1 #GCF is 1 when there is no common factor
    if Flag == 1:
        del L1[k]
        del L2[l]
        return new_Factor * get_gcf_alt(L1, L2) #return the current factor times the common factors in the remaining lists
    








#1

# This program takes 4 integer inputs and prints the largest of the 4 numbers

def largest(w,x,y,z):
    '''Takes four numbers and returns the largest value'''
    Li = [w,x,y,z] #read the parameters into list
    Max = Li[0]
    for i in range(1, len(Li)):
        if Li[i] > Max:
            Max = Li[i]
    return Max


2
import random

def magic_eight_ball():
    '''Takes no parameters. Answers any user question with a witty response. '''
    List = ["Looks Doubtful.","The Answer is Yes.","You Wish.","Perhaps.","There are Questions, More Questions, and No Answers.","Unlikely.","Definetly.","Curiosity Killed the Cat.","Ignorance is Bliss."]
    random_Index = int((9 * random.random()) // 1) #generate random number(0,10) and integer divide by one to get integer between[0,9]
    return List[random_Index]



#3
def ascii_name():
    '''Stores how name will print into a string with linefeeds, and returns a printable string'''
    D1 = "D D    "
    D2 = "D   D  "
    D3 = "D    D "
    D4 = "D    D "
    D5 = "D    D "
    D6 = "D   D  "
    D7 = "D  D   "
    D8 = "D D    "
    H1 = "H    H "
    H2 = "H    H "
    H3 = "H    H "
    H4 = "H    H "
    H5 = "HHHHHH "
    H6 = "H    H "
    H7 = "H    H "
    H8 = "H    H "
    R1 = "RRRRR  "
    R2 = "R    R "
    R3 = "R    R "
    R4 = "R   R  "
    R5 = "RRRR   "
    R6 = "R   R  "
    R7 = "R    R "
    R8 = "R    R "
    U1 = "U    U "
    U2 = "U    U "
    U3 = "U    U "
    U4 = "U    U "
    U5 = "U    U "
    U6 = "U    U "
    U7 = "U    U "
    U8 = " UUUU "
    V1 = "V   V "
    V2 = "V   V "
    V3 = "V   V "
    V4 = "V   V "
    V5 = "V   V "
    V6 = "V   V "
    V7 = " V V  "
    V8 = "  V   "
    nameString = D1+H1+R1+U1+V1+ '\n' + D2+H2+R2+U2+V2+ '\n' + D3+H3+R3+U3+V3+ '\n' +  D4+H4+R4+U4+V4+ '\n' + D5+H5+R5+U5+V5+ '\n' + D6+H6+R6+U6+V6+ '\n' +D7+H7+R7+U7+V7+ '\n' + D8+H8+R8+U8+V8+ '\n' 
    return nameString



#4 Alternate
#I interpreted this problem to require sorting ALL characters of the concatenated string, hence I used bubble sort.
#I Re-did this in 4b with positioning the whole words based on the dictionary sort of words

def alpha_order_alt(s1,s2):
    '''Takes two string parameters and returns the characters in the concatenated string in sorted order'''
    string = s1 + s2
    string = string.upper()
    charList = []
    for i in range(0, len(string)):
        charList.append(string[i])
    #the following nested loop implements bubble sort
    for i in range(0, len(charList)-1):
        for j in range(0, len(charList)-1):
            if charList[j] > charList[j+1]:
                temp = charList[j+1]
                charList[j+1] = charList[j]
                charList[j] = temp

    sortedString = ""
    for i in range(0,len(charList)):
        sortedString += str(charList[i])
    return sortedString

#4

def alpha_order(s1,s2):
    '''Takes two strings as parameters and returns a string with the two words in dictionary order, separated by a space'''
    Len1 = len(s1)
    Len2 = len(s2)
    if Len1 == 0 or Len2 == 0: #if one or both strings are null, then return the null or non-null string with no spaces
        return s1 + s2
    for i in range(0, min(Len1,Len2)): #only compare character positions of the smaller string, with the same positions in the longer string
        if s1[i].upper() > s2[i].upper(): 
            ls = s1  #ls stores the bigger alpha-string
            ss = s2  #ss stores the lesser alpha-string
            break
        elif s1[i].upper() < s2[i].upper(): #compare uppercase versions of each character, so that case is ignored in determining alpha-order
            ls = s2
            ss = s1
            break
       
    return ss + " " + ls #return concatenated string with original strings in alpha order, separated by a space





#5

def zip_strings(s1,s2):
    '''Takes two string parameters and returns a string with interleaved characters'''
    Len_s1 = len(s1)
    Len_s2 = len(s2)
    if Len_s1 > Len_s2: #the longer length is stored in LL, and the shorter length is stored in SL
        LS = s1         #the longer string is stored in LS
        LL = Len_s1
        SL = Len_s2
    else:
        LS = s2
        LL = Len_s2
        SL = Len_s1
    Zs = "" #the target string Zs is initialized to null 
    for i in range(0,SL): #the characters up to SL are assembled alternately into Zs
        Zs += s1[i] + s2[i]
    for i in range(SL,LL): #the remaining characters of LS are appended to Zs
        Zs += LS[i]
    return Zs


        

#6

def every_other(s):
    '''Takes string parameter and returns a string with every alternate character starting with the first'''
    LS = len(s)
    OS = ""
    for i in range(0, LS):
        if i % 2 == 0: #append every even indexed character starting with 0
            OS += s[i]
    return OS



#7

def count_lower(s):
    '''Takes string as parameter and returns the number of lowercase letters in it'''
    lowercaseCount = 0
    for i in range(0,len(s)):
        if s[i].isalpha(): #if alpha character, then check if it is lowercase and increment count
            if s[i].islower():
                lowercaseCount += 1
    return lowercaseCount
    




#8

def x_cipher(s):
    '''Takes string parameter and returns decoded text'''
    PT = "" #initializing the plain text target string
    for i in range(1,len(s)): #test if second character onwards should be written to the plain text
        if s[i-1].lower() == 'x':
            PT += s[i]

    return PT




###Documentation###
#Some of the specifications were ambigous, so I wrote a couple of alternative versions
#I was unclear on and struggled with problem 3. Am I supposed to use fancy printing techniques?
#The Magic Eight program was fun
#Most problems seemed like they had useful real world apllications

        
    
