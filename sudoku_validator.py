def valid_solution(board):
    check = set(i for i in range(1,10))
    rows = [x[:] for x in board]
    columns = [zip(*board)]
    squares = list()    
    # filling the list squares:
    for x in range(9):
        temp = list()
        for i in range(2,-1,-1):
            for j in range(2,-1,-1):
                temp.append(board[i].pop(j))
            if not board[i]:
                board.pop(i)
        squares.append(temp)
    print(rows)
    print(columns)
    print(squares)
    # check if valid:
    for i in range(0,9):
        if check.issubset(rows[i]) and check.issubset(columns[i]) and check.issubset(squares[i]):
            continue
        else: return False
    return True

board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]

print(valid_solution(board))