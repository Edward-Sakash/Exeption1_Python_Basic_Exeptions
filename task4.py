"""
IIb: Practical Warm Up
Place msg="You're out of list range" in the correct place below such that the program avoids an IndexError.
#Type your answer below.

lst=[5, 10, 20]

try:
    print(lst[5])



print(msg)
"""

# Solution
lst = [5, 10, 20]
try:
    print(lst[5])
except IndexError:
    msg = "You're out of list range"

print(msg)
