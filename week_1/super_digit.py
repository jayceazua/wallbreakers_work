"""
We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of  will be calculated as:

	super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2  
You are given two numbers  and . The number  is created by concatenating the string   times. Continuing the above example where , assume your value . Your initial  (spaces added for clarity).

    superDigit(p) = superDigit(9875987598759875)
                  5+7+8+9+5+7+8+9+5+7+8+9+5+7+8+9 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)
All of the digits of  sum to . The digits of  sum to .  is only one digit, so it's the super digit.

Function Description

Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

n: a string representation of an integer
k: an integer, the times to concatenate  to make 
Input Format

The first line contains two space separated integers,  and .

Constraints

Output Format

Return the super digit of , where  is created as described above.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.


def superDigit(n, k):

    s = sum(int(digit) for digit in n)
    s *= k

    if s < 10:
        return s
    return superDigit(str(s), 1)
