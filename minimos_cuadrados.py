#ajuste por minimos cuadrados

import numpy as np
import matplotlib.pyplot as plt

Y=[1.4,2.65,3.21,4.55,5.87,6.12,7.09,8.33,9.21,10.67]
L=len(Y)

X=np.zeros((L))

sx=0
sx2=0
sy=0
sxy=0

for i in range(L):
    X[i]=i+1
    sx=sx+X[i]
    sx2=sx2+X[i]**2
    sy=sy+Y[i]
    sxy=sxy+X[i]*Y[i]

a=(L*sxy-sx*sy)/(L*sx2-sx**2)
b=(sy-a*sx)/L

Ya=np.zeros((L))
for i in range(L):
    Ya[i]=a*X[i]+b

plt.figure(1)
plt.title('Ajuste por minimos cuadrados')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.plot(X,Y,'r')
plt.plot(X,Ya,'k+')
plt.legend(['Datos','Datos ajustados'])
plt.savefig('minimos_cuadrados.png')

