def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if a <= b and a != 1:
        n = a
        while a % n != 0 or b % n != 0:
            n -= 1
        return n
    elif a >= b and b != 1:
        n = b
        while a % n != 0 or b % n != 0:
            n -= 1
        return n


print(gcdIter(40, 77))
