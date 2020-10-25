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
        print(j.rjust(width),o[2:].rjust(width),h[2:].upper().rjust(width),b[2:].rjust(width))
        #print("{:2} {:2} {:2} {:2}".format(j,o[2:],h[2:].upper(),b[2:]))


if __name__ == '__main__':
    n = 10 # int(input()) # let n=10
    print_formatted(n)
    
    
"""
Output:
   1    1    1    1
   2    2    2   10
   3    3    3   11
   4    4    4  100
   5    5    5  101
   6    6    6  110
   7    7    7  111
   8   10    8 1000
   9   11    9 1001
  10   12    A 1010
"""
