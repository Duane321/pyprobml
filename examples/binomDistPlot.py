import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from utils.util import save_fig

#Plots the pmfs of binomial distributions with varying probability of success parameter

N = 10

thetas = [.25, .5, .75, .9]

X = np.arange(0, N + 1)

for th in thetas:
    probs = binom.pmf(X, N, th)
    title = r'$\theta$' + "=" + str(th)
    fig, ax = plt.subplots()
    ax.bar(X, probs, align='center')
    plt.xlim([min(X)-.5, max(X)+.5])
    plt.xticks(X)
    plt.title(title)
    plt.draw()
    save_fig('binomDistTheta' + str(int(th*100)))

plt.show()
