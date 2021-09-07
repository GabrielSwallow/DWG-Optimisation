import numpy as np
import random as rd
import time
import matplotlib.pyplot as plt
import plotparams

#import julia, the api module
import julia
#julia.Main is used to add and access atributes to the julia namespace
#inside Main.eval(), don't need Main.<atribute>, can just access via <attribute>
from julia import Main

#Julia.eval() runs julia code. Set as jl to simplify syntax
#jl = julia.Julia(compiled_modules=False)


#jl.using("TextAnalysis") - imports Julia packages needed in .jl if need be file




####
#Running julia in python directly
####
#t1 = time.perf_counter()

#define the data in python
data1=[1,2,3,4,5]

#define the data in the julia-readable object julia.Main
Main.data_j1 = data1

#define a julia function
Main.eval("func(x) = x^2")
#run and return the values back to a python object

out1 = Main.eval("func.(data_j1)")


#t2 = time.perf_counter()
#time_jl = t2-t1





####
#Running a julia file in python
####
data2= np.linspace(-100,100,1000)
Main.data_j2 = data2

Main.eval('include("Playground.jl")')
out2 = Main.eval("sqr.(data_j2)")


plt.plot(data2, out2)
plt.ylim(0, 10000)
plt.grid()
plt.show()







#%% test
#from julia import Base ##  basic julia functions to run
#print(Base.sind(90))
#from julia import Main
#julia.install() installs PyCall (only needed once. Import julia, then install)