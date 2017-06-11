import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumtrapz

initial_height = 30.0 # rider starts at an initial height of 30 meters.


path = 'droptower_vdata.txt'
velocity_data = np.loadtxt(path)

num_interval = velocity_data.shape[0]

t = velocity_data[:, 0]
t_shorter = t[:-1]

velocity = velocity_data[:, 1]
acceleration = np.diff(velocity)
position = cumtrapz(velocity, initial = initial_height)
acceleration_positive = acceleration[acceleration>0]
aver_pos = np.mean(acceleration_positive)


#print('t:', t)

#print('velocity:', velocity)

#print('acceleration:', acceleration)

#print('t_shorter:', t_shorter)

#print('position:', position)

#print('acceleration_positive:', acceleration_positive)


plt.figure(0)
plt.plot(t, velocity, '+-')
plt.xlabel('time / s')
plt.ylabel('velocity / m*s^-1')
plt.title('velocity of drop tower over time')
plt.savefig('velocity')

plt.figure(1)
plt.plot(t_shorter, acceleration, '*-')
plt.xlabel('time / s')
plt.ylabel('acceleration / m*s^-2')
plt.title('acceleration of drop tower over time')
plt.savefig('acceleration')

plt.figure(2)
plt.plot(t, position, '*-')
plt.xlabel('time / s')
plt.ylabel('position / m')
plt.title('position of drop tower over time')
plt.savefig('position')

print('average of positive accelerations:', aver_pos)
