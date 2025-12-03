import os
import sys
import numpy as np
import pandas as pd

Nbeats_to_plot = 3
BCL = 1000
dt = 1
N_from_end = int(BCL/dt)*Nbeats_to_plot+1
N_last = int(BCL/dt)+1

N_outputs = 4

output_labels = ["Na_i[mM]",
                 "Ca_i_diast[uM]","Ca_i_max[uM]","Ca_i_ampl[uM]"]

def get_last_beats(simulation_folder):

    time = np.loadtxt(os.path.join(simulation_folder,"split_29","time.dat"))
    states = np.loadtxt(os.path.join(simulation_folder,"split_29","states.dat"))
    algebraic = np.loadtxt(os.path.join(simulation_folder,"split_29","algebraic.dat"))

    states = states[:,-N_from_end:]
    algebraic = algebraic[:,-N_from_end:]
    time = time[-N_from_end:]

    na_i = states[1,:] # mM
    ca_i = states[4,:]*1e03 # microM

    return time,na_i,ca_i

def get_last_beat_outputs(simulation_folder):

    time = np.loadtxt(os.path.join(simulation_folder,"split_29","time.dat"))
    states = np.loadtxt(os.path.join(simulation_folder,"split_29","states.dat"))
    algebraic = np.loadtxt(os.path.join(simulation_folder,"split_29","algebraic.dat"))

    states = states[:,-N_last:]
    algebraic = algebraic[:,-N_last:]
    time = time[-N_last:]

    na_i = states[1,:] # mM
    ca_i = states[4,:]*1e03 # microM

    na_i_ss      = na_i[-1]
    ca_i_diast   = ca_i[-1]
    ca_i_peak    = np.max(ca_i)
    ca_i_ampl    = ca_i_peak - ca_i_diast

    return na_i_ss,ca_i_diast,ca_i_peak,ca_i_ampl

source_folder = "/media/mstrocch/MS_5/SGLT2i_Mike_Shattock/rabbit_model_shannon_bers/"
output_folder = "./rabbit_model/"
if not os.path.exists(output_folder):
    os.system("mkdir -p "+output_folder)

folders = ["baseline",
           "baseline_Km50",
           "baseline_Km60",
           "baseline_Km70",
           "baseline_Km80",
           "baseline_Km90",
           "baseline_Km110",
           "baseline_Km120",
           "baseline_Km130",
           "baseline_Km140",
           "baseline_Km150"]

output_data = np.zeros((len(folders),N_outputs),dtype=float)

for i,f in enumerate(folders):
    sim_folder = os.path.join(source_folder,f)
    out_folder = os.path.join(output_folder,f)
    if not os.path.exists(out_folder):
        os.system("mkdir -p "+out_folder)

    print("Extracting data from "+out_folder+"...")

    time,na_i,ca_i = get_last_beats(sim_folder)

    np.savetxt(os.path.join(out_folder,"time.dat"),time,fmt="%.2f")
    np.savetxt(os.path.join(out_folder,"na_i.dat"),na_i,fmt="%.6f")
    np.savetxt(os.path.join(out_folder,"ca_i.dat"),ca_i,fmt="%.6f")

    output_data[i,:] = get_last_beat_outputs(sim_folder)

df_data = pd.DataFrame(output_data,index=folders,columns=output_labels,dtype=float)
df_data.to_csv(os.path.join(output_folder,"rabbit_model_metrics.csv"),float_format="%g")