from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import spline

def text_save(filename,data1,data2):
    file=open(filename,"w")
    for i in range(len(data1)):
        s1=str(data1[i])
        s2=str(data2[i])
        file.write(s1)
        file.write('\t')
        file.write(s2)
        file.write('\n')
    file.close()


def Drafting(X,Y):#制图显示
    T = np.array(X)
    power = np.array(Y)
    xnew = np.linspace(T.min(),T.max(),300) 
    power_smooth = spline(T,power,xnew)
    plt.plot(xnew,power_smooth)
    plt.show()



def Anormal(X):#y=0,z=0
    anormal_h=200
    g=[]
    for x in X:
        g.append((k_m*anormal_h)/(np.sqrt(x**2+anormal_h**2))**3)
    text_save("E:\\python\\data1\\Anormal_g.txt",X,g)
    Drafting(X,g)

def Deflector_xz(X):#y=0,z=0
    anormal_h=200
    v=[]
    for x in X:
        v.append(-3*k_m*anormal_h*x/((np.sqrt(x**2+anormal_h**2))**5))
    text_save("E:\\python\\data1\\V_xz.txt",X,v)
    Drafting(X,v)


def Deflector_zz(X):#y=0,z=0
    anormal_h=200
    v=[]
    for x in X:
        v.append(k_m*(2*anormal_h*anormal_h-x**2)/((np.sqrt(x**2+anormal_h**2))**5))
    text_save("E:\\python\\data1\\V_zz.txt",X,v)
    Drafting(X,v)


def Deflector_xy(X):#y=1,z=0
    anormal_h=200
    v=[]
    for x in X:
        v.append(3*x/((np.sqrt(x**2+1+anormal_h**2))**5))
    text_save("E:\\python\\data1\\V_xy.txt",X,v)
    Drafting(X,v)

density_def=100
anormal_r=20
anormal_h=200
quality_def=4.0/3*3.1415926*(anormal_r**3)*density_def
k_m=6.67e-11*quality_def
X = np.arange(-300, 300, 1)

Anormal(X)
Deflector_xy(X)
Deflector_xz(X)
Deflector_zz(X)
