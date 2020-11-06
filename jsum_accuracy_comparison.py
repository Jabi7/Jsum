from funcLib import simpson_integrate, trapezoidal_integrate, midpoint_integrate
from jsum import jsum
from math import sin, pi, log
import matplotlib
import matplotlib.pyplot as plt

f = lambda x: 1.5*x**(0.5)
fi = lambda x: x**(1.5)
lims = (1,9)


j = jsum(f, lims[0], lims[1], tol = 2/5) # check the jsum funtion to find the reason for tol choice

s = simpson_integrate(f, lims, N = 5)		# notice we are giving high tolerance( ie, 1/N is high for small N)
m = midpoint_integrate(f, lims, N = 5)
t = trapezoidal_integrate(f, lims, N = 5)

ac = lambda x, l = 26: (l - abs(l - x))/l*100 
x = ['midpoint', 'trapezoidal', 'simpson', 'Jsum']
y = [ac(m), ac(t), ac(s), ac(j)]

for i, j in zip(list(x), list(y)):
	print(i, 'accuracy = ',j)

fig, a = plt.subplots()
a.plot(x, y)
a.set(xlabel='Itegration methods', ylabel='Accuracy(%)', title='Jsum comparison for very high tolerance(small N)')
a.grid()
fig.savefig("Jsum comparison result with standard methods.pdf")
plt.show()


# hence, we can see the advantge of accuracy of Jsum within less number of recursion than the iteration methods