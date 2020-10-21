import random
import string
from math import gcd
import re


def main():
    key = generate()
    single_bit_test(key)
    long_series_test(key)
    poker_test(key)
    series_test(key)

def checkIfRelativelyPrime(a, b):
    if gcd(a, b) == 1:
        return 1
    else:
        return 0


def generate():
    p, q = 0, 0
    dividers = 0

    while p % 4 != 3 and dividers != 2:
        p = random.randint(0, 1000)
        for a in range(1, p+1):
            if p % a == 0:
                dividers = dividers + 1

    while q % 4 != 3 and dividers != 2:
        q = random.randint(0, 1000)
        for a in range(1, p+1):
            if p % a == 0:
                dividers = dividers + 1

    N = p * q

    x = 0
    x_dividers = [0]
    n_dividers = []

    for z in range(1, N+1):
        if N % z == 0:
            n_dividers.append(z)

    no_of_calc = 0
    x = random.randint(0, N)

    while checkIfRelativelyPrime(x, N) == 0:
        x = random.randint(0, N)
        checkIfRelativelyPrime(x, N)

    primal_value = (x*x) % N

    key = ''

    if primal_value % 2 == 0:
        bit = 0
    else:
        bit = 1

    key = key + str(bit)
    prev_xi = primal_value

    for i in range(1, 20000):
        xi = (prev_xi * prev_xi) % N
        if xi % 2 == 0:
            bit = 0
            key = key + str(bit)
        else:
            bit = 1
            key = key + str(bit)
        prev_xi = xi

    #print("\n" + key + "\n")
    return key


def single_bit_test(key):
    res = key.count('1')
    if res > 9725 and res < 10275:
        print("\nTest pojedynczego bitu - zakonczony powodzeniem")
        return 1
    else:
        print("\nTest pojedynczego bitu - zakonczony niepowodzeniem")
        return 0


def series_test(key):
    regex1_1 = re.compile('[1](0){1}[1]?|[1]?(0){1}[1]')
    regex1_2 = re.compile('[1](1){1}[1]?|[1]?(1){1}[1]')
    res1_1 = regex1_1.findall(key)
    res1_2 = regex1_2.findall(key)
    regex2 = re.compile('(0){2}|(1){2}')
    res2 = regex2.findall(key)
    regex3 = re.compile('(0){3}|(1){3}')
    res3 = regex3.findall(key)
    regex4 = re.compile('(0){4}|(1){4}')
    res4 = regex4.findall(key)
    regex5 = re.compile('(0){5}|(1){5}')
    res5 = regex5.findall(key)
    regex6 = re.compile('(0){6,}|(1){6,}')
    res6 = regex6.findall(key)

    if 2315 < len(res1_1 + res1_2) < 2685 and 1114 < len(res2) < 1386 and len(res3) > 527 and 723 > len(res4) < 384 and 103 > len(res5) > 209 and 103 > len(res6) > 209:
        print("\nTest serii - zakonczony powodzeniem")
        return 1
    else:
        print("\nTest serii - zakonczony niepowodzeniem")
        return 0

def long_series_test(key):
    regex = re.compile('(0){26,}|(1){26,}')
    res = regex.search(key)

    if res is None:
        print("\nTest dlugiej serii - nie znaleziono serii zer i jedynek o dlugosci >= 26")
        return 1
    else:
        print("\nTest dlugiej serii - znaleziono serie zer i jedynek o dlugosci >= 26")
        return 0


def poker_test(key):

    def split_len(seq, length):
        return [seq[i:i + length] for i in range(0, len(seq), length)]

    segments = split_len(key, 4)
    #print(segments)

    unique_segments = {
        '0000': 0, '0001': 0, '0010': 0, '0011': 0,
        '0100': 0, '0101': 0, '0110': 0, '0111': 0,
        '1000': 0, '1001': 0, '1010': 0, '1011': 0,
        '1100': 0, '1101': 0, '1110': 0, '1111': 0,
    }
    #print(unique_segments)

    dict = {}
    for a in unique_segments:
        counter = 0
        for b in segments:
            if a == b:
                counter = counter + 1
        dict[a] = counter
        counter = 0

    #print(dict)
    sum = 0
    el = 0
    for i in dict:
        el = dict.get(i)*dict.get(i) - 5000
        sum = sum + el
        el = 0

    x = (16/5000)*sum-5000

    if x > 2.16 and x < 46.17:
        print("\nTest pokerowy - zakonczony z powodzeniem. Wartosc x = " + str("%.2f" % x))
        return 1
    else:
        print("\nTest pokerowy - zakonczony niepowodzeniem. Wartosc x = " + str("%.2f" % x))
        return 0

main()