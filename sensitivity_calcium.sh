#!/bin/bash

NBEATS=3000

# --------------
# pCa 
SIMFOLDER="pCa_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--pCa_scale_factor 0.5
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

SIMFOLDER="pCa_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--pCa_scale_factor 1.5
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
# background calcium 
SIMFOLDER="Cab_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Cab_scale_factor 0.5
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

SIMFOLDER="Cab_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Cab_scale_factor 1.5
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
# J release (ryr) 
SIMFOLDER="Jrel_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--jRel_scale_factor 0.5
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

SIMFOLDER="Jrel_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--jRel_scale_factor 1.5
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
# NCX
SIMFOLDER="NCX_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--ncx_scale_factor 0.5
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

SIMFOLDER="NCX_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--ncx_scale_factor 1.5
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
# SR uptake
SIMFOLDER="Juptake_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--serca_scale_factor 0.5
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

SIMFOLDER="Juptake_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--serca_scale_factor 1.5
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
# L-type calcium
SIMFOLDER="CaL_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--CaL_scale_factor 0.5
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

SIMFOLDER="CaL_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--CaL_scale_factor 1.5
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
# Jleak
SIMFOLDER="Jleak_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--leak_scale_factor 0.5
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

SIMFOLDER="Jleak_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--leak_scale_factor 1.5
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
