def check_edit_away(str1, str2):
    s1 = len(str1)
    s2 = len(str2)

    if abs(s1 - s2) > 1:
        return False

    if s1 == s2:
        count = 0
        for i in range(s1):
            if str1[i] != str2[i]:
                count += 1
        if count == 1 or 0:
            return True
        return False

    if s1 > s2:
        return insert_away(str1, str2)
    else:
        return insert_away(str2, str1)


def insert_away(s1, s2):
    i, j = 0, 0
    edited = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            j = j + 1
            i = i + 1
    return True


input = [('pale', 'pal'), ('bale', 'sade'), ('pa', 'pal')]

for i in input:
    print(check_edit_away(i[0], i[1]))
