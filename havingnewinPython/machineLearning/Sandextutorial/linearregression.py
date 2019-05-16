import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random
style.use("fivethirtyeight")

xs = [1,2,3,4,5]
ys = [5,4,6,5,6]
xs = np.array([1,2,3,4,5], dtype=np.float64)
ys = np.array([5,4,6,5,6], dtype=np.float64)


def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val += step
        elif correlation and correlation == 'neg':
            val -= step

    xs = [i for i in range(len(ys))]

    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def best_fit_slope(xs,ys):
    e=np.multiply(xs,ys)
    a=np.sum(e)
    #print(a)
    b=(np.sum(xs)*np.sum(ys))
    #print(b)
    c=np.sum(xs**2)
    d=((np.sum(xs))**2)
    m=((a-b)/(c-d))
    l = len(xs)
    s = ((np.sum(ys)) - (m * (np.sum(xs))))
    d = s / l
    return m,d

xs,ys=create_dataset(40,40,2,correlation='pos')

m,d = best_fit_slope(xs,ys)
regression=[((m*x)+d)for x in xs]
print(regression)
predict_x=12
predict_y=((m*predict_x)+d)
plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y,s=50,color='black')
plt.plot(xs,regression)
plt.show()


