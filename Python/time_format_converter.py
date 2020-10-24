#!/usr/bin/python
import re


def time_conversion(s):
    hour = int(s[00] + s[1])
    if s[9] == 'P':
        if hour < 12:
            hour += 12
        return str(hour) + s[2:8]
    if s[9] == 'A':
        if hour == 12:
            hour = 00
            return str(00) + str(hour) + s[2:8]
        if hour > 9 and hour < 12:
            return str(hour) + s[2:8]
        if hour > 00 and hour < 10:
            return str(00) + str(hour) + s[2:8]


if __name__ == '__main__':
    s = ''
    s = str(input('Enter the time (HH:MM:SS AM or HH:MM:SS PM): '))
    while not re.match('^(1[0-2]|0[1-9]):[0-5][0-9]:[0-5][0-9] (AM|PM)$', s):
        s = str(input('Invalid Input. Please enter in correct format!'))
    print ('\n24 hour time is:', time_conversion(s))
