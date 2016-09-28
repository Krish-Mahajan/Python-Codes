


import sys
sys.setrecursionlimit(1000000000)


# n_rooks_pieces.py : Solve the N-Rooks problem!
# Krishna Mahajan, September 2016
#
# N*N is the size of the board

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given col
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] ) 

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ " ".join([ "Q" if col else "_" for col in row ]) for row in board])

#Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col): 
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]
    

def add_piece2(board, row, col):
    
    #base case(if we reach N+1 rows in N*N board ,we'll get our first solution)
    from copy import deepcopy
    if row > len(board)-1:
        return board


    #check every col of the current row if its safe to place a piece
    while col < len(board):
        if is_valid(board, row, col):
            #place a piece
            board[row][col] = 1
            #place the next piece with an updated board
            return add_piece2(board, row+1, 0)
        else:
            col += 1
    
    #Backtrack((i,e. solution state from where no solution possible))
    for c in range(len(board)): 
        # removing piece from previous row
        if board[row-1][c] == 1:
                board[row-1][c] = 0
                #Resetting board to last row and last uncheked column
                return add_piece2(board, row-1, c+1)

def is_valid(board, row, col): 
    """ checking if the position to place new piece is valid """
    
    # Finding coordinates of each already places pieces in board
    pieces = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 1:
                piece = (r,c)
                pieces.append(piece)
    for piece in pieces:
        qr, qc = piece
        #check if the piece is in the same column or row as of prevously placed piece
        if row == qr or col == qc:
            return False
        
        if (S=="nqueens"):
            #check diagonals if nqueens problem
            if (row + col) == (qr+qc) or (col-row) == (qc-qr):
                return False
    return True


# Get list of successors of given board state
def successors(board):
    print("Getting successors board")
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N)]

#Succsessors2 method as asked in Q3
def successors2(board):
    print("Getting successors board")
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) if (count_pieces(board) < N and add_piece(board,r,c)!=board)]

def successors3(board):
    #add_piece2(initial_board,0,0)
    #return [ add_piece2(board, r, c) for r in range(0, N) for c in range(0,N) if (count_pieces(board) < N and add_piece(board,r,c)!=board)]
    return [ add_piece2(board, 0, 0) ]

#Checking if the solution_state=Goal_state
def is_goal(board):
    return count_pieces(board) == N and \
        all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
        all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )

# Solve n-rooks! (Prof. Crandall)
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors3( fringe.pop(0) ):
            if is_goal(s):
                return(s)
            fringe.append(s)
        print("Length of fringe is",len(fringe))
        print("No solution found..yet , Going to next successors states")    
        print("\n")
    return False

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.

N=input("Give the Value of n: ") 
N=int(N)
S=input("Which problem?type <'nrooks'> or <'nqueens'>: ")
print("\n")
initial_board = [[0 for i in range(N)] for i in range(N)] 
print("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")  
#successors3(initial_board)

solution = solve(initial_board)
print("********** Solution************")
print(printable_board(solution) if solution else "Sorry, no solution found. :(")











