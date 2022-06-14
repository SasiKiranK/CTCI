import unittest
from collections import Counter


def is_unique(string):
    if len(string) > 128:
        return False

    char_set = [False for i in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    DataT = ['tes', 'new', '']
    DataF = ['test', 'yess']

    def test_is_unique(self):

        # true test
        for data in self.DataT:
            actual = is_unique(data)
            self.assertTrue(actual)

        # false test
        for data in self.DataF:
            actual = is_unique(data)
            self.assertFalse(actual)


# if __name__ == "__name__":
# unittest.main()

# Need to find if


# Method: Character map
# Time: O(n)
# Space: O(n)

# Follow-up
# Method: Sort and compare
# Time: O(n*log(n))
# Space: O(n)


def all_uniqs(input_str: str):
    ctr = Counter(input_str)

    for k, v in ctr.items():
        if v > 1:
            return False
    return True


def all_uniqs_no_datastruct(x: str):
    sorted_x = sorted(x)
    n = len(x)
    for i in range(1, n):
        if sorted_x[i - 1] == sorted_x[i]:
            return False
    return True


if __name__ == "__main__":

    inputs = ["", "aaasodkc", "abbccdcss", "aaa", "b", "bdes"]

    for x in inputs:
        print(
            "Input {x} result: {all_uniqs(x)} same as {all_uniqs_no_datastruct(x)}")
