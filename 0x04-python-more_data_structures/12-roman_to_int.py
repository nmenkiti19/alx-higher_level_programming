#!/usr/bin/python3
def roman_to_int(roman_string):
    """Function converts roman numeral to integer"""
    result = 0
    if not (isinstance(roman_string, str)):
        return (0)
    for i in range(len(roman_string)):
        if (roman_string[i] == 'I'):
            result += 1
        if (roman_string[i] == 'V'):
            if (roman_string[i - 1] == 'I' and i != 0):
                result -= 2
            result += 5
        if (roman_string[i] == 'X'):
            if (roman_string[i - 1] == 'I' and i != 0):
                result -= 2
            result += 10
        if (roman_string[i] == 'L'):
            if (roman_string[i - 1] == 'X' and i != 0):
                result -= 20
            result += 50
        if (roman_string[i] == 'C'):
            if (roman_string[i - 1] == 'X' and i != 0):
                result -= 20
            result += 100
        if (roman_string[i] == 'D'):
            if (roman_string[i - 1] == 'C' and i != 0):
                result -= 200
            result += 500
        if (roman_string[i] == 'M'):
            if (roman_string[i - 1] == 'C' and i != 0):
                result -= 200
            result += 1000
    return (result)
