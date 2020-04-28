from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt



Q, om, A, v0, th0 = 2, 2/3, 0.5, 0, 0.01
g = 9.8
l = g / (om**2)
x0 = [th0, v0]

def dy(x, t):
    tau = (g/l)**(1/2)*t
    return [x[1], A*np.cos(om*tau) - (1/Q)*x[1] - np.sin(x[0])]


t = np.linspace(0, 100, 100000)

x = odeint(dy, x0, t)

plt.subplot(1,2,1)
plt.plot(t, x[:,0])

plt.subplot(1,2,2)
plt.plot(x[:,0], x[:,1])
plt.show()