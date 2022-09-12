line = str(input())
matrix = []
for i in range(len(line.split())):
    matrix.append([])
    for j in range(len(line.split())):
        matrix[i].append(int(line.split()[j]))