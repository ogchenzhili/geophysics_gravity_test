from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def text_save(filename,data1,data2,data3):
    file=open(filename,"w")
    for i in range(len(data2)):
        for j in range(len(data1)):
            
            s1=str(data1[1][j])
            s2=str(data2[i][1])
            s3=str(data3[i][j])
            file.write(s1)
            file.write('\t')
            file.write(s2)
            file.write('\t')
            file.write(s3)
            file.write('\n')
    file.close()


def Anormal(X,Y):
    anormal_h=200
    fig = plt.figure()
    ax = Axes3D(fig)
    X, Y = np.meshgrid(X, Y)
    Z =(k_m*anormal_h)/(np.sqrt(X**2+Y**2+anormal_h**2))**3
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    text_save("E:\\python\\data1\\二维变量\\Anormal_g.txt",X,Y,Z)
    plt.show()


def Deflector_xz(X,Y):
    anormal_h=200
    fig = plt.figure()
    ax = Axes3D(fig)
    X, Y = np.meshgrid(X, Y)
    Z =-3*k_m*anormal_h*X/((np.sqrt(X**2+Y**2+anormal_h**2))**5)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    text_save("E:\\python\\data1\\二维变量\\Deflector_xz.txt",X,Y,Z)
    plt.show()

def Deflector_zz(X,Y):
    anormal_h=200
    fig = plt.figure()
    ax = Axes3D(fig)
    X, Y = np.meshgrid(X, Y)
    Z =k_m*(2*anormal_h*anormal_h-Y**2-X**2)/((np.sqrt(X**2+Y**2+anormal_h**2))**5)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    text_save("E:\\python\\data1\\二维变量\\Deflector_zz.txt",X,Y,Z)
    plt.show()

def Deflector_xy(X,Y):
    anormal_h=200
    fig = plt.figure()
    ax = Axes3D(fig)
    X, Y = np.meshgrid(X, Y)
    Z =3*X*Y/((np.sqrt(X**2+Y**2+anormal_h**2))**5)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    text_save("E:\\python\\data1\\二维变量\\Deflector_xy.txt",X,Y,Z)
    plt.show()


density_def=100
anormal_r=20
anormal_h=200
quality_def=4.0/3*3.1415926*(anormal_r**3)*density_def
k_m=6.67e-11*quality_def
X = np.arange(-300, 300, 3)
Y = np.arange(-300, 300, 3)
Anormal(X,Y)
Deflector_xz(X,Y)
Deflector_zz(X,Y)
Deflector_xy(X,Y)