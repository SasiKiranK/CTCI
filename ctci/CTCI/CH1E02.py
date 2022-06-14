from collections import Counter


def is_palindrome(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    counter = Counter()

    for char in string_a:
        counter[char] += 1
    for char in string_b:
        if counter[char] == 0:
            return False
        counter[char] -= 1
    return True


if __name__ == "__main__":
    string_a = 'abcd'
    string_b = 'bbcda'
    input_palindrome = (
        (
            'abc', 'abd'
        ),
        (
            'abc', 'cab'
        ),
        (
            'abc', 'abd'
        )
    )
    for i in input_palindrome:
        print(is_palindrome(i[0], i[1]))
