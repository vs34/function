import math
import matplotlib.pyplot as plt
#s=ut+1/2at^2
#v^2-u^2=2as
#at=v-u
#g=mG/r^2
rdps=363
sv = 11190
m=59720
G=6674
te = 62608050
Av = []
R = []
Hv = []
for r in range(6371,11821,1):
    print('r = ',r)
    g = m*G/(r**2)
    print('g = ',g)
    pe = g*(r-6371)
    print('PE = ',pe)
    te = te-pe
    print('KE = ',te)
    hv = 2*te
    hv = math.sqrt(hv)
    print('Hv = ',hv)
    R.append(r)
    Hv.append(hv)
    av = rdps*r
    Av.append(av)
    print("====================================================")

# x axis values
x = R
# corresponding y axis values
y = Hv

# plotting the points
plt.plot(x, y)
#plt.plot(x, Av)
# naming the x axis
plt.xlabel('x(radius) - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('velocety vs r')

# function to show the plot
plt.show()
