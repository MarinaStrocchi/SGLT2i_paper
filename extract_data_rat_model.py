import os
import sys
import numpy as np
import pandas as pd

Nbeats_to_plot = 3
BCL = 1000
dt = 1
N_from_end = int(BCL/dt)*Nbeats_to_plot+1
N_last = int(BCL/dt)+1

N_outputs = 7

output_labels = ["Na_i[mM]","NHE_flux[uM/ms]",
				 "Ca_i_diast[uM]","Ca_i_max[uM]","Ca_i_ampl[uM]",
				 "T_max[kPa]","mean_pH_i[-]"]

def get_last_beats(simulation_folder):

    time = np.loadtxt(os.path.join(simulation_folder,"split_29","time.dat"))
    states = np.loadtxt(os.path.join(simulation_folder,"split_29","states.dat"))
    algebraic = np.loadtxt(os.path.join(simulation_folder,"split_29","algebraic.dat"))

    states = states[:,-N_from_end:]
    algebraic = algebraic[:,-N_from_end:]
    time = time[-N_from_end:]

    na_i = states[1,:]  # mM
    ca_i = states[16,:]*1e03 # microM
    tension = algebraic[137,:] # kPa
    nhe_flux = algebraic[51,:]*1e03 # uM/ms
    ph_i = states[13,:] # dimensionless

    return time,na_i,ca_i,tension,nhe_flux,ph_i

def get_last_beat_outputs(simulation_folder):

    time = np.loadtxt(os.path.join(simulation_folder,"split_29","time.dat"))
    states = np.loadtxt(os.path.join(simulation_folder,"split_29","states.dat"))
    algebraic = np.loadtxt(os.path.join(simulation_folder,"split_29","algebraic.dat"))

    states = states[:,-N_last:]
    algebraic = algebraic[:,-N_last:]
    time = time[-N_last:]

    na_i = states[1,:]  # mM
    ca_i = states[16,:]*1e03 # microM
    tension = algebraic[137,:] # kPa
    nhe_flux = algebraic[51,:]*1e03 # mM/ms
    ph_i = states[13,:] # dimensionless

    na_i_ss      = na_i[-1]
    nhe_flux_max = np.max(np.abs(nhe_flux))
    ca_i_diast   = ca_i[-1]
    ca_i_peak    = np.max(ca_i)
    ca_i_ampl    = ca_i_peak - ca_i_diast
    t_max        = np.max(tension)
    mean_pH_i    = np.mean(ph_i)

    return na_i_ss,nhe_flux_max,ca_i_diast,ca_i_peak,ca_i_ampl,t_max,mean_pH_i

source_folder = "/media/mstrocch/MS_5/SGLT2i_Mike_Shattock/final_experiments/"
output_folder = "./rat_model/"
if not os.path.exists(output_folder):
	os.system("mkdir -p "+output_folder)

folders = ["baseline_pH",
		   "baseline_pH_NHE_off",
		   "baseline_pH_H2",
		   "baseline_pH_H4",
		   "baseline_pH_H6",
		   "baseline_pH_H8",
		   "baseline_pH_H10",
		   "baseline_pH_INab200",
		   "baseline_pH_INab300",
		   "baseline_pH_INab400",
		   "baseline_pH_INab500",
		   "baseline_pH_Km50",
		   "baseline_pH_Km60",
		   "baseline_pH_Km70",
		   "baseline_pH_Km80",
		   "baseline_pH_Km90",
		   "baseline_pH_Km110",
		   "baseline_pH_Km120",
		   "baseline_pH_Km130",
		   "baseline_pH_Km140",
		   "baseline_pH_Km150",
		   "HF_pH",
		   "HF_pH_NHE_off",
		   "low_pH_bicarb_pH",
		   "low_pH_bicarb_pH_NHE_off"]

output_data = np.zeros((len(folders),N_outputs),dtype=float)

for i,f in enumerate(folders):
	sim_folder = os.path.join(source_folder,f)
	out_folder = os.path.join(output_folder,f)
	if not os.path.exists(out_folder):
		os.system("mkdir -p "+out_folder)

	print("Extracting data from "+out_folder+"...")

	time,na_i,ca_i,tension,nhe_flux,ph_i = get_last_beats(sim_folder)

	np.savetxt(os.path.join(out_folder,"time.dat"),time,fmt="%.2f")
	np.savetxt(os.path.join(out_folder,"na_i.dat"),na_i,fmt="%.6f")
	np.savetxt(os.path.join(out_folder,"ca_i.dat"),ca_i,fmt="%.6f")
	np.savetxt(os.path.join(out_folder,"tension.dat"),tension,fmt="%.6f")
	np.savetxt(os.path.join(out_folder,"nhe_flux.dat"),nhe_flux,fmt="%g")

	output_data[i,:] = get_last_beat_outputs(sim_folder)

df_data = pd.DataFrame(output_data,index=folders,columns=output_labels,dtype=float)
df_data.to_csv(os.path.join(output_folder,"rat_model_metrics.csv"),float_format="%g")