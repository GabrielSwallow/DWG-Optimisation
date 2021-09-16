import julia
julia.Julia(runtime="C:\\Users\\gabri\\AppData\\Local\\Programs\\Julia-1.5.4\\bin\\julia.exe")
from julia import Main

Main.using("Luna")

# Arguments
radius = 125e-6 # HCF core radius
flength = 3 # HCF length
gas = "Ar"
pressure = 80e-3 # gas pressure in bar
λ0 = 800e-9 # central wavelength of the pump pulse
τfwhm = 10e-15 # FWHM duration of the pump pulse
energy = 60e-6 # energy in the pump pulse

# Assign arguments to Main namespace
Main.radius = radius
Main.flength = flength

Main.gas_str = gas
Main.eval("gas = Symbol(gas_str)")

Main.pressure = pressure
Main.λ0 = λ0
Main.τfwhm = τfwhm
Main.energy = energy

# Calculations
Main.duv = Main.eval('prop_capillary(radius, flength, gas, pressure; λ0, τfwhm, energy, modes=4, trange=400e-15, λlims=(150e-9, 4e-6))')