# Quadratic time (Polynomial Time)
def bar(n): # O(1) + O(n^2) + O(1) ==> O(n^2)
  s = 0 # O(1)

  # O(n) * O(n) = O(n^2)
  for i in range(0, n): # O( n )
    for j in range(0, n): # O(n) * O91) = O(n) this loop runs in linear time
      s += i * j # O(1)

  return s # O(1)