data = [('test 1   ', 6), ('test ss   ', 7)
        ]


def urlify(string1, length):
    true_length = len(string1)
    for i in reversed(range(length)):
        if string1[i] == ' ':
            string1[true_length - 1] = 0
            string1[true_length - 2] = 2
            string1[true_length - 3] = '%'
            true_length -= 3
        else:
            string1[true_length - 1] = string1[i]
            true_length -= 1
    return string1


for i in data:
    print(urlify(list(i[0]), i[1]))
