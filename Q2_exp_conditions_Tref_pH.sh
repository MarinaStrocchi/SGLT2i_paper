#!/bin/bash

NBEATS=3000

SIMFOLDER="low_pH_bicarb_Tref_pH"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 0.172 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.2 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="low_pH_bicarb_Tref_pH_NHE_off"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 0.0 
		--bicarb_factor 0.172  
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.2 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd