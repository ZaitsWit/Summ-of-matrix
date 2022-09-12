line = str(input())
matrix = []
for i in range(len(line.split())): ##while
    matrix.append([])
    for j in range(len(line.split())):
        matrix[i].append(int(line.split()[j]))

    line = str(input())
final_matrix = []
for i in range(len(matrix)):
    final_matrix.append([])
    for j in range(len(matrix)):
        final_matrix[i].append(0)
        if i > 0:
            final_matrix[i][j] += matrix[i - 1][j]
        else:
            final_matrix[i][j] += matrix[- 1][j]
        if i == len(matrix) - 1:
            final_matrix[i][j] += matrix[0][j]
        else:
            final_matrix[i][j] += matrix[i + 1][j]
        if j > 0:
            final_matrix[i][j] += matrix[i][j - 1]
        else:
            final_matrix[i][j] += matrix[i][- 1]
        if j == len(matrix[i]) - 1:
            final_matrix[i][j] += matrix[i][0]
        else:
            final_matrix[i][j] += matrix[i][j + 1]