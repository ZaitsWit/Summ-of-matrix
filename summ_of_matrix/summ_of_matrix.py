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
        final_matrix[i].append(int(matrix[i - 1][j]) + int(matrix[i + 1 - len(matrix)][j]) + int(matrix[i][j - 1]) + int(matrix[i][j + 1 - len(matrix[i])]))
        print(final_matrix[i][j],  ' ', end='')
    print()