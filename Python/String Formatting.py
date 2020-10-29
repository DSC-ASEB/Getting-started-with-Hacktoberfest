# String Formatting 
# HackerRank Question: https://www.hackerrank.com/challenges/python-string-formatting/problem
# author : Saketh-Chandra


def print_formatted(n):

    width = len(bin(n)[2:])
    for i in range(1,n+1):
        o=str(oct(i))
        h=str(hex(i))
        b=str(bin(i))
        j=str(i)
        print("{:2} {:2} {:2} {:2}".format(j,o[2:],h[2:].upper(),b[2:]))


if __name__ == '__main__':
    n = 10
    print_formatted(n)
