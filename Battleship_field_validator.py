def validate_battlefield(field):
    # field is a 10 x 10 matrix
    # check that ships are not in contact (diag included)
    # ignore number and type of ships
    
    # Check no diagonals
    adjacency = 0
    counter = 0
    for i in range(0,10):
        for j in range(0,10):
            if field[i][j] == 1:
                counter += 1
                if i in range(1,9) and j in range(1,9):
                    if field[i-1][j-1] == 1 or field[i-1][j+1] == 1 or field[i+1][j-1] == 1 or field[i+1][j+1] == 1:
                        return False
                # Check no column/row collisions by sum of natural adjacency (4 liner: 3 x 1 + 3 liner: 2 x 2 + 2 liner: 1x3)
                try:
                    if field[i][j+1] == 1:
                        adjacency += 1
                except: pass
                try:
                    if field[i+1][j] == 1:
                        adjacency += 1
                except: pass
    if adjacency != 10 or counter != 20:
        print(adjacency)
        return False          
    return True

field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
print(validate_battlefield(field))