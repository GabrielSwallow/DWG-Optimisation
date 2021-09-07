import numpy as np
import random as rd

#import julia, the api module
import julia
#Used to add atributes to the julia namespace
#in jl.eval(), don't need Main.atr, can just access via atr
from julia import Main

#shorter syntax
jl = julia.api.Julia(compiled_modules=False)

#used to illustrate speed of computation
import time

#jl.using("TextAnalysis") - imports Julia packages needed in OG file


#%%
#Running julia in python directly
####
t1 = time.perf_counter()
#define the data in python
data1=[1,2,3,4,5]

#define the data in the julia-readable object julia.Main
Main.data_j1 = data1

#define a julia function
jl.eval("func(x) = x^2")
#run and return the values back to a python object
out1 = jl.eval("func.(data_j1)")
t2 = time.perf_counter()

time_jl = t2-t1

#%%
#Running a julia file in python
####
data2=[10,11,12,13,14,15]
Main.data_j2 = data2

jl.eval('include("Playground.jl")')
out2 = jl.eval("sqr.(data_j2)")

print(out1)
print(out2)




#%%
#Python time comparison
####
t1 = time.perf_counter()

data1=[rd.randint(1, 10) for i in range(100000000)]
out1_py=[]
for i in data1:
    out1_py.append(i*i)

t2 = time.perf_counter()

time_py = t2-t1

#%% test
#from julia import Base ##  basic julia functions to run
#print(Base.sind(90))
#from julia import Main
#julia.install() installs PyCall (only needed once. Import julia, then install)