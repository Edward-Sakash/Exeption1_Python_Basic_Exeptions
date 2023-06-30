"""
Python basics - Exceptions-II
IIa: Theoretical Warm Up
Write short answers (2-5 sentences) to the following questions:

Name three things that exception processing is good for.
What happens to an exception if you don’t do anything special to handle it?
How can your script recover (program continuation) from an exception?
What is the try statement for?
What are the two common variations of the try statement?
What is the raise statement for?

"""
# Question 1:Name three things that exception processing is good for.
# Answer:
# 1. Error Handling: Exception processing allows for the identification
# and handling of errors that occur during program execution.
# It provides a mechanism to catch and address unexpected or exceptional
# situations, preventing the program from terminating abruptly.

# 2. Debugging and Troubleshooting: Exceptions provide valuable information
# about the cause and location of errors. By raising and catching exceptions,
# developers can obtain detailed error messages and traceback information,
# aiding in the process of debugging and troubleshooting code.

# 3.Graceful Program Termination: Exceptions allow for controlled program
# termination in the event of critical errors. By catching and handling
# exceptions appropriately, the program can perform necessary cleanup operations,
# log error information, and exit gracefully, ensuring that resources are properly
# released and the program's state is maintained.
 
# Question 2: What happens to an exception if you don’t do anything special to handle it?
# Answer: 
# If an exception is not handled or caught in the code, it will propagate up
# the call stack until it reaches the top-level of the program. This propagation
# continues until the exception is caught and handled, or if it reaches the default
# exception handler at the top level of the program. When an unhandled exception
# reaches the top level, the program terminates, and a traceback message is printed,
# displaying the sequence of function calls that led to the exception. This traceback
# message helps in identifying the cause and location of the unhandled exception for debugging purposes.
 
# Question 3:How can your script recover (program continuation) from an exception?
# Answer:
# To enable script recovery and program continuation from an exception, you can use exception handling.
# By using a try-except block, you can catch and handle exceptions in your script. Here's how it works:
#Place the code that may potentially raise an exception inside the try block.
# If an exception occurs within the try block, the corresponding except block(s) will be executed.
# In the except block(s), you can provide code to handle the exception appropriately.
# This could involve logging the error, displaying an error message, or taking corrective actions.
#After the except block(s) are executed, the program continues execution from the point
# immediately following the try-except block, allowing it to recover and continue its normal flow.
# By handling exceptions within your script, you can prevent the program from abruptly
# terminating and provide a controlled and graceful recovery mechanism.
# It allows you to address errors, perform necessary cleanup operations, and guide
# the program to continue its execution without interruption.

# Question 4:What is the try statement for?
# Answer: the try statement provides a structured way to handle and recover from
# exceptions, ensuring that the program can gracefully respond to unexpected
# or exceptional situations during runtime.
# The try statement in Python is used for exception handling. It allows you to enclose
# a block of code that may potentially raise an exception. The purpose of the try statement
# is to test a block of code for exceptions and define how the program should react when an exception occurs.
# The structure of a try statement consists of the keyword "try" followed by
# a block of code (the try block) that is susceptible to raising exceptions.
# If an exception is raised within the try block, the program flow is transferred
# to the corresponding except block(s) that handle the specific exception type(s).
# If no exceptions occur, the except block(s) are skipped,
# and the program continues execution after the try-except block.

# Question 5:What are the two common variations of the try statement?
# Answer: 
# The two common variations of the try statement in Python are:
# 1. try-except: This is the basic form of the try statement. It allows you to catch
# and handle specific exceptions that may be raised within the try block.
# You can specify one or more except blocks immediately following the try block.
# Each except block specifies the type of exception it can handle, and if any
# of the specified exceptions occur, the corresponding except block is executed.
# You can have multiple except blocks to handle different types of exceptions.

try:
    # Code that may raise an exception
    ...
except ExceptionType1:
    # Exception handling for ExceptionType1
    ...
except ExceptionType2:
    # Exception handling for ExceptionType2
    ...

# 2. try-except-else: This variation extends the basic try-except structure
# by adding an else block after the except block(s). The else block is optional
# and executed only if no exceptions occur in the try block. It is useful for
# specifying code that should be executed when the try block runs successfully
# without raising any exceptions.

try:
    # Code that may raise an exception
    ...
except ExceptionType:
    # Exception handling for ExceptionType
    ...
else:
    # Code to be executed if no exceptions occur
    ...

# These variations provide flexibility in handling exceptions, allowing you
# to catch specific exceptions or execute additional code based on whether an exception occurred or not.

# Question 6: What is the raise statement for?
# Answer: The raise statement in Python is used to explicitly raise an exception.
# It allows you to generate and throw exceptions programmatically at specified points
# in your code. By using the raise statement, you can indicate that a certain condition
# or error has occurred, and the exception will be caught and handled by the nearest applicable except block.
# The raise statement is typically followed by an exception class or an instance
# of an exception class. This indicates the type of exception to be raised.
# Optionally, you can provide an error message or additional information about the exception.

# Custom exception class
class CustomException(Exception):
    pass

# Raising the custom exception
raise CustomException("An error occurred.")
