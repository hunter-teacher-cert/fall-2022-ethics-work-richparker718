
alive = 'X'
dead = '-'
   
def createNewBoard (rows,cols):
        board = [[' '] * (cols) for _ in range(rows)]
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                board[i][j] = '-'
                j += 1
            i += 1
        return board
   
def printBoard (board):
        i = 0
        while i < len(board):
            j = 0
            while j < len(board[i]):
                print(" " + str(board[i][j]), end ="")
                j += 1
            print()
            i += 1
   
def setCell (board,  r,  c,  val):
        board[r][c] = val
   
def countNeighbours (board,  r,  c):
        startR = r if (r - 1 < 0) else r - 1
        startC = c if (c - 1 < 0) else c - 1
        rowLim = r + 1 if (r + 1 > len(board) - 1) else r + 2
        colLim = c + 1 if (c + 1 > len(board[0]) - 1) else c + 2
        livingCt = 0
        row = startR
        while row < rowLim:
            col = startC
            while col < colLim:
                if not (row == r and col == c):
                   
                    if board[row][col] == 'X':
                        livingCt += 1
                col += 1
            row += 1
        return livingCt
    
def  getNextGenCell (board,  r,  c):
        nextGen = board[r][c]
        numNeighbours = countNeighbours (board, r, c)
        if board[r][c] == alive:
            if numNeighbours == 2 or numNeighbours == 3:
      
                nextGen = alive
            else :
                nextGen = dead
        else :
           
            if (numNeighbours == 3):
                nextGen = alive
            else :
                nextGen = dead
        return nextGen
   
def  generateNextBoard (board):
        newBoard = [[' '] * (len(board[0])) for _ in range(len(board))]
        i = 0
        while i < len(board):
            j = 0
            while j < len(board[0]):
                newBoard[i][j] = getNextGenCell(board, i, j)
                j += 1
            i += 1
        return newBoard




  
board = createNewBoard(5, 5)
setCell(board, 0, 0, 'X')
setCell(board, 0, 1, 'X')
setCell(board, 1, 0, 'X')
printBoard(board)
print("The cell is alive")
print(countNeighbours(board, 0, 0))
print("New Board:")
newBoard = generateNextBoard(board)
printBoard(newBoard)
    
