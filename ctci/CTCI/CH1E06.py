str_val = 'sshhs'
ch = str_val[0]
str2 = str_val
str_val = str_val + " "
counter = 0
compressed = ''
for i in str_val:
    if i == ch:
        counter += 1
    else:
        compressed = compressed + ch + str(counter)
        counter = 1
        ch = i
print(compressed)

i = 0
j = 0
result = ''
while (i < len(str2) - 1):
    i = j
    while j < len(str2) and str2[i] == str2[j]:
        j += 1
    result = result + str2[i] + str(j - i)
    # print(result)
print(result)
