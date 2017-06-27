'''
    An implementation of a hash function
'''


def hash(inStr, radix, modulus):

    hash_value = 0
    for c in inStr:
        hash_value = (hash_value * radix + ord(c)) % modulus

    return hash_value
