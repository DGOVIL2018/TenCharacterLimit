import math

def draw_board(grid):
    '''Prints the current board'''
    print(grid[0,0]," | ",grid[0,1]," | ",grid[0,2])
    print("--------------")
    print(grid[1,0]," | ",grid[1,1]," | ",grid[1,2])
    print("--------------")
    print(grid[2,0]," | ",grid[2,1]," | ",grid[2,2])
    print()

def is_win(g):
    '''Checks whether a player has won'''
    win = False
    for i in range(3):
        if (g[i,0] == g[i,1] and g[i,1] == g[i,2]) and g[i,0] != " ":
            win = True
        if (g[0,i] == g[1,i] and g[1,i] == g[2,i]) and g[0,i] != " ":
            win = True
    if (g[0,0] == g[1,1] and g[1,1] == g[2,2]) and g[1,1] != " ":
            win = True
    if (g[0,2] == g[1,1] and g[1,1] == g[2,0]) and g[1,1] != " ":
            win = True

    return win

def n_to_xy(n):
    '''Converts place markers on board to coordinates where an 'X' or 'O' is to be placed'''
    x = math.ceil(n/3) -1
    if n % 3 == 0:
        y = 2 
    else:
        y = n % 3 -1
    return x,y

def move(currentBoard,symbol,n):
    '''Adds 'X' or 'O' to where user specifies to and returns the newBoard'''
    newBoard = currentBoard
    x,y = n_to_xy(n)
    newBoard[x,y] = symbol

    return newBoard

def is_valid(g, n):
    '''Checks whether the location the user wants to add an 'X' or 'O' to is valid'''

    x,y = n_to_xy(n)
    
    if n not in [1,2,3,4,5,6,7,8,9]:
        return False
    elif g[x,y] != " ":
        return False
    else:
        return True


#def AI():
#    if currentPlayer ==
##### Main Program Here #####

board = { (i,j):" " for i in range(3) for j in range(3) }

# print instructions
for i in range(3):
    for j in range(3):
        board[i,j] = i*3 + j + 1

print("INSTRUCTIONS:\n\n")

draw_board(board)
        
print("Enter your moves using the numbers shown above to choose the corresponding location on the board.\n\n")


# Get user names, symbols, and first mover

P1 = input("Enter the name of Player1: ")
P2 = input("Enter the name of Player2: ")
P1S = input("Enter Player1's symbol (X or O): ")
P1S = P1S.upper()
if P1S == "X":
    P2S = "O"
else:
    P2S = "X"

Order = input("Will Player1 move first? Y/N :")
Order = Order.upper()

if Order  == "N":
    temp = P1
    P1 = P2
    P2 = temp


# Initialize board
for i in range(3):
    for j in range(3):
        board[i,j] = " "

# Loop through the game

for i in range(9):
    j = i + 1
    draw_board(board)
    if j % 2 == 0:
        currentPlayer = P2
        currentSymbol = P2S
    else:
        currentPlayer = P1
        currentSymbol = P1S    

    valid = False
    while not valid:
        print(currentPlayer, ", enter your move (1-9): ", end="")
        boardLocation = int(input()) #How to use variable in input prompt?
        if is_valid(board, boardLocation):
            board = move(board, currentSymbol, boardLocation)
            valid = True
    

    if is_win(board):
        print("Congratulations", currentPlayer, ". You have won!")
        draw_board(board)
        break

if not is_win:
    print("The game is a tie!")
    
    



#Documentation
#I used five different functions to simplify my code and therefore did not repeat code
#I found it challenging to code the part determining which player goes first, because it required the use of many variables
#I was confused on the part why initializing the playing board with three rows and three columns did not let me reference the 2D list by using list[x][y].
#I found it interesting that you can use multiple print statements to print a board without using fancy printing techniques
#I tried to make the game more user-friendly, so I asked the players their names so that the game would be more enjoyable for them


