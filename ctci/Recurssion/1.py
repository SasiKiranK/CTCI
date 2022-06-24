def print_num(n):
    print(n)
    if (n == 0):
        return
    print_num(n - 1)


def print_asen(n):
    if (n == 0):
        return
    print_asen(n - 1)
    print(n)


def print_fact(n):
    # if sum:
    #     sum = 0
    if n == 0 or n == 1:
        return 1
    sum = n * print_fact(n - 1)
    return sum


# print_asen(3)
# print(print_fact(5))

def print_fibo(n):
    if n == 0 or n == 1:
        return 1
    sum = print_fibo(n - 1) + print_fibo(n - 2)
    return sum


print(print_fibo(5))
# print(5 * 4 * 3 * 2 * 1)
