#!/usr/bin/python3
from hashlib import md5
"""
Solve the HTS Programming Challenge #3.
Problem Statement: Brute force a ciphertext of 15 serial numbers,
xxx-xxx-OEM-xxx-1.1\n (x in [A-Z,1-9]), encrypted by the encrypt() function,
below.
"""

MD5_SIZE = 32


def encrypt(plaintext, password):
    """
    Encrypt a string according to the HTS specified algorithm.
    """
    key = md5(password.encode('utf-8')).hexdigest()
    cross_total = eval_cross_total(key)
    result = []
    i = 0
    for char in plaintext:
        result.append(ord(char) + int(key[i % 32], 16) - cross_total)
        s1 = md5(plaintext[0:i+1].encode('utf-8')).hexdigest()[0:16]
        s2 = md5(str(cross_total).encode('utf-8')).hexdigest()[0:16]
        cross_total = eval_cross_total(s1 + s2)
        i = i+1
    return result


def eval_cross_total(string):
    """ Return the decimal sum of characters in a hexadecimal string. """
    total = 0
    for x in string:
        total += int(x, 16)
    return total


def brute(ciphertext, plaintext, cross_totals, i, chars_required=34):
    """
    Perform a DFS over the possible values of the key until the
    a plaintext of chars_required length is reached. After each
    potential plaintext character is generated, check against the
    serial number constraints using check_plaintext().
    Also keep a list of cross_totals to determine the key later.
    """
    # print("brute(..", plaintext, "..)") #to debug
    if i == chars_required:
        return True
    for key in range(16):
        c, next_cross_total = decrypt_step(ciphertext, i, cross_totals[i],
                                           key, plaintext)
        if check_plaintext(c, i):
            cross_totals.append(next_cross_total)
            plaintext.append(c)
            if brute(ciphertext, plaintext, cross_totals, i+1, chars_required):
                return True  # reached the exit critera, unravel
        else:
            continue
    if plaintext:
        plaintext.pop()
    cross_totals.pop()
    return False


def solve(ciphertext, chars_required):
    """
    Try all the possible IVs in most-likely-first order and
    return a viable key for the ciphertext.
    IV[0] = eval_cross_total(password) therefore is a sum of a 32-byte
    md5 hash. Min = 0, Max = 16*2, Avg (given md5 uniformity) = 256
    chars_required is the number of chars of the plaintext to decrypt
    before guessing the key (needs to be at least 32 for md5).
    """
    # 256, 255, 257, 254...
    IVs = [256]
    for i in range(1, 256):
        IVs.append(256+i)
        IVs.append(256-i)
    for key in IVs:
        cross_totals = [key]
        plaintext = []
        if brute(ciphertext, plaintext, cross_totals, 0, chars_required):
            found_key = determine_key(ciphertext, plaintext, cross_totals)
            break
    return found_key


def check_plaintext(char, pos):
    """ Is a potential plaintext character legal given its position? """
    valid = {3: '-', 7: '-', 8: 'O', 9: 'E', 10: 'M', 11: '-', 15: '-',
                16: '1', 17: '.', 18: '1', 19: '\n'}
    pos %= 20
    if pos in valid:
        return True if valid[pos] == char else False
    else:
        if ord(char) > 47 and ord(char) < 58:
            return True
        if ord(char) > 64 and ord(char) < 91:
            return True
        return False


def decrypt_step(ciphertext, i, cross_total, key_i, plaintext):
    """
    Use the inverse of the encrypt() and the given key[i] to determine
    the ith letter of plaintext. Calculate the next cross_total then
    return them both as a tuple.
    """
    try:
        c = chr(ciphertext[i] + cross_total - key_i)
    except ValueError:
        # out of range with certain guesses of key. return an invalid
        # char which won't get past constraint check
        c = '?'
    s1 = md5(("".join(plaintext)+c).encode('utf-8')).hexdigest()[0:16]
    s2 = md5(str(cross_total).encode('utf-8')).hexdigest()[0:16]
    return (c, eval_cross_total(s1 + s2))


def determine_key(ciphertext, plaintext, cross_totals):
    """ Determine the original hash from a given plain/cipher text pair """
    assert len(plaintext) >= MD5_SIZE
    key = ""
    for i in range(MD5_SIZE):
        key += format(ciphertext[i] - ord(plaintext[i]) + cross_totals[i], 'x')
    return key


def decrypt(ciphertext, key):
    """ Reverse the encrypt(plaintext, key) function. """
    cross_total = eval_cross_total(key)
    plaintext = ""
    i = 0
    for c in ciphertext:
        plaintext += chr(c + cross_total - int(key[i % 32], 16))
        s1 = md5(plaintext.encode('utf-8')).hexdigest()[0:16]
        s2 = md5(str(cross_total).encode('utf-8')).hexdigest()[0:16]
        cross_total = eval_cross_total(s1 + s2)
        i += 1
    return plaintext


def main():
    plaintext = ('C4Z-KH5-OEM-240-1.1\nQGG-V33-OEM-0B1-1.1\n'
                 'Z93-Z29-OEM-BNX-1.1\nIQ0-PZI-OEM-PK0-1.1\n'
                 'UM4-VDL-OEM-B9O-1.1\nL0S-4R2-OEM-UQL-1.1\n'
                 'JBL-EYQ-OEM-ABB-1.1\nNL1-3V3-OEM-L4C-1.1\n'
                 '7CQ-1ZR-OEM-U3I-1.1\nXX0-IHL-OEM-5XK-1.1\n'
                 'KJQ-RXG-OEM-TW8-1.1\nOZR-LW1-OEM-5EM-1.1\n'
                 '0B8-6K5-OEM-EFN-1.1\nOE2-20L-OEM-SSI-1.1\n'
                 '0ME-HAE-OEM-9XB-1.1')
    ciphertext = encrypt(plaintext, "Unknown Password")
    key = solve(ciphertext, 34)
    print(decrypt(ciphertext, key))


if __name__ == "__main__":
    main()
