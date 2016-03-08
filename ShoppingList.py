#Dhruv Govil Period 2 Feburary 27 2016
#Shopping List Program

#open the shoppinglist file
fo = open("ShoppingListFile.txt", "r")

shoppingList = []

#read the file into a list

for line in fo:
    
    if line != "\n":
        shoppingList.append(line)
   
fo.close()

if len(shoppingList) > 0:
    print("Here is your current shopping list: ")
    for i in range(1,len(shoppingList)+1):
        print(i, ".", shoppingList[i-1])
        
else:
    print("Your shopping list is empty")

#are you done loop start
status = "n"
while status == "n": 

#ask user what they want to do(add, delete)
    task = input("Enter 'a' to add or 'd' to delete items: ")
    if task == "a":      
        #add loop start
        while True:

            newItem = input("Enter next item please: ")
            if newItem == "":
                break
            else:
                
                if newItem != "\n":
                    shoppingList.append(newItem)
     #add loop end
    elif task == "d":

        #delete loop start
         while True:
             if len(shoppingList) > 0:
                     print("Here is your current shopping list: ")
                     for i in range(1,len(shoppingList)+ 1):
                         print(i, ".", shoppingList[i-1])
             else:
                     print("Your shopping list is empty")

             dIndex = int(input("Enter the number of the item you want to delete(0 if done): "))

             if dIndex == 0:
                 break
             else:
                 dItem = shoppingList[dIndex - 1]
                 shoppingList.remove(dItem)

             #delete loop end

    status = input("Are you done? y/n: ")

#are you done loop end
    
#display final list to user
if len(shoppingList) > 0:
    print("Here is your current shopping list: ")
    for i in range(1,len(shoppingList)+1):
        print(i, ".", shoppingList[i-1])
else:
    print("Your shopping list is empty")

#write list into the shopping list file
fo = open("ShoppingListFile.txt", "w")

for i in range(1,len(shoppingList)+1):
    
    if shoppingList[i-1] != "\n":
        fo.write(shoppingList[i-1] + "\n")
    

fo.close()

