# a > b

# GCD
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

# LCM
def lcm(a, b):
  return a * b // gcd(a, b)
