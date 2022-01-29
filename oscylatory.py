import cmath

d = 0.24
m1 = 21
m2 = 2
k1 = 11.5
k2 = 11.5


def find_roots(a, b, c):
  roots = []
  delta = (b**2) - (4*a*c)

  roots.append((-b + cmath.sqrt(delta))/(2 * a))
  roots.append((-b - cmath.sqrt(delta))/(2 * a))

  return roots

# 1.d
r = find_roots(1, 0, k1/m1)
print("λ1: {0}, λ2: {1}".format(r[0], r[1]))