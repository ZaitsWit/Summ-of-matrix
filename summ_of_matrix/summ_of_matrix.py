matrix = []
while True:
    enter = [i for i in input().split()]
    if enter == ["end"]:
        break
    matrix.append(enter)

final_matrix = []
for i in range(len(matrix)):
    final_matrix.append([])
    for j in range(len(matrix[i])):
        final_matrix[i].append(0)
        if i > 0:
            final_matrix[i][j] += int(matrix[i - 1][j])
        else:
            final_matrix[i][j] += int(matrix[- 1][j])
        if i == len(matrix) - 1:
            final_matrix[i][j] += int(matrix[0][j])
        else:
            final_matrix[i][j] += int(matrix[i + 1][j])
        if j > 0:
            final_matrix[i][j] += int(matrix[i][j - 1])
        else:
            final_matrix[i][j] += int(matrix[i][- 1])
        if j == len(matrix[i]) - 1:
            final_matrix[i][j] += int(matrix[i][0])
        else:
            final_matrix[i][j] += int(matrix[i][j + 1])
        print(final_matrix[i][j],  ' ', end='')
    print()