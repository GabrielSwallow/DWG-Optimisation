# DWG-Optimisation
This project started work towards optimising parameters of the Luna prop_capillary method

Current Progress:
Interactive comparison plots for a single mode of the signal. The peak gives some indication of how effective 
the paremeters are at minimising peak wavelength.
Default values are assigned for all but 1 parameter, which is varied about its default value.

We have also been able to run the simulation via a python script, allowing for plotting and optimisation in python.


## Files:
### DUV_comparison_plots.jl
Interactive plotting tool. Allows comparison of how different parameters vary the single mode of the signal
## Sim_python
Runs the Luna prop_capillary method in python

## time_1d_edit.jl
A Luna function time_1d() was edited to allow for multiple plots to be made on the same figure
## plotparams.py
attractive matplotlib.pyplot parameters for plotting in Python
 
