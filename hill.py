import numpy as np 
import matplotlib.pyplot as plt 
y=lambda x: x**4 + 5*x**3 +4*x**2-4*x+1
x=[i+j for i in range(-5,1) 
for j in [0.1,0.2,0.3,0.4] ]
res=[y(i) for i in  x]
print(res)
plt.plot(x,res)
plt.show()