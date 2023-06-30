"""
IIb: Practical Warm Up

Place msg="You can't add int to string" in the correct place below such that the program avoids a BaseExceptionError.
You can use except Exception, although normally you should be careful using such powerful exception statements.

#Type your answer below.

a="Hello World!"
try:
    a + 10



print(msg)
"""

# Solution
a = "Hello World!"
try:
    a + 10
except Exception:
    msg = "You can't add int to string"

print(msg)
