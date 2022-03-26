""" 
This is an example of a Beatty sequence.
A Beatty sequence is a type of spectrum sequence (a sequence with successive multiples of a real number 'a'
rounded down to the nearest integer - i.e. floor(n*a))
In a Beatty sequence, this real number 'a' is instead an irrational number.

Rayleigh's Theorem (aka. Beatty's Theorem) states that given a Beatty sequence with irrational number a > 1,
there exists a complementary Beatty sequence with irrational number b > 1, if and only if   1/a + 1/b = 1.
The union of these two Beatty sequences partition the set of natural numbers.

By considering the sum of the Beatty sequence with irrational number 'a' up to n,
and the Beatty sequence with irrational number 'b' up to n*(a/b) we can use summation rules to obtain an equation
for the first Beatty sequence:
    Beatty(a, n) = (n+x)(n+x+1)/2 - Beatty(b, x)
    where x = floor((a-1)*n)
In this problem, a = sqrt(2), so using Rayleigh's Theorem, b = 2 + sqrt(2).
Substituting this in and re-arranging allows a final equation to be obtained as seen in the program code.

In this program, accuracy and precision is important. The class Decimal is used instead of the class Math 
- this is because math.sqrt(2) is only accurate up to 16 decimal places whereas with Decimal(2).sqrt() the 
precision and hence accuracy can be specified.
"""
from decimal import *

# sets the precision of any Decimal numbers to 200 digits to ensure an accurate number is used
getcontext().prec = 200

def solution(str_n):
    n = int(str_n)
    z = beatty(Decimal(2).sqrt(), n)
    return str(int(z))
    
def beatty(a, n):
    if n == 0:
        return 0
    # no need for floor function as int() truncates number
    x = int((a-1) * n)
    return ((n*x) + n*(n+1)/2 - x*(x+1)/2 - beatty(a, x))


answer = solution("77")
print(answer)   # 4208

answer = solution("5")
print(answer)   # 19

answer = solution("1")
print(answer)   # 1

answer = solution("99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
print(answer)