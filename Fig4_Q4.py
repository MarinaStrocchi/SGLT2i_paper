import os
import sys

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

source_folder = "./rat_model/"
fig_folder = "./figures/"
if not os.path.exists(fig_folder):
    os.system("mkdir -p "+fig_folder)

metrics_data = pd.read_csv(os.path.join(source_folder,"rat_model_metrics.csv"),index_col=0)

color = "deepskyblue"

fig = plt.figure(constrained_layout=True, figsize=(8,6))
grid = fig.add_gridspec(3,4)
plt.rcParams['font.size'] = 9
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['text.usetex'] = True

ax00 = plt.subplot(grid[0, 0])
ax01 = plt.subplot(grid[0, 1], sharex=ax00)
ax02 = plt.subplot(grid[0, 2], sharex=ax00)
ax03 = plt.subplot(grid[0, 3], sharex=ax00)

ax10 = plt.subplot(grid[1, 0], sharex=ax00, sharey=ax00)
ax11 = plt.subplot(grid[1, 1], sharex=ax00, sharey=ax01)
ax12 = plt.subplot(grid[1, 2], sharex=ax00, sharey=ax02)
ax13 = plt.subplot(grid[1, 3], sharex=ax00, sharey=ax03)

ax20 = plt.subplot(grid[2, 0], sharex=ax00, sharey=ax00)
ax21 = plt.subplot(grid[2, 1], sharex=ax00, sharey=ax01)
ax22 = plt.subplot(grid[2, 2], sharex=ax00, sharey=ax02)
ax23 = plt.subplot(grid[2, 3], sharex=ax00, sharey=ax03)

sims_to_compare = ["baseline_pH",
				   "baseline_pH_Km110",
				   "baseline_pH_Km120",
				   "baseline_pH_Km130",
				   "baseline_pH_Km140",
				   "baseline_pH_Km150"]
sizes = [20]*len(sims_to_compare)
sizes[0] = 60
extracted_data = metrics_data.loc[sims_to_compare]

ax00.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],color=color,zorder=1)
ax00.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],s=sizes,color=color,facecolor='white')
ax00.set_xlabel("$[Na^+]_i$ [mM]")
ax00.set_ylabel("$[Ca^{2+}]_{i,diast}$ [$\mu$M]")

ax01.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],color=color,zorder=1)
ax01.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],s=sizes,color=color,facecolor='white')
ax01.set_xlabel("$[Na^+]_i$ [mM]")
ax01.set_ylabel("$[Ca^{2+}]_{i,max}$ [$\mu$M]")

ax02.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],color=color,zorder=1)
ax02.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],s=sizes,color=color,facecolor='white')
ax02.set_xlabel("$[Na^+]_i$ [mM]")
ax02.set_ylabel("$[Ca^{2+}]_{i,ampl}$ [$\mu$M]")

ax03.plot(extracted_data["Na_i[mM]"],extracted_data["T_max[kPa]"],color=color,zorder=1)
ax03.scatter(extracted_data["Na_i[mM]"],extracted_data["T_max[kPa]"],s=sizes,color=color,facecolor='white')
ax03.set_xlabel("$[Na^+]_i$ [mM]")
ax03.set_ylabel("$T_{max}$ [kPa]")

sims_to_compare = ["baseline_pH",
				   "baseline_pH_INab200",
				   "baseline_pH_INab300",
				   "baseline_pH_INab400",
				   "baseline_pH_INab500"]
sizes = [20]*len(sims_to_compare)
sizes[0] = 60
extracted_data = metrics_data.loc[sims_to_compare]

ax10.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],color=color,zorder=1)
ax10.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],s=sizes,color=color,facecolor='white')
ax10.set_xlabel("$[Na^+]_i$ [mM]")
ax10.set_ylabel("$[Ca^{2+}]_{i,diast}$ [$\mu$M]")

ax11.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],color=color,zorder=1)
ax11.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],s=sizes,color=color,facecolor='white')
ax11.set_xlabel("$[Na^+]_i$ [mM]")
ax11.set_ylabel("$[Ca^{2+}]_{i,max}$ [$\mu$M]")

ax12.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],color=color,zorder=1)
ax12.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],s=sizes,color=color,facecolor='white')
ax12.set_xlabel("$[Na^+]_i$ [mM]")
ax12.set_ylabel("$[Ca^{2+}]_{i,ampl}$ [$\mu$M]")

ax13.plot(extracted_data["Na_i[mM]"],extracted_data["T_max[kPa]"],color=color,zorder=1)
ax13.scatter(extracted_data["Na_i[mM]"],extracted_data["T_max[kPa]"],s=sizes,color=color,facecolor='white')
ax13.set_xlabel("$[Na^+]_i$ [mM]")
ax13.set_ylabel("$T_{max}$ [kPa]")

sims_to_compare = ["baseline_pH",
				   "baseline_pH_H2",
				   "baseline_pH_H4",
				   "baseline_pH_H6",
				   "baseline_pH_H8",
				   "baseline_pH_H10"]
sizes = [20]*len(sims_to_compare)
sizes[0] = 60
extracted_data = metrics_data.loc[sims_to_compare]

ax20.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],color=color,zorder=1)
ax20.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_diast[uM]"],s=sizes,color=color,facecolor='white')
ax20.set_xlabel("$[Na^+]_i$ [mM]")
ax20.set_ylabel("$[Ca^{2+}]_{i,diast}$ [$\mu$M]")

ax21.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],color=color,zorder=1)
ax21.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_max[uM]"],s=sizes,color=color,facecolor='white')
ax21.set_xlabel("$[Na^+]_i$ [mM]")
ax21.set_ylabel("$[Ca^{2+}]_{i,max}$ [$\mu$M]")

ax22.plot(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],color=color,zorder=1)
ax22.scatter(extracted_data["Na_i[mM]"],extracted_data["Ca_i_ampl[uM]"],s=sizes,color=color,facecolor='white')
ax22.set_xlabel("$[Na^+]_i$ [mM]")
ax22.set_ylabel("$[Ca^{2+}]_{i,ampl}$ [$\mu$M]")

ax23.plot(extracted_data["Na_i[mM]"],extracted_data["T_max[kPa]"],color=color,zorder=1)
ax23.scatter(extracted_data["Na_i[mM]"],extracted_data["T_max[kPa]"],s=sizes,color=color,facecolor='white')
ax23.set_xlabel("$[Na^+]_i$ [mM]")
ax23.set_ylabel("$T_{max}$ [kPa]")

plt.tight_layout()
plt.savefig(os.path.join(fig_folder,"Figure4.png"),dpi=300)