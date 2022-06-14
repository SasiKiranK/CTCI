input = "tact coa"


def check_palindrome(input):
    dict1 = {}
    for i in input:
        if i != ' ':
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

    count = 0
    for key, value in dict1.items():
        if value % 2 != 0:
            count += 1

    if count > 1:
        return False
    return True


print(check_palindrome(input))
