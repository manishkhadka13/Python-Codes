import numpy as np
import matplotlib.pyplot as plt
def coefficient_estimate(x,y):
    n=np.size(x)
    mean_x=np.mean(x)
    mean_y=np.mean(y)
    SS_xy=np.sum(y*x)-n*mean_y*mean_x
    SS_xx=np.sum(x*x)-n*mean_x*mean_x
    b1=SS_xy/SS_xx
    b0=mean_y-b1*mean_x
    return(b0,b1)
def plot_regression(x,y,b):
    plt.scatter(x,y,color="r",marker="o",s=30)
    y_predicted=b[0]+b[1]*x
    plt.plot(x,y_predicted,color="b")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
def main():
    x=np.array([0,1,2,3,4,5,6,7,8,9])
    y=np.array([1,3,11,7,17,8,13,14,18,19])
    b=coefficient_estimate(x,y)
    print("Estimated coefficients:\nb_0 = {}  \nb_1 = {}".format(b[0], b[1]))
    plot_regression(x,y,b)
if __name__=="__main__":
    main()

