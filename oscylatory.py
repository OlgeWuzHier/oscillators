import cmath
import numpy as np
import matplotlib.pyplot as plt

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
r1 = find_roots(1, 0, k1/m1)
print("1-d: λ1: {0}, λ2: {1}".format(r1[0], r1[1]))

# 2.d
r2 = find_roots(1, 2 * d, k1/m1)
print("2-d: λ1: {0}, λ2: {1}".format(r2[0], r2[1]))


# 2.e - szukanie rozwiązania równania ruchu
delta_r = 4*(d**2 - k1/m1)
sqrt_delta_r = cmath.sqrt(delta_r)
ws = sqrt_delta_r.imag  # ta liczba do wstawienia do uproszczonego równania z rz. II do rz. I

c1 = 65/14  # wyliczone z warunku początkowego V0 = 0.5 i wyznaczonej ręcznie pochodnej x'
c2 = 5  # wyliczone z warunku początkowego x0 = 5 i funkcji x będącej rozwiązaniem równania ruchu dla układu drugiego z oscylatorem z tłumieniem

xs = []  # tablica do zapamiętania wychylenia w danym czasie (t takie jak index tablicy dla danej wartości)
for t in range(0, 5000):  # t w przedziale <0, 50)
  czas = t/100
  x = np.exp(-d * czas) * (c1 * np.sin(ws * czas) + c2 * np.cos(ws * czas))  # x(t)
  x_d = -d * np.exp(-d * czas)*(c1 * np.sin(ws * czas) + c2 * np.cos(ws * czas)) + np.exp(-d * czas) * (c1 * ws * np.cos(ws * czas) + c2 * ws * np.sin(ws * czas))  # x'(t), do 2-g
  xs.append([czas, x, x_d])

xs = np.array(xs)

plt.figure(figsize=(15, 10))  # wykres do 2e
plt.plot(xs[:, 0], xs[:, 1])  # x, y
plt.xlabel("Czas")
plt.ylabel("Wychylenie")
plt.grid(True, which="both")
plt.show()

plt.figure(figsize=(10,10))  # wykres do 2-g
plt.plot(xs[:, 1], xs[:, 2])
plt.show()
