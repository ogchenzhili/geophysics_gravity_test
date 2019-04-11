from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import spline
class one_dimensional_gravity():

    def __init__(self,anormal_h,anormal_r,residual_density,range_x,filename):
        self.anormal_h=anormal_h
        self.anormal_r=anormal_r
        self.residual_density=residual_density
        self.range_x=range_x
        self.quality=6.67e-11*4.0/3*3.1415926*(self.anormal_r**3)*self.residual_density
        self.filename=filename

    def text_save(self,data_y):
        file=open(self.filename,"w")
        for i in range(len(self.range_x)):
            s1=str(self.range_x[i])
            s2=str(data_y[i])
            file.write(s1)
            file.write('\t')
            file.write(s2)
            file.write('\n')
        file.close()


    def Deflector_xy(self):
        v=[]
        for x in self.range_x:
            v.append(3*x/((np.sqrt(x**2+1+self.anormal_h**2))**5))
        self.Drafting(v)

    def Deflector_xy_save(self):
        v=[]
        for x in self.range_x:
            v.append(3*x/((np.sqrt(x**2+1+self.anormal_h**2))**5))
        self.text_save(self.filename,v)   
        self.Drafting(v)

    def Deflector_xz(self):
        v=[]
        for x in self.range_x:
            v.append(-3*self.quality*self.anormal_h*x/((np.sqrt(x**2+self.anormal_h**2))**5))
        self.Drafting(v)

    def Deflector_xz_save(self):
        v=[]
        for x in self.range_x:
            v.append(-3*self.quality*self.anormal_h*x/((np.sqrt(x**2+self.anormal_h**2))**5))
        self.text_save(self.filename,v)
        self.Drafting(v)

    def Deflector_zz(self):#y=0,z=0
        v=[]
        for x in self.range_x:
            v.append(self.quality*(2*self.anormal_h*self.anormal_h-x**2)/((np.sqrt(x**2+self.anormal_h**2))**5))
        self.Drafting(v)

    def Deflector_zz_save(self):#y=0,z=0
        v=[]
        for x in self.range_x:
            v.append(self.quality*(2*self.anormal_h*self.anormal_h-x**2)/((np.sqrt(x**2+self.anormal_h**2))**5))
        self.text_save(self.filename,v)
        self.Drafting(v)

    def Anormal(self):#y=0,z=0
        g=[]
        for x in self.range_x:
            g.append((self.quality*self.anormal_h)/(np.sqrt(x**2+self.anormal_h**2))**3)
        self.Drafting(g)

    def Anormal_save(self):#y=0,z=0
        g=[]
        for x in self.range_x:
            g.append((self.quality*self.anormal_h)/(np.sqrt(x**2+self.anormal_h**2))**3)
        self.text_save(self.filename,g)
        self.Drafting(g)

    def Drafting(self,Y):
        T = np.array(self.range_x)
        power = np.array(Y)
        xnew = np.linspace(T.min(),T.max(),300) 
        power_smooth = spline(T,power,xnew)
        plt.plot(xnew,power_smooth)
        plt.show()

if __name__ == "__main__":
    one_dimensional_gravity=one_dimensional_gravity(200,20,100,np.arange(-300, 300, 1),"文件")
    one_dimensional_gravity.Deflector_xz()
    one_dimensional_gravity.Deflector_zz()
    one_dimensional_gravity.Deflector_xy()
    one_dimensional_gravity.Anormal()