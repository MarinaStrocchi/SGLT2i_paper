#!/bin/bash

NBEATS=3000

# --------------
# CHE
SIMFOLDER="CHE_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--che_scale_factor 0.5
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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

SIMFOLDER="CHE_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--che_scale_factor 1.5
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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

# --------------
# AE
SIMFOLDER="AE_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--ae_scale_factor 0.5
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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

SIMFOLDER="AE_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--ae_scale_factor 1.5
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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

# --------------
# NCB
SIMFOLDER="NCB_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--ncb_scale_factor 0.5
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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

SIMFOLDER="NCB_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--ncb_scale_factor 1.5
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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

# --------------
# IH
SIMFOLDER="H_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--H_scale_factor 0.5
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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

SIMFOLDER="H_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--H_scale_factor 1.5
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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

# --------------
# NHE
SIMFOLDER="NHE_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 0.5 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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

SIMFOLDER="NHE_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.5 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
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