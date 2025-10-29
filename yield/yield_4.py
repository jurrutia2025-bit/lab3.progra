def fibonacci_generator(n):
  """Genera la serie de Fibonacci hasta el n-ésimo elemento usando yield."""
  a, b = 0, 1
  for _ in range(n):
    yield a
    
    a, b = b, a + b

print("Serie de Fibonacci hasta el décimo elemento:")
for num in fibonacci_generator(10):
  print(num)