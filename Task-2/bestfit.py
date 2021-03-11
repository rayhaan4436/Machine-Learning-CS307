import matplotlib.pyplot as plt
import numpy as np

def slp_inter(x,y):
	n=len(x)
	x_mean=sum(x)/n
	y_mean=sum(y)/n
	
	num=0
	den=0
	
	for i in range(n):
		num+=(x[i]-x_mean)*(y[i]-y_mean)
		den+=(x[i]-x_mean)**2
		
	slope = num/den
	intercept = y_mean - slope*x_mean
	return slope, intercept
	
x=[1,2,3]
y=[1.2,1.9,3.2]

m, c = slp_inter(x,y)

x = np.array(x)
y = np.array(y)
plt.title("Best fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y,'o')
plt.plot(x, m*x+c)

plt.show()
