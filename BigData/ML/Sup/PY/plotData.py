import matplotlib.pyplot as plt

def plotData(X, y):
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = plt.axes()
    plt.scatter(X, y)
    plt.show()
  