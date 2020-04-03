def sudoku(board):
    # Pre-defining lists
    clone = [x[:] for x in board]
    rows = [x[:] for x in clone]
    columns = list(map(list,zip(*clone)))
    squares = list()  
    check = set(i for i in range(1,10))
    
    # filling the list squares:
    for x in range(9):
        temp = list()
        for i in range(2,-1,-1):
            for j in range(2,-1,-1):
                temp.append(clone[i].pop(j))
            if not clone[i]:
                clone.pop(i)
        squares.append(temp)
    
    # Solving sudoku
    doomcount = sum(board[i].count(0) for i in range(9))
    while doomcount > 0:
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    continue
                sq_idx = ((i // 3) * 3) + (j // 3)
                sq_id = ((i % 3) * 3) + (j % 3)
                numbers_found = set(rows[i] + columns[j] + squares[sq_idx])
                number = list(check.difference(numbers_found))      
                if len(number) == 1:
                    board[i][j] = number.pop()
                    rows[i][j], columns[j][i], squares[sq_idx][sq_id] = board[i][j] , board[i][j], board[i][j]
                    doomcount += -1
                    continue

    return board == solution

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

test = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [3,4,5,2,8,6,1,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]


print(sudoku(puzzle))
