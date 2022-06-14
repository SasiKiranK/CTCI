def check_edit_away(str1, str2):
    s1 = len(str1)
    s2 = len(str2)

    if abs(s1 - s2)>1:
        return False

    if s1 == s2:
        count = 0
        for i in range(s1):
            if str1[i] != str2[i]:
                count += 1
            if count == 1 or 0:
                return True
        return False

    count = 0
    if s1>s2:
        for
        if str1[]
        return False
    else:

    return True


input = [('pale', 'pal'), ('bale', 'pale'), ('pale', 'pa')]

for i in input
    print(check_edit_away(i[0], i[1]))