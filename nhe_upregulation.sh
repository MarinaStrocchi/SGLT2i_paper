#!/bin/bash

NBEATS=3000

SIMFOLDER="HF_pH_NHE2"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 2.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.3
		--iNa_b_scale_factor 3.0
		--iK_b_scale_factor 1.0
		--H_constant -0.0006
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="HF_pH_NHE3"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 3.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.3
		--iNa_b_scale_factor 3.0
		--iK_b_scale_factor 1.0
		--H_constant -0.0006
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd