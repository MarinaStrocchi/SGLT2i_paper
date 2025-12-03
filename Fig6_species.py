import os
import sys

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig_folder = "./figures/"
if not os.path.exists(fig_folder):
    os.system("mkdir -p "+fig_folder)

source_folder = "./rat_model/"
metrics_data = pd.read_csv(os.path.join(source_folder,"rat_model_metrics.csv"),index_col=0)

rat_color    = "deepskyblue"
rabbit_color = "tab:red"
human_color  = "gray"

fig = plt.figure(constrained_layout=True, figsize=(9,3))
grid = fig.add_gridspec(1,3)
plt.rcParams['font.size'] = 9
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['text.usetex'] = True

ax00 = plt.subplot(grid[0, 0])
ax01 = plt.subplot(grid[0, 1], sharex=ax00)
ax02 = plt.subplot(grid[0, 2], sharex=ax00)

sims_to_compare = ["baseline_Tref_pH_Km50",
				   "baseline_Tref_pH_Km60",
				   "baseline_Tref_pH_Km70",
				   "baseline_Tref_pH_Km80",
				   "baseline_Tref_pH_Km90",
				   "baseline_Tref_pH",
				   "baseline_Tref_pH_Km110",
				   "baseline_Tref_pH_Km120",
				   "baseline_Tref_pH_Km130",
				   "baseline_Tref_pH_Km140",
				   "baseline_Tref_pH_Km150"]
sizes = [20]*len(sims_to_compare)
sizes[5] = 60
extracted_data = metrics_data.loc[sims_to_compare]

baseline_Na = 11.6436
NHE_off_Na  = 10.8638
pp_NHE_off = (baseline_Na-NHE_off_Na)/baseline_Na

range_diast = 0.01
range_max   = 0.2
range_ampl  = 0.2

rect = patches.Rectangle((baseline_Na*(1-pp_NHE_off), extracted_data["Ca_i_diast[uM]"][5]-0.5*range_diast), 
						 baseline_Na*pp_NHE_off,range_diast,
						 edgecolor='none', facecolor=rat_color,alpha=0.3)
ax00.add_patch(rect)

rect = patches.Rectangle((baseline_Na*(1-pp_NHE_off), extracted_data["Ca_i_max[uM]"][5]-0.5*range_max), 
						 baseline_Na*pp_NHE_off,range_max,
						 edgecolor='none', facecolor=rat_color,alpha=0.3)
ax01.add_patch(rect)

rect = patches.Rectangle((baseline_Na*(1-pp_NHE_off), extracted_data["Ca_i_ampl[uM]"][5]-0.5*range_ampl), 
						 baseline_Na*pp_NHE_off,range_ampl,
						 edgecolor='none', facecolor=rat_color,alpha=0.3)
ax02.add_patch(rect)

ax00.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],color=rat_color,zorder=1)
ax00.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],s=sizes,color=rat_color,facecolor="white")
ax00.set_xlabel("$[Na^+]_i$ [mM]")
ax00.set_ylabel("$[Ca^{2+}]_{i,diast}$ [$\mu$M]")

ax01.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],color=rat_color,zorder=1)
ax01.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],s=sizes,color=rat_color,facecolor="white")
ax01.set_xlabel("$[Na^+]_i$ [mM]")
ax01.set_ylabel("$[Ca^{2+}]_{i,max}$ [$\mu$M]")

ax02.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],color=rat_color,zorder=1)
ax02.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],s=sizes,color=rat_color,facecolor="white")
ax02.set_xlabel("$[Na^+]_i$ [mM]")
ax02.set_ylabel("$[Ca^{2+}]_{i,ampl}$ [$\mu$M]")

# ------------------------------
source_folder = "./rabbit_model/"
metrics_data = pd.read_csv(os.path.join(source_folder,"rabbit_model_metrics.csv"),index_col=0)

sims_to_compare = ["baseline_Km50",
				   "baseline_Km60",
				   "baseline_Km70",
				   "baseline_Km80",
				   "baseline_Km90",
				   "baseline",
				   "baseline_Km110",
				   "baseline_Km120",
				   "baseline_Km130",
				   "baseline_Km140",
				   "baseline_Km150"]
sizes = [20]*len(sims_to_compare)
sizes[5] = 60
extracted_data = metrics_data.loc[sims_to_compare]

baseline_Na = extracted_data["Na_i[mM]"][5]

rect = patches.Rectangle((baseline_Na*(1-pp_NHE_off), extracted_data["Ca_i_diast[uM]"][5]-0.5*range_diast), 
						 baseline_Na*pp_NHE_off,range_diast,
						 edgecolor='none', facecolor=rabbit_color,alpha=0.3)
ax00.add_patch(rect)

rect = patches.Rectangle((baseline_Na*(1-pp_NHE_off), extracted_data["Ca_i_max[uM]"][5]-0.5*range_max), 
						 baseline_Na*pp_NHE_off,range_max,
						 edgecolor='none', facecolor=rabbit_color,alpha=0.3)
ax01.add_patch(rect)

rect = patches.Rectangle((baseline_Na*(1-pp_NHE_off), extracted_data["Ca_i_ampl[uM]"][5]-0.5*range_ampl), 
						 baseline_Na*pp_NHE_off,range_ampl,
						 edgecolor='none', facecolor=rabbit_color,alpha=0.3)
ax02.add_patch(rect)

ax00.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],color=rabbit_color,zorder=1)
ax00.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],s=sizes,color=rabbit_color,
			 facecolor="white",marker='s')
ax00.set_xlabel("$[Na^+]_i$ [mM]")
ax00.set_ylabel("$[Ca^{2+}]_{i,diast}$ [$\mu$M]")

ax01.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],color=rabbit_color,zorder=1)
ax01.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],s=sizes,color=rabbit_color,
			 facecolor="white",marker='s')
ax01.set_xlabel("$[Na^+]_i$ [mM]")
ax01.set_ylabel("$[Ca^{2+}]_{i,max}$ [$\mu$M]")

ax02.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],color=rabbit_color,zorder=1)
ax02.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],s=sizes,color=rabbit_color,
			 facecolor="white",marker='s')
ax02.set_xlabel("$[Na^+]_i$ [mM]")
ax02.set_ylabel("$[Ca^{2+}]_{i,ampl}$ [$\mu$M]")

# ------------------------------
source_folder = "./human_model/"
metrics_data = pd.read_csv(os.path.join(source_folder,"human_model_metrics.csv"),index_col=0)

sims_to_compare = ["baseline_Km50",
				   "baseline_Km60",
				   "baseline_Km70",
				   "baseline_Km80",
				   "baseline_Km90",
				   "baseline",
				   "baseline_Km110",
				   "baseline_Km120",
				   "baseline_Km130",
				   "baseline_Km140",
				   "baseline_Km150"]
sizes = [20]*len(sims_to_compare)
sizes[5] = 60
extracted_data = metrics_data.loc[sims_to_compare]

baseline_Na = extracted_data["Na_i[mM]"][5]

rect = patches.Rectangle((baseline_Na*(1-pp_NHE_off), extracted_data["Ca_i_diast[uM]"][5]-0.5*range_diast), 
						 baseline_Na*pp_NHE_off,range_diast,
						 edgecolor='none', facecolor=human_color,alpha=0.3)
ax00.add_patch(rect)

rect = patches.Rectangle((baseline_Na*(1-pp_NHE_off), extracted_data["Ca_i_max[uM]"][5]-0.5*range_max), 
						 baseline_Na*pp_NHE_off,range_max,
						 edgecolor='none', facecolor=human_color,alpha=0.3)
ax01.add_patch(rect)

rect = patches.Rectangle((baseline_Na*(1-pp_NHE_off), extracted_data["Ca_i_ampl[uM]"][5]-0.5*range_ampl), 
						 baseline_Na*pp_NHE_off,range_ampl,
						 edgecolor='none', facecolor=human_color,alpha=0.3)
ax02.add_patch(rect)

ax00.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],color=human_color,zorder=1)
ax00.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],s=sizes,color=human_color,
			 facecolor="white",marker='d')
ax00.set_xlabel("$[Na^+]_i$ [mM]")
ax00.set_ylabel("$[Ca^{2+}]_{i,diast}$ [$\mu$M]")

ax01.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],color=human_color,zorder=1)
ax01.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],s=sizes,color=human_color,
			 facecolor="white",marker='d')
ax01.set_xlabel("$[Na^+]_i$ [mM]")
ax01.set_ylabel("$[Ca^{2+}]_{i,max}$ [$\mu$M]")

ax02.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],color=human_color,zorder=1)
ax02.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],s=sizes,color=human_color,
			 facecolor="white",marker='d')
ax02.set_xlabel("$[Na^+]_i$ [mM]")
ax02.set_ylabel("$[Ca^{2+}]_{i,ampl}$ [$\mu$M]")

plt.tight_layout()
plt.savefig(os.path.join(fig_folder,"Figure6.png"),dpi=300)