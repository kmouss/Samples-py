import numpy as np
from plotData import *
from computeCost import *
from gradientDescent import *

# Test and Valiation data file
filename = './data1.txt'

# Load data from file into a 2-dimentional matrix
data = np.loadtxt(filename, delimiter=',')
m = len(data)

# Now set input and out put variables set as X and y respectively
X = data[:,0]
y = data[:,1]

# Now plot data
print('\nPloting data to view correlation between x and y values...\n')
#plotData(X, y)
plt.style.use('seaborn-whitegrid')
fig = plt.figure()
ax = plt.axes()
plt.scatter(X, y)
# display here as needed to get an idea of the pattern and help decide the ML algorithm to use
# plt.show()

input('Press ENTER to continue...')

# Calculate Cost Function
d = np.ones((m))
X = np.column_stack((d, X))
theta = np.array([0, 0])
# theta = np.zeros((2, 1))
# theta = [-1 , 2]
print('\nTesting the cost function ...\n')
J = computeCost(X, y, theta)  # compute and display initial cost
print('J= ', J)

input('Press ENTER to continue...')

# Some gradient descent settings
iterations = 1500
alpha = 0.01

# run gradient descent
print('\nRunning Gradient Descent ...\n')
theta = gradientDescent(X, y, theta, alpha, iterations)

print('Theta = ', theta)

input('Press ENTER to continue...')

# Plot the linear fit
#hold on; % keep previous plot visible
#plotData(X[:,1], X@theta)
lines = plt.scatter(X[:,1], X@theta)
plt.setp(lines, color='r', linewidth=2.0)
#legend('Training data', 'Linear regression')
#hold off % don't overlay any more plots on this figure

plt.show()