def matrices(matrix):
    
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    for row in matrix:
        print(row)


print("The output of 3x3 matrix is:")
matrices([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]])


print("\n")
print("The output of 4x4 matrix is:")
matrices( [[5, 1, 9, 11],
         [2, 4, 8, 10], 
         [13, 3, 6, 7], 
         [15, 14, 12, 16]])