"""
Given a non-empty string which is composed of a repeating pattern and less than 200 characters in length, 
this algorithm will return the repeating pattern and how many times it occurs in the string.
"""

def find_repeating_string(s):
    length = len(s)
    
    # Only need to check half of string as for string to be repeating, it needs to repeat at least once
    for i in range(1, int(length/2)+1):
        # leftovers is size of substring
        size, remainder = divmod(length, i)
        substring = s[:i]
        
        # First check if length string is divisible be length of substring  - otherwise, it can't be repeating
        # Second check if original string equals 
        if (remainder == 0) and (s == substring * size):
            return substring, size
        
    return "There is no substring", 1
    
slices = find_repeating_string("abcabcabcabc")      # this string = 'abc' * 4
print(slices)

slices = find_repeating_string("abccbaabccba")      # this string = 'abccba' * 2
print(slices)

slices = find_repeating_string("llllllllllll")      # this string = 'l' * 12
print(slices)

slices = find_repeating_string("awgeqbt")           # no repeating pattern
print(slices)

slices = find_repeating_string("123123")            # this string = '123' * 2
print(slices)