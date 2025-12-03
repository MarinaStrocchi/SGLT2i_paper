import os
import sys

import numpy as np

import argparse
import subprocess
import copy

def plot_model(voi, states, algebraic, figname):
    """Plot variables against variable of integration"""
    import matplotlib.pyplot as plt

    legend = []
    na_i = states[1,:]*1e03 # intracellular sodium

    ca_i = states[16,:]*1e03 # intracellular calcium

    tension = algebraic[135,:]

    nhe_flux = algebraic[51,:]*1e03

    fig,axs = plt.subplots(nrows=1, ncols=4, figsize=(9,3))
    axs[0].plot(voi,na_i,lw=1.0,color='black')
    axs[0].set_xlabel("time [ms]")
    axs[0].set_ylabel("Na_i [uM]")

    axs[1].plot(voi,ca_i,lw=1.0,color='black')
    axs[1].set_xlabel("time [ms]")
    axs[1].set_ylabel("Ca_i [uM]")

    axs[2].plot(voi,tension,lw=1.0,color='black')
    axs[2].set_xlabel("time [ms]")
    axs[2].set_ylabel("Tension [kPa]")

    axs[3].plot(voi,nhe_flux,lw=1.0,color='black')
    axs[3].set_xlabel("time [ms]")
    axs[3].set_ylabel("NHE flux [uM/ms]")

    plt.tight_layout()
    plt.savefig(figname,dpi=300)

def run_split_model(args):

	NBEATS_split = 100
	BCL = float(args.bcl)

	NBEATS = int(args.nbeats)
	if NBEATS%NBEATS_split!=0:
		raise Exception("Please select a number of beats that is a multiple of "+str(NBEATS_split)+" to split the simulation")

	Nsplits = int(NBEATS/NBEATS_split)
	run = True
	if not os.path.exists(args.simfolder):
		os.system("mkdir -p "+args.simfolder)
	else:
		choice = input("The output folder already exists. Do you want to overwrite? [y/n]\n")
		while choice not in ['y','n']: choice = input("Please choose y or n\n")
		if choice=='y':
			os.system("rm -r "+args.simfolder)
			os.system("mkdir -p "+args.simfolder)
		else:
			run = False

	all_ok = True

	store_actions = ['fast','visualise','compute_algebraic','coarse']
	original_args = copy.deepcopy(args)
	for i in range(Nsplits):
		process_cmd = ['python','niederer_smith_2007_pacing_study_Tref_pH_bicarb.py']

		simfolder_sub = os.path.join(original_args.simfolder,"split_"+str(i))
		args_dct = vars(args)

		args_dct["figname"] = os.path.join(simfolder_sub,"results.png")
		args_dct["simfolder"] = simfolder_sub
		args_dct["nbeats"] = str(NBEATS_split)
		if i > 0:
			args_dct['inittime'] = str(BCL*i*NBEATS_split)
			args_dct['initstate'] = os.path.join(original_args.simfolder,"split_"+str(i-1),"init_state.dat")
		for arg in args_dct:
			if (not arg in store_actions) and (args_dct[arg] is not None):
				process_cmd += ['--'+arg,args_dct[arg]]
			else:
				if args_dct[arg]:
					process_cmd += ['--'+arg]

		print(process_cmd)

		process = subprocess.run(process_cmd,capture_output=True)
		if process.returncode!=0:
			all_ok = False
			raise Exception("Simulation split_"+str(i)+" did not run successfully. Stopping")

	if all_ok:
		# Put all simulations together
		simfolder_sub = os.path.join(original_args.simfolder,"split_0")
		states        = np.loadtxt(os.path.join(simfolder_sub,"states.dat"),dtype=float)
		algebraic     = np.loadtxt(os.path.join(simfolder_sub,"algebraic.dat"),dtype=float)
		time          = list(np.loadtxt(os.path.join(simfolder_sub,"time.dat"),dtype=float))
		for i in range(Nsplits-1):
			simfolder_sub = os.path.join(original_args.simfolder,"split_"+str(i+1))

			states_tmp    = np.loadtxt(os.path.join(simfolder_sub,"states.dat"),dtype=float)
			algebraic_tmp = np.loadtxt(os.path.join(simfolder_sub,"algebraic.dat"),dtype=float)
			time_tmp      = np.loadtxt(os.path.join(simfolder_sub,"time.dat"),dtype=float)

			if i!=Nsplits-2:
				states = np.column_stack((states,states_tmp[:,:-1]))
				algebraic = np.column_stack((algebraic,algebraic_tmp[:,:-1]))
				time += list(time_tmp[:-1])	
			else:
				states = np.column_stack((states,states_tmp))
				algebraic = np.column_stack((algebraic,algebraic_tmp))
				time += list(time_tmp)	

		states = np.array(states)
		algebraic = np.array(algebraic)	

		plot_model(time, states, algebraic, os.path.join(original_args.simfolder,"results_SS.png"))

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.formatter_class = argparse.ArgumentDefaultsHelpFormatter

	parser.add_argument('--simfolder', type=str, default=None, required=True,
						help='Provide the folder where to save the results')

	parser.add_argument('--initstate', type=str, default=None, required=False,
						help='If provided, the simulation is initialised at this state')

	parser.add_argument('--inittime', type=str, default=None, required=False,
						help='If provided, the simulation is started at this time')

	parser.add_argument('--nhe_factor', type=str, default="1.0", required=False,
						help='Set to 0 to turn off NHE. It multipies kp1_nhe')

	parser.add_argument('--bicarb_factor', type=str, default="1.0", required=False,
						help='Scales constant 183 extracellular HCO3 concentration. Cannot set to 0 because it goes at the denominator of another constant')

	parser.add_argument('--Km_Na_factor', type=str, default="1.0", required=False,
						help='Scales constant 34 Km_Na for the Na-K pump')

	parser.add_argument('--iNa_b_scale_factor', type=str, default="1.0", required=False,
                        help='Scales algebraic 37 Na background current (simulating increased late Na current)')

	parser.add_argument('--iK_b_scale_factor', type=str, default="0.0", required=False,
                        help='Scales algebraic 38 K background current')

	parser.add_argument('--H_constant', type=str, default="0.0", required=False,
                        help='Introduce a constant current across the cell membrane')

	parser.add_argument('--pH_e', type=str, default="7.4", required=False,
						help='Extracellular pH')

	parser.add_argument('--figname', type=str, default=None, required=False,
						help='Provide the name of the figure if you want to save it ')

	parser.add_argument('--bcl', type=str, default="1000.0", required=False,
						help='BCL of the simulation in ms')

	parser.add_argument('--nbeats', type=str, default="100", required=False,
						help='Number of beats to simulate')

	parser.add_argument('--dtout', type=str, default="1.0", required=False,
						help='Output granularity')

	parser.add_argument("--fast", help="Run with a bigger dt for testing",
						action="store_true")

	parser.add_argument("--visualise", help="Plot outputs",
						action="store_true")

	parser.add_argument("--compute_algebraic", help="Use existing solution to only save algebraic",
						action="store_true")

	parser.add_argument("--coarse", help="Use coarse solution to compute algebraic",
						action="store_true")

	args = parser.parse_args()

	run_split_model(args)