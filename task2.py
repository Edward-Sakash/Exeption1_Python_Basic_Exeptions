"""
IIb: Practical Warm Up (30 mins)
Place result="You can't divide by 0" in the correct place below such that the program avoids a ZeroDivisionError.
#Type your answer below (pick the correct line).

a=5
b=0
try:
    result=a/b
except ZeroDivisionError:


print(result)
"""
# Solution

a = 5
b = 0
try:
    result = a / b
except ZeroDivisionError:
    result = "You can't divide by 0"

print(result)

