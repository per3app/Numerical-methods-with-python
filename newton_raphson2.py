#newton raphson
import numpy as np
import matplotlib.pyplot as plt

n=8             #limite del eje x
X=np.zeros((n))     #vector vacio del eje x

F=np.zeros((n))
DF=np.zeros((n))
Er=np.zeros((n))
print('-----------------------------')
print('    X           Error')
for i in range(n-1):
    X[0]=2                      #valor inicial
    F[i]=4*X[i]**3-3*X[i]         #funcion 
    DF[i]=12*X[i]**2-3              #derivada de la funcion
    X[i+1]=X[i]-F[i]/DF[i]
    Er[i]=X[i+1]-X[i]
    s='{0:3.5f}     {1:3.5e}'.format(X[i],Er[i])
    print(s)
print('-----------------------------')
for i in range(n):
    s='{0:2.4f}'.format(Er[i])
    if abs(Er[i])<0.00000000005:
        print(s,'Error permitido')
        
    else:
        print(s,'Error no permitido')
print('-----------------------------')
plt.plot(X,Er,'ro')
plt.plot(X,Er,'b--')
plt.grid(True)

plt.ylabel('Error')
plt.xlabel('X')
plt.title('X vs Error')
plt.show()
