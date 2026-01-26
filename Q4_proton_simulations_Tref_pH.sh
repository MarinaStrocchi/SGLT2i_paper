#!/bin/bash

NBEATS=3000

SIMFOLDER="baseline_pH_H2"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant -0.0002
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_H4"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant -0.0004
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_H6"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.0
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

SIMFOLDER="baseline_pH_H8"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant -0.0008
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_H10"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant -0.001
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd