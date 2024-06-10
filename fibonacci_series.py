def fibonacci(n):
  if n <= 0:
    print("Please enter a positive integer for the number of terms.")
    return
  a, b = 0, 1
  print(a)
  if n == 1:
    return
  for _ in range(2, n + 1):
    c = a + b 
    print(c)
    a, b = b, c 
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci(n)
