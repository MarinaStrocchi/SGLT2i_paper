#!/bin/bash

NBEATS=3000

SIMFOLDER="baseline_pH_Km50"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 0.5
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_Km60"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 0.6
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_Km70"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 0.7
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_Km80"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 0.8
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_Km90"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 0.9
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_Km110"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.1
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_Km120"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.2
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_Km130"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.3
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_Km140"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.4
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="baseline_pH_Km150"
cmd="python run_SS_simulation_Tref_pH_R1.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.5
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 1.0
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd
