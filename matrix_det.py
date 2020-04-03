def determinant(matrix):
    n = len(matrix)
    det = 0
    list_matrices = list()
    # base case
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix [1][1] - matrix[1][0] * matrix[0][1]
    
    # matrix reduction for next recursion
    idx_value = [i for i in matrix[0]]
    for x in range(n):
        list_matrices.append([(matrix[i][:x] + matrix[i][x+1:]) for i in range (1,n)])
    # recursion
    for i in range(n):
        if i % 2 == 0:
            sense = 1
        else:
            sense = -1
        add = sense * idx_value[i] * determinant(list_matrices[i])
        det += add
    return det

m1 = [ [1, 3], [2,5]]
print(determinant(m1))
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
print(determinant(m2))