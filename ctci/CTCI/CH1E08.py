first_row = False
first_col = False
data = [
    [1, 2, 3, 4, 0],
    [6, 0, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 0, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
n = len(data)
for i in range(n):
    if data[i][0] == 0:
        first_col = True
for i in range(len(data[0])):
    if data[0][i] == 0:
        first_row = True;

print(first_row, first_col)

for i in range(1, n):
    for j in range(1, len(data[0])):
        if data[i][j] == 0:
            data[i][0] = 0
            data[0][j] = 0

for i in range(n):
    if data[i][0] == 0:
        for j in range(1, n):
            data[i][j] = 0

for i in range(len(data[0])):
    if data[0][i] == 0:
        for j in range(1, n):
            data[j][i] = 0

if first_col:
    for i in range(n):
        data[i][0] = 0

if first_row:
    for i in range(len(data[0])):
        data[0][i] = 0

# print(data)
# for i in data:
#     print(i)
#     print('\n')

data = [
    [1, 2, 3, 4, 0],
    [6, 0, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 0, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

row = set()
col = set()
for i in range(n):
    for j in range(len(data[0])):
        if data[i][j] == 0:
            row.add(i)
            col.add(j)

for i in row:
    for j in range(len(data[0])):
        data[i][j] = 0

for i in col:
    for j in range(n):
        data[j][i] = 0

# print(row)
# print(col)
for i in data:
    print(i)
    print('\n')
