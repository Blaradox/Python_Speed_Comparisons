import timeit

def is_palindrome_if(s: str) -> bool:
    if len(s) <= 1:
        return True
    elif s[0] != s[1]:
        return False
    else:
        return is_palindrome_if(s[1:-1])

def is_palindrome_sc(s: str) -> bool:
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[1] and is_palindrome_sc(s[1:-1])

def main():
    print('Check if "1234567890987654321" is a palindrome')
    print('\twith if statements\t',
        timeit.timeit(lambda: is_palindrome_if("1234567890987654321"), number=1_000_000))
    print('\twith short circuits\t',
        timeit.timeit(lambda: is_palindrome_sc("1234567890987654321"), number=1_000_000))

    print('Check if "12345678900987654321" is a palindrome')
    print('\twith if statements\t',
        timeit.timeit(lambda: is_palindrome_if("12345678900987654321"), number=1_000_000))
    print('\twith short circuits\t',
        timeit.timeit(lambda: is_palindrome_sc("12345678900987654321"), number=1_000_000))

if __name__ == '__main__':
    main()
