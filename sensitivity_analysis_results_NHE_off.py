import os
import sys

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

source_folder = "./results/sensitivity_analysis/rat_model/"

metrics_data = pd.read_csv(os.path.join(source_folder,"rat_model_sensitivity_analysis.csv"),index_col=0)

metrics_of_interest = ["Na_i[mM]","Ca_i_diast[uM]","Ca_i_max[uM]","T_max[kPa]","mean_pH_i[-]"]
metrics_data = metrics_data[metrics_of_interest]
ylabels = list(metrics_data.columns)

parameters = ["pCa","Cab","Jrel","NCX","Juptake","CaL","Jleak"]
parameters += ["Cl","Kss","K1","Kt","Kf","Ko","NaK","Na","Nab","Kb","Naf"]
parameters += ["CHE","AE","NCB","H"]

# add one row for 0 sensitivities for NHE 
S = np.zeros((len(parameters),len(ylabels)+1))
for i in range(len(parameters)):
	sims_to_extract = [f"{parameters[i]}_50", f"{parameters[i]}_150"]

	metrics_i = np.array(metrics_data.loc[sims_to_extract])
	S[i,:] = metrics_i[1,:] - metrics_i[0,:]

# normalise by the maximum effect on each output
S_norm = S/np.max(np.abs(S),axis=0)

S_df = pd.DataFrame(S,columns=ylabels,index=parameters+["NHE"])
S_df.to_csv(os.path.join(source_folder,"rat_model_sensitivity_index.csv"))

S_norm_df = pd.DataFrame(S_norm,columns=ylabels,index=parameters)
S_norm_df.to_csv(os.path.join(source_folder,"rat_model_sensitivity_index_norm.csv"))

# ---------
# plot
cbar_args = {"orientation": "horizontal",
			 'ticks': [-1,0,1],
			 'label': 'Normalised Sensitivity [-]'}
ylabels_tex = ["$Na_i$",
               "$Ca_{i,diast}$",
               "$Ca_{i,max}$",
               "$T_{max}$",
               "$pH_i$"]
parameters_tex = ["$pCa$","$Ca_b$","$J_{rel}$","$NCX$","$J_{up}$","$CaL$","$J_{leak}$"]
parameters_tex += ["$Cl$","$K_{ss}$","$K_1$","$K_t$","$K_f$","$K_o$","$NaK$","$Na$","$Na_b$","$K_b$","$Na_f$"]
parameters_tex += ["$CHE$","$AE$","$NCB$","$H$","$NHE$"]

sns.set(font_scale=1.05, rc={'text.usetex' : True})
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

fig,ax = plt.subplots(1,1,figsize=(12,4))
ax=sns.heatmap(S_norm_df.transpose(), 
			annot=False, 
			cmap='coolwarm_r', 
			vmin=-1, 
			vmax=1,
			linewidths=1.0,
			square=True,
			cbar_kws=cbar_args,
			xticklabels=parameters_tex,
			yticklabels=ylabels_tex)
ax.axes.set_title("Sensitivity Analysis",fontweight="bold",fontsize=16)
plt.tight_layout()
plt.savefig(os.path.join(source_folder,"sensitivity_analysis_norm.png"),dpi=300)
plt.close('all')

