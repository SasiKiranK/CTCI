data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
# data_new = data

n = len(data)
ans = []

# for i in range(n):
#     for j in range(n - 1, -1, -1):
#         print(j)
#         # ans[i].append(data[j, i])

for i in range(n):
    for j in range(i, n, 1):
        # print(i, j)
        temp = data[i][j]
        data[i][j] = data[j][i]
        data[j][i] = temp
print(data)

for i in range(n):
    for j in range(0, 3, 1):
        temp = data[i][j]
        data[i][j] = data[i][n - j - 1]
        data[i][n - j - 1] = temp
print(data)

data_new = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
ans = [[

]]

# print(data_new[4][0])
print(data_new)
for i in range(n):
    for j in range(n - 1, -1, -1):
        # print(i)
        ans[i].append(data_new[j][i])
        # print(data_new[j][i])
print(ans)
