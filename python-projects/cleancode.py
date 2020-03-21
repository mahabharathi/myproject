#clean code
def is_even(num):
    if num%2==0:
        return True
    return False

print(is_even(20))
print(is_even(21))


def is_even1(num):
    return num%2==0

print(is_even1(20))
print(is_even1(21))