import os
import sys

import numpy as np

# In the original rat model, SERCA (algebraic[90]) is modelled as 
# g_SERCA * (Cai^2/(Cai^2+k_SERCA^2))
# where 
# g_SERCA = 0.00045 constants[95]
# k_SERCA = 0.0005 constants[96]

# in the model with pH regulation (eq 2 from Crampin and Smith 2006)
# there are no squares in Cai and k_SERCA and g_SERCA (Jup_infinity) is 0.036

Jup_infinity = 0.036
n_up = 1.14
pKup = 7.53

# this is the variable in the model
pH = 7.2

g_SERCA_pH = Jup_infinity / (1.0 + np.power(10.0000, n_up * (-pH + pKup)))

print(f"g_SERCA_pH : {g_SERCA_pH} vs original value of 0.00045") # g_SERCA_pH : 0.011472413934009825 much bigger than the original value of 0.00045

# ---------------
# alternative 

g_SERCA = 0.00045
pH_ref = 7.15
pH_high = 7.4
pH_low  = 7.1

g_SERCA_pH_ref = g_SERCA * (1.0 + np.power(10.0000, n_up * (-pH_ref + pKup)))/(1.0 + np.power(10.0000, n_up * (-pH_ref + pKup)))
g_SERCA_pH_high = g_SERCA * (1.0 + np.power(10.0000, n_up * (-pH_ref + pKup)))/(1.0 + np.power(10.0000, n_up * (-pH_high + pKup)))
g_SERCA_pH_low = g_SERCA * (1.0 + np.power(10.0000, n_up * (-pH_ref + pKup)))/(1.0 + np.power(10.0000, n_up * (-pH_low + pKup)))

print(f"g_SERCA_pH reference 7.15 : {g_SERCA_pH_ref} ")
print(f"g_SERCA_pH high pH 7.4 : {g_SERCA_pH_high} ")
print(f"g_SERCA_pH low pH 7.1 (acidosis) : {g_SERCA_pH_low} ")

def SERCA_factor_pH(pH):

	return (1.0 + np.power(10.0000, n_up * (-pH_ref + pKup)))/(1.0 + np.power(10.0000, n_up * (-pH + pKup)))

print(f"Factor reference 7.15 : {SERCA_factor_pH(pH_ref)} ") # 1.0
print(f"Factor high pH 7.4 : {SERCA_factor_pH(pH_high)} ") # 1.54
print(f"Factor low pH 7.1 (acidosis) : {SERCA_factor_pH(pH_low)} ") # 0.91

