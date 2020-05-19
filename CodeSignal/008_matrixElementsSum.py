def matrixElementsSum(matrix):
    total_cost = 0

    rotated = tuple(zip(*matrix[::1]))
    for i in range(len(rotated)):
        for j in rotated[i]:
            if j == 0:
                break
            total_cost += j
    return total_cost


matrix = [[1, 1, 1, 1], [0, 5, 0, 1], [2, 1, 3, 10]]
matrix = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]
print(matrixElementsSum(matrix))
