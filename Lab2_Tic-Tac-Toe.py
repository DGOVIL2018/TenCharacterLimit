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


def check_Winning_Move(current_Board,move_Symbol):
    '''This function checks for an immediate winning move for the computer, and makes that move if it exists. If not, then it returns the existing board.
    This function also returns a boolean status noting if such a move was found.'''
    for i in range(1,10):
        x,y = n_to_xy(i)
        if current_Board[x,y] == " ":
            current_Board[x,y] = move_Symbol
            if is_win(current_Board):
                return True,current_Board
            else:
                current_Board[x,y] = " "
                
    return False,current_Board
    
def check_Blocking_Move(current_Board,move_Symbol):
    '''This function checks if the opponent has an immediate winning move, if not blocked. Used in AI(computer) mode in the AI_Move function'''

    if move_Symbol == "X":
        opponent_Symbol = "O"
    else:
        opponent_Symbol = "X"    

    for i in range(1,10): 
        x,y = n_to_xy(i)
        if current_Board[x,y] == " ":
            current_Board[x,y] = opponent_Symbol #put opponent symbol in the blank spot 
            if is_win(current_Board): #check if that makes the opponent win
                current_Board[x,y] = move_Symbol #if so, then move your symbol there
                return True,current_Board
            else:
                current_Board[x,y] = " " #if not a winning move for opponent, then reset that location to blank/open
                
    return False,current_Board


def AI_Move(currentBoard,symbol):
    '''This function looks for the best next move and returns the board after making that move'''
    
    win, newBoard = check_Winning_Move(currentBoard,symbol)
    if win: #check if an immediately winning move was found
        return newBoard

    block, newBoard = check_Blocking_Move(currentBoard,symbol)
    if block:
        return newBoard
       

    if currentBoard[1,1] == " ":
        move(currentBoard,symbol,5)
        return newBoard
    
    if currentBoard[0,0] == " ":
        return move(currentBoard,symbol,1)
    if currentBoard[0,2] == " ":
        return move(currentBoard,symbol,3)
    if currentBoard[2,0] == " ":
        return move(currentBoard,symbol,7)
    if currentBoard[2,2] == " ":
        return move(currentBoard,symbol,9)

    if currentBoard[0,1] == " ":
        return move(currentBoard,symbol,2)
    if currentBoard[1,0] == " ":
        return move(currentBoard,symbol,4)
    if currentBoard[1,2] == " ":
        return move(currentBoard,symbol,6)
    if currentBoard[2,1] == " ":
        return move(currentBoard,symbol,8)
    
 

### Main Program Here #####

board = { (i,j):" " for i in range(3) for j in range(3) }

# print instructions
for i in range(3):
    for j in range(3):
        board[i,j] = i*3 + j + 1

print("INSTRUCTIONS:\n\n")

draw_board(board)
        
print("Enter your moves using the numbers shown above to choose the corresponding location on the board.\n\n")


# Get mode, user names, symbols, and first mover

mode = input("Do you want to play against the computer? Y/N: ")
mode = mode.upper()

if mode == "Y": 
    
    P1 = input("Enter your name: ")
    P1S = input("Enter your symbol choice (X or O): ")
    Order = input("Will you move first? Y/N :")

    P2 = "Computer"
    P1S = P1S.upper()
    if P1S == "X":
        P2S = "O"
    else:
        P2S = "X"

    Order = Order.upper()
    if Order  == "N":
        temp = P1
        P1 = P2
        P2 = temp

else:
    
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

    if mode == "Y": #this section is for playing against the computer
        
        if currentPlayer != "Computer":
            valid = False
            while not valid:
                    print(currentPlayer, ", enter your move (1-9): ", end="")
                    boardLocation = int(input()) #How to use variable in input prompt?
                    print()
                    if is_valid(board, boardLocation):
                        board = move(board, currentSymbol, boardLocation)
                        valid = True
        else: #this is when it is the computer's turn
            print("Here is the Computer's move:\n")
            board = AI_Move(board, currentSymbol)
    else: #this section is for playing against another player
        valid = False
        while not valid:
            print(currentPlayer, ", enter your move (1-9): ", end="")
            boardLocation = int(input()) #How to use variable in input prompt?
            print()
            if is_valid(board, boardLocation):
                board = move(board, currentSymbol, boardLocation)
                valid = True        

       
    if is_win(board):
        print("Congratulations", currentPlayer, ". You have won!")
        draw_board(board)
        break

if not is_win(board):
    draw_board(board)
    print("The game is a tie!")
    
    



#Documentation
#I used eight different functions to simplify my code and therefore did not repeat code
#I found it challenging to code the part determining which player goes first, because it required the use of many variables
#I was confused on the part why initializing the playing board with three rows and three columns did not let me reference the 2D list by using list[x][y].
#I found it interesting that you can use multiple print statements to print a board without using fancy printing techniques
#I tried to make the game more user-friendly, so I asked the players their names and game-mode so that the game would be more enjoyable for them
#The AI function was complicated to define. I had to think through the sequence of checks that would make it smart. The order of priority was:
    #1: Make an immediate winning move if available
    #2: Block the opponent's immediate winning move, if possible
    #3: Play the center, as it controls four different lines (if possible)
    #4: Next, play the corners, as they control three different lines (if possible)
    #5: Lastly, play the sides, as they have the least value outside of the previous four (if possible)
    


