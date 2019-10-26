"""
You are given two numerical strings, and your task is to return the sum of their digits, as described below.

Add every i-th  digit of the first string to the i-th digit of the second string, both counted from the end. 
If the i-th digit of one of the strings is absent the sum will be the i-th digit of the other string.
Return a string of those sums concatenated with each other.

Input: 
a = "99", b = "99"

Output:
"1818"

Input:
a = "11", b = "9"

 - The sum of both, the first and the second numbers are "18", so the answer is "1818".

Output:
"110"

 - The sum of the first numbers from the end is "10", and the sum of the second numbers from the end is "1",
 so the answer is "110"

Constraints:
 - Execution time limit 4s

[input] string a
 - The first string. It is guaranteed that a consists of digits only and does not contain leading zeros.
 - Guaranteed Constraints 1 <= a.length <= 10**5

[input] string b
  - The second string. It is guaranteed that b consists of digits only and does not contain leading zeros.
  - Guaranteed Constraints 1 <= b.length <= 10**5

[output] string
 - The sum of the digits of a and b concatenated together, as decribed above.

"""

