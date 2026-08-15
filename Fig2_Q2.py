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

fig = plt.figure(constrained_layout=True, figsize=(12,6))
grid = fig.add_gridspec(4,3)
plt.rcParams['font.size'] = 9
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['text.usetex'] = True

ax00 = plt.subplot(grid[0, 0])
ax01 = plt.subplot(grid[0, 1])
ax02 = plt.subplot(grid[0, 2])
ax10 = plt.subplot(grid[1, 0])
ax11 = plt.subplot(grid[1, 1])
ax12 = plt.subplot(grid[1, 2])
ax20 = plt.subplot(grid[2, 0])
ax21 = plt.subplot(grid[2, 1])
ax22 = plt.subplot(grid[2, 2])
ax30 = plt.subplot(grid[3, 0])
ax31 = plt.subplot(grid[3, 1])
ax32 = plt.subplot(grid[3, 2])

colours = ["deepskyblue","deepskyblue","tab:red","tab:red"]
hatches = ['','///','','///']
line_styles = ['-','--','-','--']
dashes = [[],(5, 1),[],(5, 1)]

sims_to_compare = ["baseline_pH","baseline_pH_NHE_off",
				   "low_pH_bicarb_pH","low_pH_bicarb_pH_NHE_off"]
legend = ["baseline","NHE off","$pH_e$=7.2\nlow $[HCO_3^-]_e$","$pH_e$=7.2\nlow $[HCO_3^-]_e$\nNHE off"]

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

ax10.bar(x,extracted_data["Ca_i_max[uM]"],color=colours,hatch=hatches,edgecolor='white')
ax10.set_xticks(x)
ax10.set_xticklabels(legend)
ax10.set_ylabel("$[Ca^{2+}]_{i,max}$ [$\mu$M]")
ax10.spines[['right', 'top']].set_visible(False)

ax11.bar(x,extracted_data["Ca_i_ampl[uM]"],color=colours,hatch=hatches,edgecolor='white')
ax11.set_xticks(x)
ax11.set_xticklabels(legend)
ax11.set_ylabel("$[Ca^{2+}]_{i,ampl}$ [$\mu$M]")
ax11.spines[['right', 'top']].set_visible(False)

ax12.bar(x,extracted_data["T_max[kPa]"],color=colours,hatch=hatches,edgecolor='white')
ax12.set_xticks(x)
ax12.set_xticklabels(legend)
ax12.set_ylabel("$T_{max}$ [kPa]")
ax12.spines[['right', 'top']].set_visible(False)

sims_plot = [0,2]
for i in sims_plot:
	time = time_transients[i]
	ca_i = ca_transients[i]
	tension = t_transients[i]
	ax20.plot(time-time[0],ca_i,
			  color=colours[i],ls=line_styles[i],lw=1.5,dashes=dashes[i])
	ax20.set_xlabel('Time [ms]')
	ax20.set_ylabel('$[Ca^{2+}]_{i}$ [$\mu$M]')

	ax30.plot(time-time[0],tension,
			  color=colours[i],ls=line_styles[i],lw=1.5,dashes=dashes[i])
	ax30.set_xlabel('Time [ms]')
	ax30.set_ylabel('T [kPa]')

sims_plot = [0,1]
for i in sims_plot:
	time = time_transients[i]
	ca_i = ca_transients[i]
	tension = t_transients[i]
	ax21.plot(time-time[0],ca_i,
			  color=colours[i],ls=line_styles[i],lw=1.5,dashes=dashes[i])
	ax21.set_xlabel('Time [ms]')
	ax21.set_ylabel('$[Ca^{2+}]_{i}$ [$\mu$M]')

	ax31.plot(time-time[0],tension,
			  color=colours[i],ls=line_styles[i],lw=1.5,dashes=dashes[i])
	ax31.set_xlabel('Time [ms]')
	ax31.set_ylabel('T [kPa]')

sims_plot = [2,3]
for i in sims_plot:
	time = time_transients[i]
	ca_i = ca_transients[i]
	tension = t_transients[i]
	ax22.plot(time-time[0],ca_i,
			  color=colours[i],ls=line_styles[i],lw=1.5,dashes=dashes[i])
	ax22.set_xlabel('Time [ms]')
	ax22.set_ylabel('$[Ca^{2+}]_{i}$ [$\mu$M]')

	ax32.plot(time-time[0],tension,
			  color=colours[i],ls=line_styles[i],lw=1.5,dashes=dashes[i])
	ax32.set_xlabel('Time [ms]')
	ax32.set_ylabel('T [kPa]')

plt.tight_layout()
plt.savefig(os.path.join(fig_folder,"Figure2.png"),dpi=300)
