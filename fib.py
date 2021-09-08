
"""
Fibonacci number generator
When given a position, the function returns the fibonacci at that position in the sequence.
The zeroth number in the fibonacci sequence is 0. The first number is 1
"""
def fibonacci(position):
  if(position == 1 or position == 2):
    return 1
  return fibonacci(position - 1) + fibonacci(position - 2)


# Test cases
print("The 1st Fibonacci number: ", fibonacci(1))
print("The 21st Fibonacci number: ", fibonacci(21))
print("The 0th Fibonacci number: ", fibonacci(1))
print("The -1st Fibonacci number: ", fibonacci(-1))

print("Code ran successfully!")

