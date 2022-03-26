import numpy as np
from fractions import Fraction


def get_term_states(m):
    # Each state is unique so to ensure this, the terminal states are stored in a set
    terminal_states = set()
    for row in range(0, len(m)):
        # If every position in the state is 0, then the state is terminal
        if sum(m[row]) == 0:
            terminal_states.add(row)
    return terminal_states


def get_submatrices(m, term_states):
    # Q is a t x t matrix and R is a t x s matrix
    # t = the amount of rows from the initial state to the first terminal state
    # s = the amount of terminal states
    q = []
    r = []
    
    for row in range(0, len(m)):
        if row not in term_states:
            total = sum(m[row])
            q_temp = []
            r_temp = []
            for col in range(0, len(m[row])):
                # As Q is t x t, it only contains elements which aren't in any terminal rows or columns
                if col not in term_states:
                    q_temp.append(float(m[row][col])/total)
                # As R is t x s, it only contains elements which aren't in any terminal rows but which are in terminal columns
                else:
                    r_temp.append(float(m[row][col])/total)
            q.append(q_temp)
            r.append(r_temp)
            
    return (q, r)


# The fundamental matrix, N = (I - Q)^-1
# where I is the t x t identity matrix and ^-1 is the inverse
def get_n_matrix(q):
    identity = np.identity(len(q))
    n = np.subtract(identity, q)
    n_inv = np.linalg.inv(n)
    return(n_inv)
  

# Finds the greatest common denominator of two numbers  using Euclidean algorithm   
def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x
    

def get_fractions(prob):
    # Goes through the top row of the probability matrix and approximates each decimal to a fraction with a limited denominator
    fractions = [Fraction(prob[0][i]).limit_denominator() for i in range(0, len(prob[0]))]
    denoms = [fract.denominator for fract in fractions]
    
    # To simplify the fractions, the lowest common denominator is found
    lcd = denoms[0]
    for den in denoms:
        lcd = lcd // gcd(lcd, den) * den

    # Creates the final probability matrix with the numerators for each terminal states and the denominator at the end
    nums = [int(fract.numerator * (lcd / fract.denominator)) for fract in fractions] + [lcd]
    return nums


# This uses an absorbing Markov Chain to find the probabilities, where m is the transition matrix
def solution(m):
    # If the transition matrix has 1 or less rows then it is certain it will terminate
    if len(m) <= 1:
        return [1, 1]

    # If every state in the transition matrix is terminal then the probability of reaching each state is 0, with a denominator of 1
    term_states = get_term_states(m)
    if len(term_states) == len(m):
        return [0 for i in range(0, len(m))] + [1]
    
    q, r = get_submatrices(m, term_states)
    n = get_n_matrix(q)
    
    # The probability matrix is equal to the dot product of the fundamental matrix (N) and submatrix (R)
    prob = np.dot(n, r)
 
    return get_fractions(prob)

 
answer = solution([[0, 1, 0, 0, 0, 1], 
                   [4, 0, 0, 3, 2, 0], 
                   [0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0]]) # [0, 3, 2, 9, 14]
print(answer)

answer = solution([[0, 2, 1, 0, 0], 
                   [0, 0, 0, 3, 4], 
                   [0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0]])    # [7, 6, 8, 21]
print(answer)

answer = solution([0])  # [1, 1]
print(answer)

answer = solution([[0, 1],
                   [0, 0]]) # [1, 1]
print(answer)

answer = solution([[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],]) # [0, 0, 0, 0, 1]
print(answer)

answer = solution([[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 0]])    # [1, 1]
print(answer)

answer = solution([[103424363, 7132421, 15463234, 34359, 303887451],
                   [42276556711, 0, 932425349, 1034223437, 5567867639],
                   [1028977601, 7878763243261, 7659, 38344, 28978989459],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]])
print(answer)





def create_identity_matrix(n):
    matrix = [[0 for i in range(0, n)] for j in range(0, n)]
    for i in range(0, n):
        matrix[i][i] = 1
    return matrix

def get_t(m):
    t = 0
    for row in m:
        if sum(row) == 0:
            return t
        t += 1
    # This will only be reached if there are no terminal states
    return t