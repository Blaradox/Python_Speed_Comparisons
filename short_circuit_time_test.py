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
    PAL_EVEN="1234567890987654321"
    PAL_ODD="12345678900987654321"
    REPEATS=10_000_000

    print(f'Check if {PAL_EVEN!r} is a palindrome, measured in seconds')
    print('\twith if statements\t',
        timeit.timeit(lambda: is_palindrome_if(PAL_ODD), number=REPEATS))
    print('\twith short circuits\t',
        timeit.timeit(lambda: is_palindrome_sc(PAL_ODD), number=REPEATS))

    print(f'Check if {PAL_EVEN!r} is a palindrome')
    print('\twith if statements\t',
        timeit.timeit(lambda: is_palindrome_if(PAL_EVEN), number=REPEATS))
    print('\twith short circuits\t',
        timeit.timeit(lambda: is_palindrome_sc(PAL_EVEN), number=REPEATS))

if __name__ == '__main__':
    main()
