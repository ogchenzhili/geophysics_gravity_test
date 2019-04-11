from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class two_dimensional_gravity():
    def __init__(self,anormal_h,anormal_r,residual_density,range_x,rang_y,filename):
        self.anormal_h=anormal_h
        self.anormal_r=anormal_r
        self.residual_density=residual_density
        self.range_x=range_x
        self.range_y=rang_y
        self.quality=6.67e-11*4.0/3*3.1415926*(self.anormal_r**3)*self.residual_density
        self.filename=filename

    def Anormal(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        self.range_x, self.range_y = np.meshgrid(self.range_x, self.range_y)
        Z =(self.quality*self.anormal_h)/(np.sqrt(self.range_x**2+self.range_y**2+self.anormal_h**2))**3
        ax.plot_surface(self.range_x, self.range_y, Z, rstride=1, cstride=1, cmap='rainbow')
        self.text_save(self.filename,Z)
        plt.show()


    def Deflector_xz(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        self.range_x, self.range_y = np.meshgrid(self.range_x, self.range_y)
        Z =-3*self.quality*self.anormal_h*self.range_x/((np.sqrt(self.range_x**2+self.range_y**2+self.anormal_h**2))**5)
        ax.plot_surface(self.range_x, self.range_y, Z, rstride=1, cstride=1, cmap='rainbow')
        self.text_save(self.filename,Z)
        plt.show()

    def Deflector_zz(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        self.range_x, self.range_y = np.meshgrid(self.range_x, self.range_y)
        Z =self.range_x*(2*self.anormal_h*self.anormal_h-self.range_y**2-self.range_x**2)/((np.sqrt(self.range_x**2+self.range_y**2+self.anormal_h**2))**5)
        ax.plot_surface(self.range_x, self.range_y, Z, rstride=1, cstride=1, cmap='rainbow')
        self.text_save(self.filename,Z)
        plt.show()

    def Deflector_xy(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        self.range_x, self.range_y = np.meshgrid(self.range_x, self.range_y)
        Z =3*self.range_x*self.range_y/((np.sqrt(self.range_x**2+self.range_y**2+self.anormal_h**2))**5)
        ax.plot_surface(self.range_x, self.range_y, Z, rstride=1, cstride=1, cmap='rainbow')
        self.text_save(self.filename,Z)
        plt.show()

    def text_save(self,data3):
        file=open(filename,"w")
        for i in range(len(self.range_y)):
            for j in range(len(self.range_x)):
                s1=str(self.range_x[1][j])
                s2=str(self.range_y[i][1])
                s3=str(data3[i][j])
                file.write(s1)
                file.write('\t')
                file.write(s2)
                file.write('\t')
                file.write(s3)
                file.write('\n')
        file.close()

if __name__=="__main__":
    two_dimensional_gravity=two_dimensional_gravity(20,200,100,np.arange(-300, 300, 3),np.arange(-300, 300, 3),"文件")
    two_dimensional_gravity.Deflector_xy()
    two_dimensional_gravity.Deflector_xz()
    two_dimensional_gravity.Deflector_zz()