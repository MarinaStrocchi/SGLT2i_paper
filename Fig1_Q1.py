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

fig = plt.figure(constrained_layout=True, figsize=(12,4))
grid = fig.add_gridspec(2,6)
plt.rcParams['font.size'] = 9
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['text.usetex'] = True

ax00 = plt.subplot(grid[0, 0])
ax01 = plt.subplot(grid[0, 1])
ax02 = plt.subplot(grid[0, 2])
ax03 = plt.subplot(grid[0, 3])
ax04 = plt.subplot(grid[0, 4])
ax05 = plt.subplot(grid[0, 5])
ax10 = plt.subplot(grid[1, :3])
ax11 = plt.subplot(grid[1, 3:])

colours = ["deepskyblue","deepskyblue"]
hatches = ['','///']
line_styles = ['-','--']
dashes = [[],(5, 1)]

sims_to_compare = ["baseline_Tref_pH","baseline_Tref_pH_NHE_off"]
legend = ["baseline","NHE off"]

time_transients = []
ca_transients = []
t_transients = []
for s in sims_to_compare:

	sim_folder = os.path.join(source_folder,s)

	time = np.loadtxt(os.path.join(sim_folder,"time.dat"),dtype=float)
	ca_i = np.loadtxt(os.path.join(sim_folder,"ca_i.dat"),dtype=float)
	tension = np.loadtxt(os.path.join(sim_folder,"tension.dat"),dtype=float)

	time_transients.append(time)
	ca_transients.append(ca_i)
	t_transients.append(tension)

extracted_data = metrics_data.loc[sims_to_compare]
x = range(len(sims_to_compare))

ax00.bar(x,extracted_data["Na_i[mM]"],color=colours,hatch=hatches,edgecolor='white')
ax00.set_xticks(x)
ax00.set_xticklabels(legend)
ax00.set_ylabel("$[Na^+]_i$ [mM]")
ax00.spines[['right', 'top']].set_visible(False)

ax01.bar(x,extracted_data["NHE_flux[uM/ms]"],color=colours,hatch=hatches,edgecolor='white')
ax01.set_xticks(x)
ax01.set_xticklabels(legend)
ax01.set_ylabel("NHE flux [$\mu$M/ms]")
ax01.spines[['right', 'top']].set_visible(False)

ax02.bar(x,extracted_data["Ca_i_diast[uM]"],color=colours,hatch=hatches,edgecolor='white')
ax02.set_xticks(x)
ax02.set_xticklabels(legend)
ax02.set_ylabel("$[Ca^{2+}]_{i,diast}$ [$\mu$M]")
ax02.spines[['right', 'top']].set_visible(False)

ax03.bar(x,extracted_data["Ca_i_max[uM]"],color=colours,hatch=hatches,edgecolor='white')
ax03.set_xticks(x)
ax03.set_xticklabels(legend)
ax03.set_ylabel("$[Ca^{2+}]_{i,max}$ [$\mu$M]")
ax03.spines[['right', 'top']].set_visible(False)

ax04.bar(x,extracted_data["Ca_i_ampl[uM]"],color=colours,hatch=hatches,edgecolor='white')
ax04.set_xticks(x)
ax04.set_xticklabels(legend)
ax04.set_ylabel("$[Ca^{2+}]_{i,ampl}$ [$\mu$M]")
ax04.spines[['right', 'top']].set_visible(False)

ax05.bar(x,extracted_data["T_max[kPa]"],color=colours,hatch=hatches,edgecolor='white')
ax05.set_xticks(x)
ax05.set_xticklabels(legend)
ax05.set_ylabel("$T_{max}$ [kPa]")
ax05.spines[['right', 'top']].set_visible(False)

for i in range(len(sims_to_compare)):
	time = time_transients[i]
	ca_i = ca_transients[i]
	tension = t_transients[i]
	ax10.plot(time-time[0],ca_i,
			  color=colours[i],ls=line_styles[i],lw=1.5,dashes=dashes[i])
	ax10.set_xlabel('Time [ms]')
	ax10.set_ylabel('$[Ca^{2+}]_{i}$ [$\mu$M]')

	ax11.plot(time-time[0],tension,
			  color=colours[i],ls=line_styles[i],lw=1.5,dashes=dashes[i])
	ax11.set_xlabel('Time [ms]')
	ax11.set_ylabel('T [kPa]')

plt.tight_layout()
plt.savefig(os.path.join(fig_folder,"Figure1.png"),dpi=300)
