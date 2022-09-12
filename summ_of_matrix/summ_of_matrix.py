line = str(input())
matrix = []
i = 0
while not(line == "end"):
    matrix.append([])
    for j in range(len(line.split())):
        matrix[i].append(int(line.split()[j]))

    i += 1
    line = str(input())
final_matrix = []
for i in range(len(matrix)):
    final_matrix.append([])
    for j in range(len(matrix[i])):
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
        print(final_matrix[i][j],  ' ', end='')
    print('\n', end='')
