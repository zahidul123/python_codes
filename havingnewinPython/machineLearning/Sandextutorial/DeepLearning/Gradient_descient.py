import numpy as np

def gradient_descent(x,y):
    m_curr=b_current=0
    itteration=1000
    n=len(x)
    learning_rate=0.08
    for i in range(itteration):
        y_predic=m_curr*x+b_current
        cost=(1/n)*sum([val**2 for val in(y- y_predic)])
        m_derivative=-(2/n)*sum(x*(y-y_predic))
        b_derivative = -(2 / n) * sum((y - y_predic))
        m_curr=m_curr-learning_rate*m_derivative
        b_current=b_current-learning_rate*b_derivative
        print("m {},b {},cost {},itteration {}".format(m_curr,b_current,cost,i))


x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])
gradient_descent(x,y)
