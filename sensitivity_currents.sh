#!/bin/bash

NBEATS=3000

# --------------
# ICl
SIMFOLDER="Cl_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Cl_scale_factor 0.5
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

SIMFOLDER="Cl_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Cl_scale_factor 1.5
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
# IKss
SIMFOLDER="Kss_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Kss_scale_factor 0.5
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

SIMFOLDER="Kss_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Kss_scale_factor 1.5
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
# IK1
SIMFOLDER="K1_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--K1_scale_factor 0.5
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

SIMFOLDER="K1_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--K1_scale_factor 1.5
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
# IKt
SIMFOLDER="Kt_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Kt_scale_factor 0.5
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

SIMFOLDER="Kt_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Kt_scale_factor 1.5
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
# IKf
SIMFOLDER="Kf_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Kf_scale_factor 0.5
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

SIMFOLDER="Kf_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Kf_scale_factor 1.5
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
# IKo
SIMFOLDER="Ko_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Ko_scale_factor 0.5
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

SIMFOLDER="Ko_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Ko_scale_factor 1.5
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
# NaK
SIMFOLDER="NaK_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--NaK_scale_factor 0.5
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

SIMFOLDER="NaK_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--NaK_scale_factor 1.5
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
# Na
SIMFOLDER="Na_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Na_scale_factor 0.5
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

SIMFOLDER="Na_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Na_scale_factor 1.5
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
# Nab
SIMFOLDER="Nab_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 0.5
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

SIMFOLDER="Nab_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.5
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
# Kb
SIMFOLDER="Kb_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 0.5
		--H_constant 0.0
		--pH_e 7.4 
		--figname ${SIMFOLDER}/results.png 
		--bcl 1000
		--nbeats ${NBEATS} 
		--dtout 1.0 
		--visualise 
		>/dev/null 2>&1 &"
eval $cmd

SIMFOLDER="Kb_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--nhe_factor 1.0 
		--bicarb_factor 1.0 
		--Km_Na_factor 1.0
		--iNa_b_scale_factor 1.0
		--iK_b_scale_factor 0.5
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
# Naf
SIMFOLDER="Naf_50"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Naf_scale_factor 0.5
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

SIMFOLDER="Naf_150"
cmd="python run_SS_simulation_Tref_pH_R2.py 
		--simfolder ${SIMFOLDER} 
		--Naf_scale_factor 1.5
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