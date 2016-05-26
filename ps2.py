#Dhruv Govil Period 2 May 23 2016
#Problem Set 2

#0
def insertion_sort(List):
    '''Takes list parameter and returns sorted version of list'''
    l = len(List)
    if len(List) == 0:
        return List
    for i in range(1,l): #loop to insert the ith number of the list into the sorted portion
        hand = List[i] #hand temporarily stores the current number, as it will get overwritten by the shift
        for j in range(i-1,-1,-1): #compare the ith number to each number before it
            if hand < List[j]:
                List[j+1] = List[j] #if a number on the left side is bigger than the current number, then move it to the right
            else:
                List[j+1] = hand #if a number on the left is smaller than the current number, then put the current number after it
                break
            if j == 0: #if no number smaller than the current unsorted number found, then the unsorted number goes into the first place
                List[j] = hand

                
    return List
    
List = [6,5,4,3,2,1]
print(insertion_sort(List))
List = [0,0,0,0]
print(insertion_sort(List))
List = [-5,-8,-20,5,13]
print(insertion_sort(List))
List = [-5]
print(insertion_sort(List))
List = []
print(insertion_sort(List))


#1

def add_variable(L1, L2):
    '''Takes two lists and returns a list that
    contains the result of adding the two parameters
    together. '''
    len1 = len(L1)
    len2 =len(L2)
    len3 = max(len1,len2)+1 # L3 will store the sum and its length has to be 1 more than max of input strings due to final carry
    L3 = []
    L1P = [] # Created to store L1 with zeros padded on the left. helps implement simple digit summation loop
    L2P = []
    for i in range(len3): # initialize lists to output length
        L3.append(0)
        L1P.append(0)
        L2P.append(0)

    for i in range(len1):
        L1P[len3-1-i] = L1[len1-1-i]

    
    for i in range(len2):
        L2P[len3-1-i] = L2[len2-1-i]
 
        
    carry = 0
    for i in range(len3-1,-1,-1):
        sumDigit = (L1P[i] + L2P[i] + carry)
        L3[i] = sumDigit % 10
        carry = sumDigit // 10

    for i in range(len3): # remove left padded zeros
        if L3[i] == 0:
            del L3[i]
        else:
            break

    return L3

L1 = [2,3,4,5]
L2 = [1,2,3,4]
print(add_variable(L1,L2))
      
L1 = []
L2 = []
print(add_variable(L1,L2))

L1 = [9,5,6,7]
L2 = [7,8,1]
print(add_variable(L1,L2))


#2

def alpha_string(message):
    '''this function take a string and returns only alphabets and spaces while removing other character'''
    alphaMessage = ""
    for char in message:
        if ord(char) <= 90 and ord(char) >=65 or ord(char) <= 122 and ord(char) >= 97 or char == ' ':
            alphaMessage += char
    alphaMessage += ' '
    return alphaMessage        
            
            
def spam_filter(messages, badWords):
    '''this function takes a list of message strings and a list of bad words. It returns the list of messages after removing the messages that contain any bad word from the list'''
    cleanMessages = [] # delare and initialize the list of messages to be returned. bad ones will be remved the code
    for i in range(len(messages)):
        cleanMessages.append(messages[i])
        
    for i in range(len(messages)): # for each message string
        alphaMessage = alpha_string(messages[i]) # clean the string
        alphaList = [] # put space separated words from string int a word list
        word = ""
        for char in alphaMessage: 
            if char != ' ':
                word += char
            else:
                alphaList.append(word)
                word = ""    
        for j in range(len(badWords)): # compare each word in the badWords list to the list of words in the message
            for k in range(len(alphaList)):
                if badWords[j].upper() == alphaList[k].upper():
                    cleanMessages.remove(messages[i]) # if bad word found then remove that message from the cleanMessage lsit
                    break
            
    return cleanMessages


badWords = ["bad", "Shit"]
messages = ["He is %!*#Bad karma", "I am good", "You are OK", "The Project went to SHIT!", "Badminton" ]
print(spam_filter(messages,badWords),"\n\n")

#3

def merge_list(List1, List2):
    '''Takes two sorted lists as paremeters and merges them into one sorted list'''
    ListM = [] # merged list declared
    L1 = len(List1)
    L2 = len(List2)
    i=0
    j=0
    k=0
    while k <= L1+L2: #while the merged list is not fully populated
        while i < L1 and j != L2 : #while we haven't gone through all the elements of List1, and List2 is not complete
            while j < L2 and  i!= L1 : #while we haven't gone through all the elements of List2, and List1 is not complete
                if List1[i] <= List2[j]:
                    nextNumber = List1[i] #assign the lower of the current number between the two lists to next number
                    i+=1
                else:
                    nextNumber = List2[j]
                    j+=1
                ListM.append(nextNumber) #append the next number to merged list
                k+=1
        #when one list is exhausted, append remaining numbers from other list to the output list        
        if i == L1:
            if j < L2:
                nextNumber = List2[j]
                ListM.append(nextNumber)
                j+=1
        if j == L2:
            if i < L1:
                nextNumber = List1[i]
                ListM.append(nextNumber)         
                i+=1
        k+=1 

    return ListM

List1 = [1,3,5,7,9,11]
List2 = [1,2,4,6,8,9,10]
print(merge_list(List1,List2),"\n\n")

#4

def is_fib(s):
    L = len(s)
    
    if s[0] != 0:
        return False

    if L == 1:
        return True
    else:
        if s[1] != 1:
            return False
    if L == 2:
        return True
       
    for i in range(2,L):
        if s[i] != s[i-1] + s[i-2]:
            return False

    return True

S1 = [0]
if is_fib(S1):
    print(S1, "is fibonacci\n\n")
else:
    print(S1, "is NOT fibonacci\n\n")
    
S1 = [0,1]
if is_fib(S1):
    print(S1, "is fibonacci\n\n")
else:
    print(S1, "is NOT fibonacci\n\n")

S1 = [0,1,1,2,3,5,8,13]
if is_fib(S1):
    print(S1, "is fibonacci\n\n")
else:
    print(S1, "is NOT fibonacci\n\n")

S1 = [1,2,4,6,8,9,10]
if is_fib(S1):
    print(S1, "is fibonacci\n\n")
else:
    print(S1, "is NOT fibonacci\n\n")

#5

def word_freq(fileName):
    '''Takes fileName and returns the frequency of each word in that file'''
    ch = open(fileName, 'r')
    Dict = {}
    while True:
        blank = False
        word = ""
        while blank == False:
            char = ch.read(1)

            if char == ' ' or char == '':
                blank = True
                break
            else:
                word += char
        
        if word in Dict.keys():
            Dict[word] = Dict[word] + 1
        else:
            Dict[word] = 1
        if char == '':
            break
            
        
    ch.close()
    return Dict

fileName = "Input5.txt"
print(word_freq(fileName))


#6

def ten_greatest(Dict):
    '''returns the keys with the top ten values'''
    keyList = [k for k in Dict.keys()]
    valList = [k for k in Dict.values()]
    L =len(valList)
    topTen = []
    m=0
    for K in range(min(10,L)):
        maxVal = 0
        for i in range (L-m):
            if int(valList[i]) > maxVal:
                maxVal = int(valList[i])
                maxIndex = i
        
        topTen.append(keyList[maxIndex])
        del valList[maxIndex]
        del keyList[maxIndex]
        m+=1

    return topTen

        
Dict = word_freq(fileName) # uses the filename from problem 5 and the function word_freq() from problem 5
print(ten_greatest(Dict))

#7 
def validate_5k(Tup) :
    Dict = dict(Tup)
    removeList = []
    for key in Dict:           
        if len(key) <= 2 or Dict[key] > 60:
            removeList.append(key)
    for name in removeList:
        del Dict[name]
    return Dict

Tup = (("AAAA",2.3),("BBBB",63.5),("C", 3.2))
print(validate_5k(Tup))









    
        
#8

def XOR(L1,L2):
    commonList = []
    XOR_list = []
    for i in range(len(L1)):
        for j in range(len(L2)):
            if L1[i] == L2[j]:
                common = L1[i]
                commonList.append(common)

    for i in range(len(L1)):
        include = True
        for k in range(len(commonList)):
            if L1[i] == commonList[k]:
                include = False
                break
        if include:
                XOR_list.append(L1[i])
        
    for i in range(len(L2)):
        include = True
        for k in range(len(commonList)):
            if L2[i] == commonList[k]:
                include = False
                break
        if include:
                XOR_list.append(L2[i])

    return XOR_list

L1 = [1,3,5,6,9,12]
L2 = [1,2,5,7,9,10]
print("XOR of ", L1, "and ", L2, "Is ", XOR(L1,L2),"\n\n")
                       









                   
