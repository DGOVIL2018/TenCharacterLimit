#Dhruv Govil 5/8/16 Period 2
#Average Rows and Columns Program
#Enhancement: Computes row and column averages for ANY n by n matrix. Check by changing the value of n in the main program.

from random import randint

def draw_matrix(grid):
    '''Prints a 4x4 matrix neatly'''
    for i in range(len(grid)):
        for k in range(4 * len(grid)+ 1): #prints a dotted line before each row. The number of dashes equals the number of values times 4 for formatting purposes
            print("-", sep='', end='') #zero separation between prints and no linefeed
        print()
        print("| ", sep='', end='')
        for j in range(len(grid)): #prints the values in row i
            print(grid[i][j], " | ", sep='', end='') 
        print()    
    for k in range(4 * len(grid)+ 1): #prints the last dotted line
            print("-", sep='', end='')
    print()

##### Main Program Here #####

n = 4 #set the dimensions of the matrix, in this case 4x4
grid = [[randint(0,9) for i in range(n)] for j in range(n)] #initialize a nxn list with random integers between 0 and 9
print("Initial random matrix.")
draw_matrix(grid) #print matrix

rowAverages = [0 for i in range(n)] #declare a list of size n to store row averages, and initialize them to 0
columnAverages = [0 for i in range(n)]
rowSums = [0 for i in range(n)]
columnSums = [0 for i in range(n)]

for i in range(n): #compute row and column sums using the grid
    for j in range(n):
        rowSums[i] += grid[i][j]
        columnSums[i] += grid[j][i]

for i in range(n): #compute row and column averages from the row and column sums, by dividing the sums by n
    rowAverages[i] = rowSums[i] / n
    columnAverages[i] = columnSums[i] / n

#print results
print("Row averages: ",rowAverages)
print("Column averages: ",columnAverages)

    
    
       
         
        
