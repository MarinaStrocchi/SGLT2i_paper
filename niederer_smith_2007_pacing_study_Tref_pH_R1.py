# Size of variable arrays:
sizeAlgebraic = 140
sizeStates = 26
sizeConstants = 196

import os

import math
import numpy
import json

import argparse

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_constants[0] = "NO_on in component strain_control (dimensionless)"
    legend_constants[1] = "pH_on in component strain_control (dimensionless)"
    legend_constants[2] = "SAC_on in component strain_control (dimensionless)"
    legend_voi = "time in component environment (ms)"
    legend_constants[3] = "V_myo in component cell_geom (mm3)"
    legend_constants[4] = "V_SR in component cell_geom (mm3)"
    legend_constants[5] = "N in component cell_geom (dimensionless)"
    legend_constants[6] = "A_cap in component cell_geom (mm2)"
    legend_constants[140] = "rho in component cell_geom (per_mm)"
    legend_states[0] = "V in component membrane (mV)"
    legend_constants[7] = "R in component membrane (millijoule_per_mole_kelvin)"
    legend_constants[8] = "T in component membrane (kelvin)"
    legend_constants[9] = "F in component membrane (coulomb_per_mole)"
    legend_constants[10] = "CmF in component membrane (uF)"
    legend_constants[149] = "Cm in component membrane (uF_per_mm2)"
    legend_algebraic[24] = "i_Na in component sodium_current (uA_per_mm2)"
    legend_algebraic[30] = "i_t in component Ca_independent_transient_outward_K_current (uA_per_mm2)"
    legend_algebraic[31] = "i_ss in component steady_state_outward_K_current (uA_per_mm2)"
    legend_algebraic[36] = "i_f in component hyperpolarisation_activated_current (uA_per_mm2)"
    legend_algebraic[32] = "i_K1 in component inward_rectifier (uA_per_mm2)"
    legend_algebraic[41] = "i_NaK in component sodium_potassium_pump (uA_per_mm2)"
    legend_algebraic[9] = "i_Stim in component I_stimulus (uA_per_mm2)"
    legend_algebraic[127] = "I_CaL in component I_Ca_L (uA_per_mm2)"
    legend_algebraic[87] = "I_NaCa in component NCX (uA_per_mm2)"
    legend_algebraic[83] = "I_Cab in component Cab (uA_per_mm2)"
    legend_algebraic[81] = "I_pCa in component SL_pump (uA_per_mm2)"
    legend_algebraic[37] = "i_B_Na in component background_currents (uA_per_mm2)"
    legend_algebraic[38] = "i_B_K in component background_currents (uA_per_mm2)"
    legend_algebraic[22] = "I_SAC_Na in component SAC_current (uA_per_mm2)"
    legend_algebraic[27] = "I_SAC_K in component SAC_current (uA_per_mm2)"
    legend_algebraic[29] = "I_Ko in component KSA_current (uA_per_mm2)"
    legend_algebraic[73] = "I_Cl in component intracellular_ion_concentrations (uA_per_mm2)"
    legend_algebraic[76] = "I_H in component intracellular_ion_concentrations (uA_per_mm2)"
    legend_constants[11] = "stim_period in component I_stimulus (ms)"
    legend_constants[12] = "stim_duration in component I_stimulus (ms)"
    legend_constants[13] = "stim_amplitude in component I_stimulus (uA)"
    legend_algebraic[20] = "E_Na in component sodium_current (mV)"
    legend_algebraic[25] = "E_K in component Ca_independent_transient_outward_K_current (mV)"
    legend_constants[14] = "ExtensionRatio in component Myofilaments (dimensionless)"
    legend_constants[15] = "g_SAC in component SAC_current (mS)"
    legend_algebraic[28] = "I_SAC in component SAC_current (uA_per_mm2)"
    legend_constants[141] = "gamma_SLSAC in component SAC_current (dimensionless)"
    legend_constants[16] = "E_R in component SAC_current (mV)"
    legend_constants[142] = "r in component SAC_current (dimensionless)"
    legend_constants[17] = "g_Ko in component KSA_current (mS)"
    legend_constants[143] = "gamma_SLKO in component KSA_current (dimensionless)"
    legend_constants[18] = "g_Na in component sodium_current (mS)"
    legend_constants[144] = "g_Na_endo in component sodium_current (mS)"
    legend_states[1] = "Na_i in component intracellular_ion_concentrations (mM)"
    legend_constants[19] = "Na_o in component standard_ionic_concentrations (mM)"
    legend_states[2] = "m in component sodium_current_m_gate (dimensionless)"
    legend_states[3] = "h in component sodium_current_h_gate (dimensionless)"
    legend_states[4] = "j in component sodium_current_j_gate (dimensionless)"
    legend_algebraic[0] = "m_infinity in component sodium_current_m_gate (dimensionless)"
    legend_algebraic[12] = "tau_m in component sodium_current_m_gate (ms)"
    legend_algebraic[1] = "h_infinity in component sodium_current_h_gate (dimensionless)"
    legend_algebraic[13] = "tau_h in component sodium_current_h_gate (ms)"
    legend_algebraic[2] = "j_infinity in component sodium_current_j_gate (dimensionless)"
    legend_algebraic[14] = "tau_j in component sodium_current_j_gate (ms)"
    legend_constants[20] = "g_t in component Ca_independent_transient_outward_K_current (mS)"
    legend_constants[145] = "g_t_endo in component Ca_independent_transient_outward_K_current (mS)"
    legend_constants[21] = "a_endo in component Ca_independent_transient_outward_K_current (dimensionless)"
    legend_constants[22] = "b_endo in component Ca_independent_transient_outward_K_current (dimensionless)"
    legend_constants[23] = "K_o in component standard_ionic_concentrations (mM)"
    legend_states[5] = "K_i in component intracellular_ion_concentrations (mM)"
    legend_states[6] = "r in component Ca_independent_transient_outward_K_current_r_gate (dimensionless)"
    legend_states[7] = "s in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_states[8] = "s_slow in component Ca_independent_transient_outward_K_current_s_slow_gate (dimensionless)"
    legend_algebraic[15] = "tau_r in component Ca_independent_transient_outward_K_current_r_gate (ms)"
    legend_algebraic[3] = "r_infinity in component Ca_independent_transient_outward_K_current_r_gate (dimensionless)"
    legend_algebraic[16] = "tau_s_endo in component Ca_independent_transient_outward_K_current_s_gate (ms)"
    legend_algebraic[4] = "s_infinity in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_algebraic[17] = "tau_s_slow_endo in component Ca_independent_transient_outward_K_current_s_slow_gate (ms)"
    legend_algebraic[5] = "s_slow_infinity in component Ca_independent_transient_outward_K_current_s_slow_gate (dimensionless)"
    legend_constants[24] = "g_ss in component steady_state_outward_K_current (mS)"
    legend_states[9] = "r_ss in component steady_state_outward_K_current_r_ss_gate (dimensionless)"
    legend_states[10] = "s_ss in component steady_state_outward_K_current_s_ss_gate (dimensionless)"
    legend_algebraic[18] = "tau_r_ss in component steady_state_outward_K_current_r_ss_gate (ms)"
    legend_algebraic[6] = "r_ss_infinity in component steady_state_outward_K_current_r_ss_gate (dimensionless)"
    legend_constants[146] = "tau_s_ss in component steady_state_outward_K_current_s_ss_gate (ms)"
    legend_algebraic[7] = "s_ss_infinity in component steady_state_outward_K_current_s_ss_gate (dimensionless)"
    legend_constants[25] = "g_K1 in component inward_rectifier (mS)"
    legend_algebraic[33] = "i_f_Na in component hyperpolarisation_activated_current (uA_per_mm2)"
    legend_algebraic[34] = "i_f_K in component hyperpolarisation_activated_current (uA_per_mm2)"
    legend_constants[26] = "g_f in component hyperpolarisation_activated_current (mS)"
    legend_constants[27] = "f_Na in component hyperpolarisation_activated_current (dimensionless)"
    legend_constants[147] = "f_K in component hyperpolarisation_activated_current (dimensionless)"
    legend_states[11] = "y in component hyperpolarisation_activated_current_y_gate (dimensionless)"
    legend_algebraic[19] = "tau_y in component hyperpolarisation_activated_current_y_gate (ms)"
    legend_algebraic[8] = "y_infinity in component hyperpolarisation_activated_current_y_gate (dimensionless)"
    legend_constants[28] = "g_B_Na in component background_currents (mS)"
    legend_constants[29] = "g_B_K in component background_currents (mS)"
    legend_constants[30] = "scale_Na in component background_currents (dimensionless)"
    legend_constants[31] = "scale_K in component background_currents (dimensionless)"
    legend_constants[32] = "i_NaK_max in component sodium_potassium_pump (uA)"
    legend_constants[33] = "K_m_K in component sodium_potassium_pump (mM)"
    legend_constants[34] = "K_m_Na in component sodium_potassium_pump (mM)"
    legend_constants[148] = "sigma in component sodium_potassium_pump (dimensionless)"
    legend_algebraic[39] = "p_nai in component sodium_potassium_pump (dimensionless)"
    legend_algebraic[40] = "p_v in component sodium_potassium_pump (dimensionless)"
    legend_algebraic[42] = "jco2 in component J_CO2 (mM_per_ms)"
    legend_constants[35] = "Pco2 in component J_CO2 (mm_per_ms)"
    legend_states[12] = "CO2i in component intracellular_ion_concentrations (mM)"
    legend_constants[182] = "CO2e in component intracellular_ion_concentrations (mM)"
    legend_states[13] = "pH_i in component intracellular_ion_concentrations (dimensionless)"
    legend_constants[36] = "pH_e in component intracellular_ion_concentrations (dimensionless)"
    legend_algebraic[51] = "v_nhe in component comp_v_nhe_exchanger (mM_per_ms)"
    legend_constants[37] = "KA in component comp_v_nhe_exchanger (mM)"
    legend_constants[38] = "KB in component comp_v_nhe_exchanger (mM)"
    legend_constants[39] = "kp1 in component comp_v_nhe_exchanger (per_ms)"
    legend_constants[40] = "km1 in component comp_v_nhe_exchanger (per_ms)"
    legend_constants[41] = "kp2 in component comp_v_nhe_exchanger (per_ms)"
    legend_constants[163] = "km2 in component comp_v_nhe_exchanger (dimensionless)"
    legend_constants[42] = "K_Hi in component comp_v_nhe_exchanger (mM)"
    legend_constants[43] = "n_Hi in component comp_v_nhe_exchanger (dimensionless)"
    legend_constants[166] = "Be in component comp_v_nhe_exchanger (mM)"
    legend_algebraic[46] = "Bi in component comp_v_nhe_exchanger (mM)"
    legend_algebraic[47] = "am1 in component comp_v_nhe_exchanger (per_ms)"
    legend_constants[169] = "ap1 in component comp_v_nhe_exchanger (per_ms)"
    legend_constants[171] = "am2 in component comp_v_nhe_exchanger (per_ms)"
    legend_algebraic[48] = "ap2 in component comp_v_nhe_exchanger (per_ms)"
    legend_algebraic[49] = "reg in component comp_v_nhe_exchanger (dimensionless)"
    legend_algebraic[50] = "flux_nhe in component comp_v_nhe_exchanger (dimensionless)"
    legend_constants[44] = "Q_10Scaler in component comp_v_nhe_exchanger (dimensionless)"
    legend_constants[156] = "gamma_NHE in component comp_v_nhe_exchanger (dimensionless)"
    legend_constants[160] = "K_Hs in component comp_v_nhe_exchanger (mM)"
    legend_constants[45] = "Cle in component intracellular_ion_concentrations (mM)"
    legend_states[14] = "Cli in component intracellular_ion_concentrations (mM)"
    legend_algebraic[57] = "v_che in component comp_v_che_exchanger (mM_per_ms)"
    legend_constants[46] = "K_Cl in component comp_v_che_exchanger (mM)"
    legend_constants[47] = "K_OH in component comp_v_che_exchanger (mM)"
    legend_constants[48] = "kp1 in component comp_v_che_exchanger (per_min)"
    legend_constants[49] = "km1 in component comp_v_che_exchanger (per_min)"
    legend_constants[50] = "kp2 in component comp_v_che_exchanger (per_min)"
    legend_constants[172] = "km2 in component comp_v_che_exchanger (per_min)"
    legend_constants[173] = "OHe in component comp_v_che_exchanger (mM)"
    legend_algebraic[52] = "OHi in component comp_v_che_exchanger (mM)"
    legend_constants[174] = "a in component comp_v_che_exchanger (dimensionless)"
    legend_constants[175] = "b in component comp_v_che_exchanger (dimensionless)"
    legend_algebraic[53] = "c in component comp_v_che_exchanger (dimensionless)"
    legend_algebraic[54] = "d in component comp_v_che_exchanger (dimensionless)"
    legend_algebraic[55] = "s1 in component comp_v_che_exchanger (dimensionless)"
    legend_algebraic[56] = "s6 in component comp_v_che_exchanger (dimensionless)"
    legend_constants[51] = "Q_10Scaler in component comp_v_che_exchanger (dimensionless)"
    legend_constants[183] = "HCO3e in component intracellular_ion_concentrations (mM)"
    legend_states[15] = "HCO3i in component intracellular_ion_concentrations (mM)"
    legend_algebraic[64] = "v_nbc in component comp_v_nbc (mM_per_ms)"
    legend_constants[52] = "K_Na in component comp_v_nbc (mM)"
    legend_constants[53] = "K_HCO3 in component comp_v_nbc (mM)"
    legend_constants[54] = "kp1 in component comp_v_nbc (per_min)"
    legend_constants[55] = "km1 in component comp_v_nbc (per_min)"
    legend_constants[56] = "kp2 in component comp_v_nbc (per_min)"
    legend_constants[176] = "km2 in component comp_v_nbc (per_min)"
    legend_constants[57] = "K_Hi in component comp_v_nbc (mM)"
    legend_constants[58] = "n_Hi in component comp_v_nbc (dimensionless)"
    legend_constants[59] = "K_He in component comp_v_nbc (mM)"
    legend_constants[60] = "n_He in component comp_v_nbc (dimensionless)"
    legend_constants[177] = "He in component comp_v_nbc (mM)"
    legend_algebraic[60] = "Hi in component comp_v_nbc (mM)"
    legend_constants[184] = "a in component comp_v_nbc (dimensionless)"
    legend_constants[185] = "b in component comp_v_nbc (dimensionless)"
    legend_algebraic[58] = "c in component comp_v_nbc (dimensionless)"
    legend_algebraic[59] = "d in component comp_v_nbc (dimensionless)"
    legend_algebraic[61] = "s1 in component comp_v_nbc (dimensionless)"
    legend_algebraic[62] = "s6 in component comp_v_nbc (dimensionless)"
    legend_algebraic[63] = "reg in component comp_v_nbc (dimensionless)"
    legend_constants[61] = "Q_10Scaler in component comp_v_nbc (dimensionless)"
    legend_algebraic[71] = "v_ae in component comp_v_ae (mM_per_ms)"
    legend_constants[62] = "K_Cl in component comp_v_ae (mM)"
    legend_constants[63] = "K_HCO3 in component comp_v_ae (mM)"
    legend_constants[64] = "kp1 in component comp_v_ae (per_min)"
    legend_constants[65] = "km1 in component comp_v_ae (per_min)"
    legend_constants[66] = "kp2 in component comp_v_ae (per_min)"
    legend_constants[180] = "km2 in component comp_v_ae (per_min)"
    legend_constants[67] = "K_Hi in component comp_v_ae (mM)"
    legend_constants[68] = "n_Hi in component comp_v_ae (dimensionless)"
    legend_constants[69] = "K_He in component comp_v_ae (mM)"
    legend_constants[70] = "n_He in component comp_v_ae (dimensionless)"
    legend_constants[181] = "He in component comp_v_ae (mM)"
    legend_algebraic[65] = "Hi in component comp_v_ae (mM)"
    legend_constants[186] = "a in component comp_v_ae (dimensionless)"
    legend_constants[187] = "b in component comp_v_ae (dimensionless)"
    legend_algebraic[66] = "c in component comp_v_ae (dimensionless)"
    legend_algebraic[67] = "d in component comp_v_ae (dimensionless)"
    legend_algebraic[68] = "s1 in component comp_v_ae (dimensionless)"
    legend_algebraic[69] = "s6 in component comp_v_ae (dimensionless)"
    legend_algebraic[70] = "reg in component comp_v_ae (dimensionless)"
    legend_constants[71] = "Q_10Scaler in component comp_v_ae (dimensionless)"
    legend_constants[178] = "gamma_AE in component comp_v_ae (dimensionless)"
    legend_constants[179] = "K_Hs in component comp_v_ae (mM)"
    legend_constants[72] = "PP_co2e in component intracellular_ion_concentrations (dimensionless)"
    legend_constants[73] = "CO_2sol in component intracellular_ion_concentrations (dimensionless)"
    legend_constants[74] = "P_atm in component intracellular_ion_concentrations (dimensionless)"
    legend_constants[75] = "kf_co2hyd in component intracellular_ion_concentrations (per_ms)"
    legend_constants[76] = "kr_co2hyd in component intracellular_ion_concentrations (per_mM_per_ms)"
    legend_algebraic[79] = "v_co2hyd in component intracellular_ion_concentrations (mM_per_ms)"
    legend_constants[77] = "pKa_ib1 in component intracellular_ion_concentrations (dimensionless)"
    legend_constants[78] = "ib1 in component intracellular_ion_concentrations (mM)"
    legend_constants[79] = "pKa_ib2 in component intracellular_ion_concentrations (dimensionless)"
    legend_constants[80] = "ib2 in component intracellular_ion_concentrations (mM)"
    legend_algebraic[77] = "beta_intr in component intracellular_ion_concentrations (dimensionless)"
    legend_constants[81] = "pH_scale in component intracellular_ion_concentrations (dimensionless)"
    legend_algebraic[43] = "nai_Nak in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[78] = "nai_NHE in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[80] = "nai_NBC in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[88] = "nai_flux in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[35] = "nai_bg in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[44] = "K_Nak in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[45] = "K_flux in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[72] = "E_Cl in component intracellular_ion_concentrations (mV)"
    legend_constants[82] = "g_Cl in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[75] = "E_H in component intracellular_ion_concentrations (mV)"
    legend_constants[83] = "g_H in component intracellular_ion_concentrations (mM_per_ms)"
    legend_constants[150] = "H_o in component intracellular_ion_concentrations (mM)"
    legend_algebraic[74] = "H_i in component intracellular_ion_concentrations (mM)"
    legend_constants[84] = "J_CO2 in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[89] = "nai_NaCa in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[26] = "nai_na in component intracellular_ion_concentrations (mM_per_ms)"
    legend_algebraic[91] = "nai_total in component intracellular_ion_concentrations (mM_per_ms)"
    legend_constants[85] = "Ca_o in component standard_ionic_concentrations (mM)"
    legend_constants[86] = "g_pCa in component SL_pump (mM_per_ms)"
    legend_constants[87] = "K_mpCa in component SL_pump (mM)"
    legend_states[16] = "Ca_i in component ionic_concentrations (mM)"
    legend_constants[88] = "delta in component Ca_voltage (per_mV)"
    legend_algebraic[82] = "E_Ca in component Cab (mV)"
    legend_constants[89] = "g_Cab in component Cab (mM_per_ms)"
    legend_algebraic[125] = "J_LC in component L_flux (mM_per_ms_per_mm3)"
    legend_constants[90] = "K_mNa in component NCX (mM)"
    legend_constants[91] = "K_mCa in component NCX (mM)"
    legend_constants[92] = "eta in component NCX (dimensionless)"
    legend_constants[93] = "k_sat in component NCX (dimensionless)"
    legend_constants[94] = "g_NCX in component NCX (mM_per_ms)"
    legend_algebraic[84] = "edv in component NCX (dimensionless)"
    legend_algebraic[85] = "edv2 in component NCX (dimensionless)"
    legend_algebraic[86] = "Nai3 in component NCX (mM3)"
    legend_constants[151] = "Nae3 in component NCX (mM3)"
    legend_constants[95] = "g_SERCA in component SERCA (mM_per_ms)"
    legend_constants[96] = "K_SERCA in component SERCA (mM)"
    legend_algebraic[90] = "I_SERCA in component SERCA (mM_per_ms)"
    legend_states[17] = "Ca_SR in component ionic_concentrations (mM)"
    legend_states[18] = "TRPN in component ionic_concentrations (mM)"
    legend_constants[97] = "B_CMDN in component ionic_concentrations (mM)"
    legend_constants[98] = "K_CMDN in component ionic_concentrations (mM)"
    legend_constants[99] = "g_SRl in component ionic_concentrations (per_ms)"
    legend_algebraic[139] = "J_TPRN in component troponin (dimensionless)"
    legend_algebraic[129] = "J_RY in component R_flux (mM_per_ms_per_mm3)"
    legend_algebraic[131] = "J_SR in component ionic_concentrations (mM_per_ms)"
    legend_algebraic[10] = "Ca_b in component ionic_concentrations (mM)"
    legend_constants[100] = "B_TRPN in component troponin (mM)"
    legend_constants[101] = "g_D in component Ca_conductances (mm3_per_ms)"
    legend_constants[102] = "J_R in component Ca_conductances (mm3_per_ms)"
    legend_constants[103] = "J_L in component Ca_conductances (mm3_per_ms)"
    legend_algebraic[93] = "expmdV in component Ca_voltage (dimensionless)"
    legend_algebraic[94] = "expVL in component Ca_voltage (dimensionless)"
    legend_algebraic[92] = "dV in component Ca_voltage (mV)"
    legend_constants[104] = "V_L0 in component Ca_voltage (mV)"
    legend_constants[105] = "delta_VL in component Ca_voltage (mV)"
    legend_algebraic[11] = "C_cc in component C_ij (mM)"
    legend_algebraic[97] = "C_oc in component C_ij (mM)"
    legend_algebraic[96] = "C_co in component C_ij (mM)"
    legend_algebraic[95] = "C_oo in component C_ij (mM)"
    legend_algebraic[101] = "J_Loo in component J_ij (mM_per_ms)"
    legend_algebraic[100] = "J_Loc in component J_ij (mM_per_ms)"
    legend_algebraic[98] = "J_Rco in component J_ij (mM_per_ms)"
    legend_algebraic[99] = "J_Roo in component J_ij (mM_per_ms)"
    legend_constants[152] = "t_R in component Ca_tau (ms)"
    legend_constants[106] = "t_L in component Ca_tau (ms)"
    legend_algebraic[104] = "epsilon_m in component epsilon (per_ms)"
    legend_algebraic[102] = "epsilon_pco in component epsilon (per_ms)"
    legend_algebraic[103] = "epsilon_pcc in component epsilon (per_ms)"
    legend_constants[107] = "a in component epsilon (dimensionless)"
    legend_constants[108] = "b in component epsilon (dimensionless)"
    legend_constants[109] = "tau_L in component epsilon (ms)"
    legend_constants[110] = "K_L in component epsilon (mM)"
    legend_algebraic[105] = "alpha_p in component alpha (per_ms)"
    legend_constants[157] = "alpha_m in component alpha (per_ms)"
    legend_constants[111] = "phi_L in component alpha (dimensionless)"
    legend_constants[164] = "phi_R in component RyR_param (dimensionless)"
    legend_constants[112] = "phi_R_base in component RyR_param (dimensionless)"
    legend_constants[113] = "tau_R in component RyR_param (ms)"
    legend_constants[114] = "theta_R in component RyR_param (dimensionless)"
    legend_constants[115] = "K_RyR in component RyR_param (mM)"
    legend_constants[161] = "gamma_NO in component RyR_param (dimensionless)"
    legend_algebraic[106] = "beta_poc in component beta (per_ms)"
    legend_algebraic[107] = "beta_pcc in component beta (per_ms)"
    legend_constants[167] = "beta_m in component beta (per_ms)"
    legend_algebraic[108] = "mu_poc in component mu_ij (per_ms)"
    legend_algebraic[109] = "mu_pcc in component mu_ij (per_ms)"
    legend_algebraic[110] = "mu_moc in component mu_ij (per_ms)"
    legend_algebraic[111] = "mu_mcc in component mu_ij (per_ms)"
    legend_constants[116] = "c in component mu_ij (dimensionless)"
    legend_constants[117] = "d in component mu_ij (dimensionless)"
    legend_algebraic[113] = "y_oc in component y_ij (dimensionless)"
    legend_algebraic[114] = "y_co in component y_ij (dimensionless)"
    legend_algebraic[115] = "y_oo in component y_ij (dimensionless)"
    legend_algebraic[116] = "y_cc in component y_ij (dimensionless)"
    legend_algebraic[112] = "denom in component y_ij (per_ms3)"
    legend_algebraic[118] = "r_1 in component r_i (per_ms)"
    legend_algebraic[120] = "r_2 in component r_i (per_ms)"
    legend_algebraic[122] = "r_3 in component r_i (per_ms)"
    legend_algebraic[124] = "r_4 in component r_i (per_ms)"
    legend_algebraic[126] = "r_5 in component r_i (per_ms)"
    legend_algebraic[128] = "r_6 in component r_i (per_ms)"
    legend_algebraic[130] = "r_7 in component r_i (per_ms)"
    legend_algebraic[132] = "r_8 in component r_i (per_ms)"
    legend_states[19] = "z_1 in component z_i (dimensionless)"
    legend_states[20] = "z_2 in component z_i (dimensionless)"
    legend_states[21] = "z_3 in component z_i (dimensionless)"
    legend_algebraic[133] = "z_4 in component z_i (dimensionless)"
    legend_algebraic[117] = "J_R1 in component J_values (mM_per_ms)"
    legend_algebraic[119] = "J_R3 in component J_values (mM_per_ms)"
    legend_algebraic[121] = "J_L1 in component J_values (mM_per_ms)"
    legend_algebraic[123] = "J_L2 in component J_values (mM_per_ms)"
    legend_algebraic[138] = "betaCab in component troponin (per_ms)"
    legend_constants[118] = "k_on in component troponin (per_mM_per_ms)"
    legend_constants[119] = "k_off in component troponin (per_ms)"
    legend_constants[120] = "gamma_trpn in component troponin (dimensionless)"
    legend_constants[121] = "TRPN_tot in component troponin (mM)"
    legend_algebraic[137] = "Tension in component Cross_Bridges (N_per_mm2)"
    legend_constants[122] = "T_ref in component length_independent_tension (N_per_mm2)"
    legend_constants[153] = "lamda in component Myofilaments (dimensionless)"
    legend_constants[154] = "dExtensionRatiodt in component Myofilaments (per_ms)"
    legend_constants[155] = "lambda_prev in component Myofilaments (dimensionless)"
    legend_states[22] = "z in component tropomyosin (dimensionless)"
    legend_constants[170] = "z_max in component tropomyosin (dimensionless)"
    legend_constants[123] = "alpha_0 in component tropomyosin (per_ms)"
    legend_constants[124] = "alpha_r1 in component tropomyosin (per_ms)"
    legend_constants[125] = "alpha_r2 in component tropomyosin (per_ms)"
    legend_constants[126] = "n_Rel in component tropomyosin (dimensionless)"
    legend_constants[127] = "K_z in component tropomyosin (dimensionless)"
    legend_constants[128] = "n_Hill in component tropomyosin (dimensionless)"
    legend_constants[129] = "Ca_50ref in component tropomyosin (mM)"
    legend_constants[130] = "z_p in component tropomyosin (dimensionless)"
    legend_constants[131] = "beta_1 in component tropomyosin (dimensionless)"
    legend_constants[165] = "Ca_50 in component tropomyosin (mM)"
    legend_constants[168] = "Ca_TRPN_50 in component tropomyosin (mM)"
    legend_constants[158] = "K_2 in component tropomyosin (dimensionless)"
    legend_constants[162] = "K_1 in component tropomyosin (dimensionless)"
    legend_algebraic[21] = "alpha_Tm in component tropomyosin (per_ms)"
    legend_algebraic[23] = "beta_Tm in component tropomyosin (per_ms)"
    legend_constants[132] = "beta_0 in component filament_overlap (dimensionless)"
    legend_constants[159] = "overlap in component filament_overlap (dimensionless)"
    legend_algebraic[134] = "T_Base in component length_independent_tension (N_per_mm2)"
    legend_algebraic[135] = "T_0 in component isometric_tension (N_per_mm2)"
    legend_algebraic[136] = "Q in component Cross_Bridges (dimensionless)"
    legend_constants[133] = "a in component Cross_Bridges (dimensionless)"
    legend_states[23] = "Q_1 in component Cross_Bridges (dimensionless)"
    legend_states[24] = "Q_2 in component Cross_Bridges (dimensionless)"
    legend_states[25] = "Q_3 in component Cross_Bridges (dimensionless)"
    legend_constants[134] = "A_1 in component Cross_Bridges (dimensionless)"
    legend_constants[135] = "A_2 in component Cross_Bridges (dimensionless)"
    legend_constants[136] = "A_3 in component Cross_Bridges (dimensionless)"
    legend_constants[137] = "alpha_1 in component Cross_Bridges (dimensionless)"
    legend_constants[138] = "alpha_2 in component Cross_Bridges (dimensionless)"
    legend_constants[139] = "alpha_3 in component Cross_Bridges (dimensionless)"
    legend_constants[188] = "bt maximum tension-pH dependence (dimensionless)"
    legend_constants[189] = "pHref reference pH for tension-pH dependence (dimensionless)"
    legend_constants[190] = "n_up for pH-dendence in SERCA uptake (dimensionless)"
    legend_constants[191] = "pKup for pH-dendence in SERCA uptake (dimensionless)"
    legend_constants[192] = "nNaCa for pH-dendence in NCX (dimensionless)"
    legend_constants[193] = "pKNaCa for pH-dendence in NCX (dimensionless)"
    legend_constants[194] = "nrel for pH-dendence in RyR (dimensionless)"
    legend_constants[195] = "pKrel for pH-dendence in RyR (dimensionless)"
    legend_rates[0] = "d/dt V in component membrane (mV)"
    legend_rates[2] = "d/dt m in component sodium_current_m_gate (dimensionless)"
    legend_rates[3] = "d/dt h in component sodium_current_h_gate (dimensionless)"
    legend_rates[4] = "d/dt j in component sodium_current_j_gate (dimensionless)"
    legend_rates[6] = "d/dt r in component Ca_independent_transient_outward_K_current_r_gate (dimensionless)"
    legend_rates[7] = "d/dt s in component Ca_independent_transient_outward_K_current_s_gate (dimensionless)"
    legend_rates[8] = "d/dt s_slow in component Ca_independent_transient_outward_K_current_s_slow_gate (dimensionless)"
    legend_rates[9] = "d/dt r_ss in component steady_state_outward_K_current_r_ss_gate (dimensionless)"
    legend_rates[10] = "d/dt s_ss in component steady_state_outward_K_current_s_ss_gate (dimensionless)"
    legend_rates[11] = "d/dt y in component hyperpolarisation_activated_current_y_gate (dimensionless)"
    legend_rates[15] = "d/dt HCO3i in component intracellular_ion_concentrations (mM)"
    legend_rates[12] = "d/dt CO2i in component intracellular_ion_concentrations (mM)"
    legend_rates[13] = "d/dt pH_i in component intracellular_ion_concentrations (dimensionless)"
    legend_rates[1] = "d/dt Na_i in component intracellular_ion_concentrations (mM)"
    legend_rates[5] = "d/dt K_i in component intracellular_ion_concentrations (mM)"
    legend_rates[14] = "d/dt Cli in component intracellular_ion_concentrations (mM)"
    legend_rates[17] = "d/dt Ca_SR in component ionic_concentrations (mM)"
    legend_rates[16] = "d/dt Ca_i in component ionic_concentrations (mM)"
    legend_rates[18] = "d/dt TRPN in component ionic_concentrations (mM)"
    legend_rates[19] = "d/dt z_1 in component z_i (dimensionless)"
    legend_rates[20] = "d/dt z_2 in component z_i (dimensionless)"
    legend_rates[21] = "d/dt z_3 in component z_i (dimensionless)"
    legend_rates[22] = "d/dt z in component tropomyosin (dimensionless)"
    legend_rates[23] = "d/dt Q_1 in component Cross_Bridges (dimensionless)"
    legend_rates[24] = "d/dt Q_2 in component Cross_Bridges (dimensionless)"
    legend_rates[25] = "d/dt Q_3 in component Cross_Bridges (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts(args):

    initialise = False
    if args.initstate is not None:
        if not os.path.exists(args.initstate):
            raise Exception("Cannot find requested initialisation state file "+args.initstate)
        print("Initialising simulation with "+args.initstate)
        initial_state = numpy.loadtxt(args.initstate,dtype=float)
        initialise = True

    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    constants[0] = 0
    constants[1] = 0
    constants[2] = 0
    constants[3] = 2.584e-5
    constants[4] = 2.098e-6
    constants[5] = 75000
    constants[6] = 0.01534
    states[0] = -80.5561112771341 if not initialise else initial_state[0]
    constants[7] = 8314.5
    constants[8] = 295
    constants[9] = 96487
    constants[10] = 0.0001
    # constants[11] = 1000
    constants[11] = float(args.bcl)
    constants[12] = 10
    constants[13] = -0.0006
    constants[14] = 1
    constants[15] = 4.1333e-7
    constants[16] = -10
    constants[17] = 1.2e-6
    constants[18] = 0.0008
    states[1] = 10.9735342589175 if not initialise else initial_state[1]
    constants[19] = 140
    states[2] = 0.00419283833975832 if not initialise else initial_state[2]
    states[3] = 0.675647510010602 if not initialise else initial_state[3]
    states[4] = 0.675294627571238 if not initialise else initial_state[4]
    constants[20] = 3.5e-5
    constants[21] = 0.583
    constants[22] = 0.417
    constants[23] = 5.4
    states[5] = 142.021261491871 if not initialise else initial_state[5]
    states[6] = 0.00218107055088884 if not initialise else initial_state[6]
    states[7] = 0.922573773425153 if not initialise else initial_state[7]
    states[8] = 0.530207467628341 if not initialise else initial_state[8]
    constants[24] = 7e-6
    states[9] = 0.00289374682707489 if not initialise else initial_state[9]
    states[10] = 0.308572839431787 if not initialise else initial_state[10]
    constants[25] = 2.4e-5
    constants[26] = 1.45e-6
    constants[27] = 0.2
    states[11] = 0.00331726547133295 if not initialise else initial_state[11]
    constants[28] = 8.015e-8
    constants[29] = 1.38e-7
    constants[30] = float(args.iNa_b_scale_factor)
    constants[31] = float(args.iK_b_scale_factor)
    constants[32] = 9.5e-5
    constants[33] = 1.5
    constants[34] = 10*float(args.Km_Na_factor)
    constants[35] = 5.8e-5
    states[12] = 1.23610845162584 if not initialise else initial_state[12]
    states[13] = 7.20905044774657 if not initialise else initial_state[13]
    # constants[36] = 7.4
    constants[36] = float(args.pH_e)
    constants[37] = 21.4935205515214
    constants[38] = 1.77948608115949e-7
    constants[39] = 0.51156085723193*float(args.nhe_factor)
    # constants[39] = 0.51156085723193
    constants[40] = 0.14069285629105
    constants[41] = 0.001698
    constants[42] = 0.000416869383470335
    constants[43] = 2
    constants[44] = 0.35
    constants[45] = 126
    states[14] = 16.2285651746901 if not initialise else initial_state[14]
    constants[46] = 17970.36
    constants[47] = 0.0008907
    constants[48] = 14975.6
    constants[49] = 257.4
    constants[50] = 4084.9
    constants[51] = 0.35
    states[15] = 15.1428688811927 if not initialise else initial_state[15]
    constants[52] = 4866.11
    constants[53] = 0.008017
    constants[54] = 4677
    constants[55] = 777.92
    constants[56] = 6.656
    constants[57] = 0.000183
    constants[58] = 2.91
    constants[59] = 6.53e-5
    constants[60] = 2.18
    constants[61] = 0.35
    constants[62] = 983.5
    constants[63] = 110.64
    constants[64] = 20789.9
    constants[65] = 21118.2
    constants[66] = 21256.54
    constants[67] = 2.67e-5
    constants[68] = 5.11
    constants[69] = 0.000312
    constants[70] = 1.44
    constants[71] = 0.35
    constants[72] = 0.05
    constants[73] = 0.03253
    constants[74] = 760
    constants[75] = 0.000365
    constants[76] = 0.481
    constants[77] = 6.40013149605198
    constants[78] = 31.2044223705215
    constants[79] = 7.48048792987277
    constants[80] = 6.84513535697271
    constants[81] = 1
    constants[82] = 2e-5
    constants[83] = 4e-6
    constants[84] = 0
    constants[85] = 2
    constants[86] = 3.5e-6
    constants[87] = 0.0005
    states[16] = 8.60587059887361e-5 if not initialise else initial_state[16]
    constants[88] = 0.075
    constants[89] = 2.4216e-8
    constants[90] = 87.5
    constants[91] = 1.38
    constants[92] = 0.35
    constants[93] = 0.1
    constants[94] = 0.0385
    constants[95] = 0.00045
    constants[96] = 0.0005
    states[17] = 0.843733859307907 if not initialise else initial_state[17]
    states[18] = 0.0670845085340179 if not initialise else initial_state[18]
    constants[97] = 0.05
    constants[98] = 0.00238
    constants[99] = 5.2e-6
    constants[100] = 0.07
    constants[101] = 6.5e-11
    constants[102] = 2e-11
    constants[103] = 9.13e-13
    constants[104] = -2
    constants[105] = 7
    constants[106] = 1
    constants[107] = 0.0625
    constants[108] = 14
    constants[109] = 650
    constants[110] = 0.00022
    constants[111] = 2.35
    constants[112] = 0.05
    constants[113] = 2.43
    constants[114] = 0.012
    constants[115] = 0.041
    constants[116] = 0.01
    constants[117] = 100
    states[19] = 0.988955429362334 if not initialise else initial_state[19]
    states[20] = 0.00860686643357905 if not initialise else initial_state[20]
    states[21] = 0.00241692704700704 if not initialise else initial_state[21]
    constants[118] = 100
    constants[119] = 0.2
    constants[120] = 2
    constants[121] = 0.07
    constants[122] = 56.2
    states[22] = 0.0175189833295748 if not initialise else initial_state[22]
    constants[123] = 0.008
    constants[124] = 0.002
    constants[125] = 0.00175
    constants[126] = 3
    constants[127] = 0.15
    constants[128] = 3
    constants[129] = 0.00105
    constants[130] = 0.85
    constants[131] = -4
    constants[132] = 4.9
    constants[133] = 0.35
    states[23] = 0 if not initialise else initial_state[23]
    states[24] = 0 if not initialise else initial_state[24]
    states[25] = 0 if not initialise else initial_state[25]
    constants[134] = -29
    constants[135] = 138
    constants[136] = 129
    constants[137] = 0.03
    constants[138] = 0.13
    constants[139] = 0.625
    constants[140] = constants[6]/constants[3]
    constants[141] = custom_piecewise([numpy.equal(constants[2] , 1.00000), (constants[14]-1.00000)*10.0000 , True, 0.00000])
    constants[142] = -(constants[16]+85.0000)/(constants[16]-65.0000)
    constants[143] = custom_piecewise([numpy.equal(constants[2] , 1.00000), 0.700000+(constants[14]-1.00000)*3.00000 , True, 0.700000])
    constants[144] = 1.33000*constants[18]
    constants[145] = 0.464700*constants[20]
    constants[146] = 2100.00
    constants[147] = 1.00000-constants[27]
    constants[148] = (numpy.exp(constants[19]/67.3000)-1.00000)/7.00000
    constants[149] = constants[10]/constants[6]
    constants[150] = 1000.00*(numpy.power(10.0000, -constants[36]))
    constants[151] = numpy.power(constants[19], 3.00000)
    constants[152] = 1.17000*constants[106]
    constants[153] = custom_piecewise([numpy.greater(constants[14] , 0.800000) & numpy.less_equal(constants[14] , 1.15000), constants[14] , numpy.greater(constants[14] , 1.15000), 1.15000 , True, 0.800000])
    constants[154] = 0.00000
    constants[155] = constants[14]
    constants[156] = custom_piecewise([numpy.equal(constants[1] , 1.00000), 1.00000-2.80400*(constants[14]-1.00000) , True, 1.00000])
    constants[157] = constants[111]/constants[106]
    constants[158] = ((constants[125]*(numpy.power(constants[130], constants[126])))/(numpy.power(constants[130], constants[126])+numpy.power(constants[127], constants[126])))*(1.00000-(constants[126]*(numpy.power(constants[127], constants[126])))/(numpy.power(constants[130], constants[126])+numpy.power(constants[127], constants[126])))
    constants[159] = 1.00000+constants[132]*(constants[153]-1.00000)
    constants[160] = constants[42]*constants[156]
    constants[161] = custom_piecewise([numpy.equal(constants[0] , 1.00000), 1.00000+22.4100*(constants[14]-1.00000) , True, 1.00000])
    constants[162] = (constants[125]*(numpy.power(constants[130], constants[126]-1.00000))*constants[126]*(numpy.power(constants[127], constants[126])))/(numpy.power(numpy.power(constants[130], constants[126])+numpy.power(constants[127], constants[126]), 2.00000))
    constants[163] = (constants[39]*constants[41])/constants[40]
    constants[164] = constants[112]*constants[161]
    constants[165] = constants[129]*(1.00000+constants[131]*(constants[153]-1.00000))
    constants[166] = (numpy.power(10.0000, -constants[36]))*1000.00
    constants[167] = constants[164]/constants[152]
    constants[168] = (constants[165]*constants[121])/(constants[165]+(constants[119]/constants[118])*(1.00000-((1.00000+constants[132]*(constants[153]-1.00000))*0.500000)/constants[120]))
    constants[169] = (constants[38]*constants[19]*constants[39])/(constants[37]*constants[38]+constants[38]*constants[19]+constants[19]*constants[166]+constants[37]*constants[166])
    constants[170] = (constants[123]/(numpy.power(constants[168]/constants[121], constants[128]))-constants[158])/(constants[124]+constants[162]+constants[123]/(numpy.power(constants[168]/constants[121], constants[128])))
    constants[171] = (constants[37]*constants[166]*constants[163])/(constants[37]*constants[38]+constants[38]*constants[19]+constants[19]*constants[166]+constants[37]*constants[166])
    constants[172] = (constants[50]*constants[49])/constants[48]
    constants[173] = 1000.00*(numpy.power(10.0000, -14.0000+constants[36]))
    constants[174] = 1.00000+constants[47]/constants[173]+(constants[47]*constants[45])/(constants[173]*constants[46])
    constants[175] = 1.00000+constants[46]/constants[45]+(constants[46]*constants[173])/(constants[45]*constants[47])
    constants[176] = (constants[56]*constants[55])/constants[54]
    constants[177] = 1000.00*(numpy.power(10.0000, -constants[36]))
    constants[178] = custom_piecewise([numpy.equal(constants[1] , 1.00000), 1.00000+2.50000*(constants[14]-1.00000) , True, 1.00000])
    constants[179] = constants[67]*constants[178]
    constants[180] = (constants[66]*constants[65])/constants[64]
    constants[181] = 1000.00*(numpy.power(10.0000, -constants[36]))
    constants[182] = constants[72]*constants[73]*constants[74]*float(args.bicarb_factor)
    constants[183] = ((constants[75]/constants[76])*constants[182])/((numpy.power(10.0000, -constants[36]))*1000.00)
    constants[184] = 1.00000+constants[19]/constants[52]+(constants[19]*constants[183])/(constants[52]*constants[53])
    constants[185] = 1.00000+constants[53]/constants[183]+(constants[52]*constants[53])/(constants[183]*constants[19])
    constants[186] = 1.00000+constants[63]/constants[183]+(constants[63]*constants[45])/(constants[183]*constants[62])
    constants[187] = 1.00000+constants[62]/constants[45]+(constants[62]*constants[183])/(constants[45]*constants[63])
    constants[188] = 0.621 # b_t for pH-dendendence in tension
    constants[189] = 7.15  # pH_ref
    constants[190] = 1.14  # n_up for pH-dendence in SERCA uptake
    constants[191] = 7.53  # pKup for pH-dendence in SERCA uptake
    constants[192] = 0.991 # nNaCa for pH-dendence in NCX 
    constants[193] = 7.37  # pKNaCa for pH-dendence in NCX 
    constants[194] = 1.87  # nrel for pH-dendence in RyR 
    constants[195] = 6.64  # pKrel for pH-dendence in RyR 

    return (states, constants)

def computeRates(voi, states, constants):

    # -----------------------------------------
    # updating constants with pH dependence

    # Reference tension
    constants[122] = 56.2 * (1+constants[188]*(states[13]-constants[189]))

    # SERCA
    constants[95] = 0.00045 * (1.0 + numpy.power(10.0000, constants[190] * (-constants[189] + constants[191])))/(1.0 + numpy.power(10.0000, constants[190] * (-states[13] + constants[191])))
 
    # NCX
    constants[94] = 0.0385 * (1.0 + numpy.power(10.0000, constants[192] * (-constants[189] + constants[193])))/(1.0 + numpy.power(10.0000, constants[192] * (-states[13] + constants[193])))

    # RyR
    constants[102] = 2e-11 * (1.0 + numpy.power(10.0000, constants[194] * (-constants[189] + constants[195])))/(1.0 + numpy.power(10.0000, constants[194] * (-states[13] + constants[195])))

    # -----------------------------------------

    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    rates[23] = constants[134]*constants[154]-constants[137]*states[23]
    rates[24] = constants[135]*constants[154]-constants[138]*states[24]
    rates[25] = constants[136]*constants[154]-constants[139]*states[25]
    algebraic[7] = 1.00000/(1.00000+numpy.exp((states[0]+87.5000)/10.3000))
    rates[10] = (algebraic[7]-states[10])/constants[146]
    algebraic[0] = 1.00000/(1.00000+numpy.exp((states[0]+45.0000)/-6.50000))
    algebraic[12] = 1.36000/((0.320000*(states[0]+47.1300))/(1.00000-numpy.exp(-0.100000*(states[0]+47.1300)))+0.0800000*numpy.exp(-states[0]/11.0000))
    rates[2] = (algebraic[0]-states[2])/algebraic[12]
    algebraic[1] = 1.00000/(1.00000+numpy.exp((states[0]+76.1000)/6.07000))
    algebraic[13] = custom_piecewise([numpy.greater_equal(states[0] , -40.0000), 0.453700*(1.00000+numpy.exp(-(states[0]+10.6600)/11.1000)) , True, 3.49000/(0.135000*numpy.exp(-(states[0]+80.0000)/6.80000)+3.56000*numpy.exp(0.0790000*states[0])+310000.*numpy.exp(0.350000*states[0]))])
    rates[3] = (algebraic[1]-states[3])/algebraic[13]
    algebraic[2] = 1.00000/(1.00000+numpy.exp((states[0]+76.1000)/6.07000))
    algebraic[14] = custom_piecewise([numpy.greater_equal(states[0] , -40.0000), (11.6300*(1.00000+numpy.exp(-0.100000*(states[0]+32.0000))))/numpy.exp(-2.53500e-07*states[0]) , True, 3.49000/(((states[0]+37.7800)/(1.00000+numpy.exp(0.311000*(states[0]+79.2300))))*(-127140.*numpy.exp(0.244400*states[0])-3.47400e-05*numpy.exp(-0.0439100*states[0]))+(0.121200*numpy.exp(-0.0105200*states[0]))/(1.00000+numpy.exp(-0.137800*(states[0]+40.1400))))])
    rates[4] = (algebraic[2]-states[4])/algebraic[14]
    algebraic[15] = 1000.00/(45.1600*numpy.exp(0.0357700*(states[0]+50.0000))+98.9000*numpy.exp(-0.100000*(states[0]+38.0000)))
    algebraic[3] = 1.00000/(1.00000+numpy.exp((states[0]+10.6000)/-11.4200))
    rates[6] = (algebraic[3]-states[6])/algebraic[15]
    algebraic[16] = 550.000*numpy.exp(-(numpy.power((states[0]+70.0000)/25.0000, 2.00000)))+49.0000
    algebraic[4] = 1.00000/(1.00000+numpy.exp((states[0]+45.3000)/6.88410))
    rates[7] = (algebraic[4]-states[7])/algebraic[16]
    algebraic[17] = 3300.00*numpy.exp(-(numpy.power((states[0]+70.0000)/30.0000, 2.00000)))+49.0000
    algebraic[5] = 1.00000/(1.00000+numpy.exp((states[0]+45.3000)/6.88410))
    rates[8] = (algebraic[5]-states[8])/algebraic[17]
    algebraic[18] = 10000.0/(45.1600*numpy.exp(0.0357700*(states[0]+50.0000))+98.9000*numpy.exp(-0.100000*(states[0]+38.0000)))
    algebraic[6] = 1.00000/(1.00000+numpy.exp((states[0]+11.5000)/-11.8200))
    rates[9] = (algebraic[6]-states[9])/algebraic[18]
    algebraic[19] = 1000.00/(0.118850*numpy.exp((states[0]+80.0000)/28.3700)+0.562300*numpy.exp((states[0]+80.0000)/-14.1900))
    algebraic[8] = 1.00000/(1.00000+numpy.exp((states[0]+138.600)/10.4800))
    rates[11] = (algebraic[8]-states[11])/algebraic[19]
    algebraic[10] = constants[100]-states[18]
    algebraic[21] = constants[123]*(numpy.power(algebraic[10]/constants[168], constants[128]))
    algebraic[23] = constants[124]+(constants[125]*(numpy.power(states[22], constants[126]-1.00000)))/(numpy.power(states[22], constants[126])+numpy.power(constants[127], constants[126]))
    rates[22] = algebraic[21]*(1.00000-states[22])-algebraic[23]*states[22]
    algebraic[25] = ((constants[7]*constants[8])/constants[9])*math.log(constants[23]/states[5])
    algebraic[30] = (constants[145]*states[6]*(constants[21]*states[7]+constants[22]*states[8])*(states[0]-algebraic[25]))/constants[6]
    algebraic[31] = (constants[24]*states[9]*states[10]*(states[0]-algebraic[25]))/constants[6]
    algebraic[32] = (((0.0480000/(numpy.exp((states[0]+37.0000)/25.0000)+numpy.exp((states[0]+37.0000)/-25.0000))+0.0100000)*0.00100000)/(1.00000+numpy.exp((states[0]-(algebraic[25]+76.7700))/-17.0000))+(constants[25]*(states[0]-(algebraic[25]+1.73000)))/((1.00000+numpy.exp((1.61300*constants[9]*(states[0]-(algebraic[25]+1.73000)))/(constants[7]*constants[8])))*(1.00000+numpy.exp((constants[23]-0.998800)/-0.124000))))/constants[6]
    algebraic[39] = 1.00000/(1.00000+numpy.power(constants[34]/states[1], 4.00000))
    algebraic[40] = 1.00000/(1.00000+0.124500*numpy.exp((-0.100000*states[0]*constants[9])/(constants[7]*constants[8]))+0.0365000*constants[148]*numpy.exp((-states[0]*constants[9])/(constants[7]*constants[8])))
    algebraic[41] = (((constants[32]/constants[6])*algebraic[40]*constants[23])/(constants[23]+constants[33]))*algebraic[39]
    algebraic[9] = custom_piecewise([numpy.greater_equal(voi-math.floor(voi/constants[11])*constants[11] , 0.00000) & numpy.less_equal(voi-math.floor(voi/constants[11])*constants[11] , constants[12]), constants[13]/constants[6] , True, 0.00000])
    algebraic[38] = (constants[31]*constants[29]*(states[0]-algebraic[25]))/constants[6]
    algebraic[27] = (constants[15]*constants[141]*(states[0]-algebraic[25]))/constants[6]
    algebraic[29] = ((constants[17]/(1.00000+numpy.exp(-(10.0000+states[0])/45.0000)))*(states[0]-algebraic[25])*constants[143])/constants[6]
    algebraic[34] = (constants[26]*states[11]*constants[147]*(states[0]-algebraic[25]))/constants[6]
    rates[5] = (-(((algebraic[9]+algebraic[27]+algebraic[31]+algebraic[29]+algebraic[30]+algebraic[32]+algebraic[34])-2.00000*algebraic[41])+algebraic[38])*constants[6])/(constants[3]*constants[9])
    algebraic[72] = ((constants[7]*constants[8])/constants[9])*math.log(states[14]/constants[45])
    algebraic[73] = constants[82]*(states[0]-algebraic[72])
    algebraic[52] = 1000.00*(numpy.power(10.0000, -14.0000+states[13]))
    algebraic[53] = 1.00000+constants[46]/states[14]+(constants[46]*algebraic[52])/(states[14]*constants[47])
    algebraic[54] = 1.00000+constants[47]/algebraic[52]+(constants[47]*states[14])/(algebraic[52]*constants[46])
    algebraic[55] = 1.00000/(constants[174]+(algebraic[54]*(constants[48]+(constants[50]*constants[174])/constants[175]))/(constants[49]+(constants[172]*algebraic[54])/algebraic[53]))
    algebraic[56] = 1.00000/(algebraic[54]+(constants[174]*(constants[49]+(constants[172]*algebraic[54])/algebraic[53]))/(constants[48]+(constants[50]*constants[174])/constants[175]))
    algebraic[57] = ((constants[3]*(constants[49]*algebraic[56]-constants[48]*algebraic[55]))/(60.0000*1000.00))*constants[51]
    algebraic[66] = 1.00000+constants[62]/states[14]+(constants[62]*states[15])/(states[14]*constants[63])
    algebraic[67] = 1.00000+constants[63]/states[15]+(constants[63]*states[14])/(states[15]*constants[62])
    algebraic[68] = 1.00000/(constants[186]+(algebraic[67]*(constants[64]+(constants[66]*constants[186])/constants[187]))/(constants[65]+(constants[180]*algebraic[67])/algebraic[66]))
    algebraic[69] = 1.00000/(algebraic[67]+(constants[186]*(constants[65]+(constants[180]*algebraic[67])/algebraic[66]))/(constants[64]+(constants[66]*constants[186])/constants[187]))
    algebraic[65] = 1000.00*(numpy.power(10.0000, -states[13]))
    algebraic[70] = (((numpy.power(constants[179], constants[68]))/(numpy.power(algebraic[65], constants[68])+numpy.power(constants[179], constants[68])))*(numpy.power(constants[181], constants[70])))/(numpy.power(constants[181], constants[70])+numpy.power(constants[69], constants[70]))
    algebraic[71] = ((constants[3]*algebraic[70]*(constants[65]*algebraic[69]-constants[64]*algebraic[68]))/(60.0000*1000.00))*constants[71]
    rates[14] = (algebraic[73]*constants[6])/(constants[3]*constants[9])+(constants[81]*(algebraic[57]+algebraic[71]))/constants[3]
    algebraic[58] = 1.00000+constants[53]/states[15]+(constants[52]*constants[53])/(states[15]*states[1])
    algebraic[59] = 1.00000+states[1]/constants[52]+(states[1]*states[15])/(constants[52]*constants[53])
    algebraic[61] = 1.00000/(constants[184]+(algebraic[59]*(constants[54]+(constants[56]*constants[184])/constants[185]))/(constants[55]+(constants[176]*algebraic[59])/algebraic[58]))
    algebraic[62] = 1.00000/(algebraic[59]+(constants[184]*(constants[55]+(constants[176]*algebraic[59])/algebraic[58]))/(constants[54]+(constants[56]*constants[184])/constants[185]))
    algebraic[60] = 1000.00*(numpy.power(10.0000, -states[13]))
    algebraic[63] = ((numpy.power(algebraic[60], constants[58]))/(numpy.power(algebraic[60], constants[58])+numpy.power(constants[57], constants[58])))*(1.00000-(numpy.power(constants[177], constants[60]))/(numpy.power(constants[177], constants[60])+numpy.power(constants[59], constants[60])))
    algebraic[64] = ((constants[3]*algebraic[63]*(constants[55]*algebraic[62]-constants[54]*algebraic[61]))/(60.0000*1000.00))*constants[61]
    algebraic[79] = (constants[3]+constants[4])*(constants[75]*states[12]-constants[76]*states[15]*(numpy.power(10.0000, -states[13]))*1000.00)
    rates[15] = algebraic[79]/(constants[3]+constants[4])+(algebraic[64]-algebraic[71])/constants[3]
    algebraic[42] = constants[3]*constants[140]*constants[35]*(constants[182]-states[12])
    rates[12] = (algebraic[42]/constants[3]-algebraic[79]/(constants[3]+constants[4]))+constants[84]
    algebraic[74] = 1000.00*(numpy.power(10.0000, -states[13]))
    algebraic[75] = ((constants[7]*constants[8])/constants[9])*math.log(constants[150]/algebraic[74])
    algebraic[76] = constants[83]*(states[0]-algebraic[75])+float(args.H_constant)
    algebraic[46] = (numpy.power(10.0000, -states[13]))*1000.00
    algebraic[47] = (constants[38]*states[1]*constants[40])/(constants[37]*constants[38]+constants[38]*states[1]+states[1]*algebraic[46]+constants[37]*algebraic[46])
    algebraic[48] = (constants[37]*algebraic[46]*constants[41])/(constants[37]*constants[38]+constants[38]*states[1]+states[1]*algebraic[46]+constants[37]*algebraic[46])
    algebraic[49] = (numpy.power(algebraic[46], constants[43]))/(numpy.power(algebraic[46], constants[43])+numpy.power(constants[160], constants[43]))
    algebraic[50] = (algebraic[49]*(constants[169]*algebraic[48]-algebraic[47]*constants[171]))/(constants[169]+algebraic[48]+algebraic[47]+constants[171])
    algebraic[51] = algebraic[50]*constants[3]*constants[44]
    algebraic[77] = math.log(10.0000)*(numpy.power(10.0000, -states[13])+((numpy.power(10.0000, states[13]+constants[77]))*constants[78])/(numpy.power(numpy.power(10.0000, states[13])+numpy.power(10.0000, constants[77]), 2.00000))+((numpy.power(10.0000, states[13]+constants[79]))*constants[80])/(numpy.power(numpy.power(10.0000, states[13])+numpy.power(10.0000, constants[79]), 2.00000)))
    rates[13] = (1.00000/-algebraic[77])*(((-algebraic[51]+algebraic[57])/constants[3]+algebraic[79]/(constants[3]+constants[4]))-(algebraic[76]*constants[6])/(constants[3]*constants[9]))
    algebraic[20] = ((constants[7]*constants[8])/constants[9])*math.log(constants[19]/states[1])
    algebraic[24] = (constants[144]*(numpy.power(states[2], 3.00000))*states[3]*states[4]*(states[0]-algebraic[20]))/constants[6]
    algebraic[84] = numpy.exp(constants[88]*0.500000*states[0]*constants[92])
    algebraic[85] = numpy.exp(constants[88]*0.500000*states[0]*(constants[92]-1.00000))
    algebraic[86] = numpy.power(states[1], 3.00000)
    algebraic[87] = ((((constants[94]/((constants[151]+numpy.power(constants[90], 3.00000))*(constants[85]+constants[91])))*(algebraic[84]*algebraic[86]*constants[85]-algebraic[85]*constants[151]*states[16]))/(1.00000+constants[93]*algebraic[85]))*constants[3]*constants[9])/constants[6]
    algebraic[37] = (constants[30]*constants[28]*(states[0]-algebraic[20]))/constants[6]
    algebraic[22] = ((constants[15]*constants[141]*(states[0]-algebraic[20]))/constants[6])*constants[142]
    algebraic[33] = (constants[26]*states[11]*constants[27]*(states[0]-algebraic[20]))/constants[6]
    rates[1] = (-(algebraic[37]+algebraic[22]+algebraic[24]+algebraic[87]*3.00000+algebraic[41]*3.00000+algebraic[33])*constants[6])/(constants[3]*constants[9])+(algebraic[51]+algebraic[64])/constants[3]
    algebraic[36] = algebraic[33]+algebraic[34]
    algebraic[92] = constants[88]*states[0]
    algebraic[93] = numpy.exp(-algebraic[92])
    algebraic[101] = custom_piecewise([numpy.greater(math.fabs(algebraic[92]) , 1.00000e-05), (((constants[103]*algebraic[92])/(1.00000-algebraic[93]))*((constants[85]*algebraic[93]-states[16])+(constants[102]/constants[101])*(constants[85]*algebraic[93]-states[17])))/(1.00000+constants[102]/constants[101]+((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93])) , True, (((constants[103]*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))*((constants[85]*numpy.exp(-1.00000e-05)-states[16])+(constants[102]/constants[101])*(constants[85]*numpy.exp(-1.00000e-05)-states[17])))/(1.00000+constants[102]/constants[101]+((constants[103]/constants[101])*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))])
    algebraic[100] = custom_piecewise([numpy.greater(math.fabs(algebraic[92]) , 1.00000e-05), (((constants[103]*algebraic[92])/(1.00000-algebraic[93]))*(constants[85]*algebraic[93]-states[16]))/(1.00000+((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93])) , True, (((constants[103]*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))*(constants[85]*numpy.exp(-1.00000e-05)-states[16]))/(1.00000+((constants[103]/constants[101])*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))])
    algebraic[94] = numpy.exp((states[0]-constants[104])/constants[105])
    algebraic[105] = algebraic[94]/(constants[106]*(algebraic[94]+1.00000))
    algebraic[107] = ((1.00000/constants[152])*(numpy.power(states[16], 2.00000)))/(numpy.power(states[16], 2.00000)+numpy.power(constants[115], 2.00000))
    algebraic[97] = custom_piecewise([numpy.greater(math.fabs(algebraic[92]) , 1.00000e-09), (states[16]+((constants[103]/constants[101])*constants[85]*algebraic[92]*algebraic[93])/(1.00000-algebraic[93]))/(1.00000+((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93])) , True, (states[16]+(constants[103]/constants[101])*constants[85])/(1.00000+constants[103]/constants[101])])
    algebraic[106] = ((1.00000/constants[152])*(numpy.power(algebraic[97], 2.00000)))/(numpy.power(algebraic[97], 2.00000)+numpy.power(constants[115], 2.00000))
    algebraic[112] = (algebraic[105]+constants[157])*((constants[167]+algebraic[106]+constants[157])*(constants[167]+algebraic[107])+algebraic[105]*(constants[167]+algebraic[106]))
    algebraic[113] = (algebraic[105]*constants[167]*(algebraic[105]+constants[157]+constants[167]+algebraic[107]))/algebraic[112]
    algebraic[115] = (algebraic[105]*(algebraic[106]*(algebraic[105]+constants[167]+algebraic[107])+algebraic[107]*constants[157]))/algebraic[112]
    algebraic[121] = algebraic[101]*algebraic[115]+algebraic[100]*algebraic[113]
    algebraic[123] = (algebraic[100]*algebraic[105])/(algebraic[105]+constants[157])
    algebraic[125] = ((states[19]*algebraic[121]+states[20]*algebraic[123])*constants[5])/constants[3]
    algebraic[127] = (-algebraic[125]*2.00000*constants[3]*constants[9])/constants[6]
    algebraic[82] = math.log(constants[85]/states[16], 10)/constants[88]
    algebraic[83] = (constants[89]*(states[0]-algebraic[82])*2.00000*constants[3]*constants[9])/constants[6]
    algebraic[81] = (((constants[86]*states[16])/(constants[87]+states[16]))*2.00000*constants[3]*constants[9])/constants[6]
    rates[0] = -(algebraic[76]+algebraic[73]+algebraic[24]+algebraic[127]+algebraic[30]+algebraic[31]+algebraic[36]+algebraic[32]+algebraic[83]+algebraic[22]+algebraic[38]+algebraic[37]+algebraic[29]+algebraic[27]+algebraic[41]+algebraic[87]+algebraic[81]+algebraic[9])/constants[149]
    algebraic[108] = ((1.00000/constants[113])*(numpy.power(algebraic[97], 2.00000)+constants[116]*(numpy.power(constants[115], 2.00000))))/(numpy.power(algebraic[97], 2.00000)+numpy.power(constants[115], 2.00000))
    algebraic[109] = ((1.00000/constants[113])*(numpy.power(states[16], 2.00000)+constants[116]*(numpy.power(constants[115], 2.00000))))/(numpy.power(states[16], 2.00000)+numpy.power(constants[115], 2.00000))
    algebraic[116] = (constants[157]*constants[167]*(constants[157]+algebraic[105]+constants[167]+algebraic[106]))/algebraic[112]
    algebraic[118] = algebraic[113]*algebraic[108]+algebraic[116]*algebraic[109]
    algebraic[110] = ((constants[114]/constants[113])*constants[117]*(numpy.power(algebraic[97], 2.00000)+constants[116]*(numpy.power(constants[115], 2.00000))))/(constants[117]*(numpy.power(algebraic[97], 2.00000))+constants[116]*(numpy.power(constants[115], 2.00000)))
    algebraic[111] = ((constants[114]/constants[113])*constants[117]*(numpy.power(states[16], 2.00000)+constants[116]*(numpy.power(constants[115], 2.00000))))/(constants[117]*(numpy.power(states[16], 2.00000))+constants[116]*(numpy.power(constants[115], 2.00000)))
    algebraic[120] = (algebraic[105]*algebraic[110]+constants[157]*algebraic[111])/(algebraic[105]+constants[157])
    algebraic[96] = (states[16]+(constants[102]/constants[101])*states[17])/(1.00000+constants[102]/constants[101])
    algebraic[102] = ((((1.00000/constants[109])*algebraic[96])/constants[110])*(algebraic[94]+constants[107]))/(algebraic[94]+1.00000)
    algebraic[103] = ((((1.00000/constants[109])*states[16])/constants[110])*(algebraic[94]+constants[107]))/(algebraic[94]+1.00000)
    algebraic[114] = (constants[157]*(algebraic[107]*(constants[157]+constants[167]+algebraic[106])+algebraic[106]*algebraic[105]))/algebraic[112]
    algebraic[126] = algebraic[114]*algebraic[102]+algebraic[116]*algebraic[103]
    algebraic[104] = ((1.00000/constants[109])*constants[108]*(algebraic[94]+constants[107]))/(constants[108]*algebraic[94]+constants[107])
    algebraic[128] = algebraic[104]
    rates[19] = -(algebraic[118]+algebraic[126])*states[19]+algebraic[120]*states[20]+algebraic[128]*states[21]
    algebraic[90] = (constants[95]*(numpy.power(states[16], 2.00000)))/(numpy.power(constants[96], 2.00000)+numpy.power(states[16], 2.00000))
    algebraic[98] = (constants[102]*(states[17]-states[16]))/(1.00000+constants[102]/constants[101])
    algebraic[99] = custom_piecewise([numpy.greater(math.fabs(algebraic[92]) , 1.00000e-05), (constants[102]*((states[17]-states[16])+(((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93]))*(states[17]-constants[85]*algebraic[93])))/(1.00000+constants[102]/constants[101]+((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93])) , True, (constants[102]*((states[17]-states[16])+(((constants[103]/constants[101])*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))*(states[17]-constants[85]*numpy.exp(-1.00000e-05))))/(1.00000+constants[102]/constants[101]+((constants[103]/constants[101])*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))])
    algebraic[117] = algebraic[115]*algebraic[99]+algebraic[98]*algebraic[114]
    algebraic[119] = (algebraic[98]*algebraic[107])/(constants[167]+algebraic[107])
    algebraic[129] = ((states[19]*algebraic[117]+states[21]*algebraic[119])*constants[5])/constants[3]
    algebraic[131] = (-algebraic[129]+algebraic[90])-constants[99]*(states[17]-states[16])
    rates[17] = (constants[3]/constants[4])*algebraic[131]
    algebraic[130] = (constants[157]*algebraic[103])/(algebraic[105]+constants[157])
    algebraic[132] = algebraic[104]
    algebraic[133] = ((1.00000-states[19])-states[20])-states[21]
    rates[20] = (algebraic[118]*states[19]-(algebraic[120]+algebraic[130])*states[20])+algebraic[132]*algebraic[133]
    algebraic[122] = (constants[167]*algebraic[109])/(constants[167]+algebraic[107])
    algebraic[124] = algebraic[111]
    rates[21] = (algebraic[126]*states[19]-(algebraic[128]+algebraic[122])*states[21])+algebraic[124]*algebraic[133]
    algebraic[134] = (constants[122]*states[22])/constants[170]
    algebraic[135] = algebraic[134]*constants[159]
    algebraic[136] = states[23]+states[24]+states[25]
    algebraic[137] = custom_piecewise([numpy.less(algebraic[136] , 0.00000), (algebraic[135]*(constants[133]*algebraic[136]+1.00000))/(1.00000-algebraic[136]) , True, (algebraic[135]*(1.00000+(constants[133]+2.00000)*algebraic[136]))/(1.00000+algebraic[136])])
    algebraic[138] = custom_piecewise([numpy.greater(1.00000-algebraic[137]/(constants[120]*constants[122]) , 0.100000), constants[119]*(1.00000-algebraic[137]/(constants[120]*constants[122])) , True, constants[119]*0.100000])
    algebraic[139] = (constants[100]-states[18])*algebraic[138]-states[16]*states[18]*constants[118]
    rates[16] = (1.00000/(1.00000+(constants[97]*constants[98])/((states[16]+constants[98])*(states[16]+constants[98]))))*((algebraic[139]-algebraic[131])+((((2.00000*algebraic[87]-algebraic[81])-algebraic[83])-algebraic[127])*constants[6])/(2.00000*constants[3]*constants[9]))
    rates[18] = algebraic[139]
    return(rates)

def computeAlgebraic(constants, states, voi):

    # -----------------------------------------
    # updating constants with pH dependence

    # Reference tension
    constants[122] = 56.2 * (1+constants[188]*(states[13]-constants[189]))

    # SERCA
    constants[95] = 0.00045 * (1.0 + numpy.power(10.0000, constants[190] * (-constants[189] + constants[191])))/(1.0 + numpy.power(10.0000, constants[190] * (-states[13] + constants[191])))
 
    # NCX
    constants[94] = 0.0385 * (1.0 + numpy.power(10.0000, constants[192] * (-constants[189] + constants[193])))/(1.0 + numpy.power(10.0000, constants[192] * (-states[13] + constants[193])))

    # RyR
    constants[102] = 2e-11 * (1.0 + numpy.power(10.0000, constants[194] * (-constants[189] + constants[195])))/(1.0 + numpy.power(10.0000, constants[194] * (-states[13] + constants[195])))

    # -----------------------------------------

    algebraic = numpy.array([[0.0] * len(voi)] * sizeAlgebraic)
    states = numpy.array(states)
    voi = numpy.array(voi)
    algebraic[7] = 1.00000/(1.00000+numpy.exp((states[0]+87.5000)/10.3000))
    algebraic[0] = 1.00000/(1.00000+numpy.exp((states[0]+45.0000)/-6.50000))
    algebraic[12] = 1.36000/((0.320000*(states[0]+47.1300))/(1.00000-numpy.exp(-0.100000*(states[0]+47.1300)))+0.0800000*numpy.exp(-states[0]/11.0000))
    algebraic[1] = 1.00000/(1.00000+numpy.exp((states[0]+76.1000)/6.07000))
    algebraic[13] = custom_piecewise([numpy.greater_equal(states[0] , -40.0000), 0.453700*(1.00000+numpy.exp(-(states[0]+10.6600)/11.1000)) , True, 3.49000/(0.135000*numpy.exp(-(states[0]+80.0000)/6.80000)+3.56000*numpy.exp(0.0790000*states[0])+310000.*numpy.exp(0.350000*states[0]))])
    algebraic[2] = 1.00000/(1.00000+numpy.exp((states[0]+76.1000)/6.07000))
    algebraic[14] = custom_piecewise([numpy.greater_equal(states[0] , -40.0000), (11.6300*(1.00000+numpy.exp(-0.100000*(states[0]+32.0000))))/numpy.exp(-2.53500e-07*states[0]) , True, 3.49000/(((states[0]+37.7800)/(1.00000+numpy.exp(0.311000*(states[0]+79.2300))))*(-127140.*numpy.exp(0.244400*states[0])-3.47400e-05*numpy.exp(-0.0439100*states[0]))+(0.121200*numpy.exp(-0.0105200*states[0]))/(1.00000+numpy.exp(-0.137800*(states[0]+40.1400))))])
    algebraic[15] = 1000.00/(45.1600*numpy.exp(0.0357700*(states[0]+50.0000))+98.9000*numpy.exp(-0.100000*(states[0]+38.0000)))
    algebraic[3] = 1.00000/(1.00000+numpy.exp((states[0]+10.6000)/-11.4200))
    algebraic[16] = 550.000*numpy.exp(-(numpy.power((states[0]+70.0000)/25.0000, 2.00000)))+49.0000
    algebraic[4] = 1.00000/(1.00000+numpy.exp((states[0]+45.3000)/6.88410))
    algebraic[17] = 3300.00*numpy.exp(-(numpy.power((states[0]+70.0000)/30.0000, 2.00000)))+49.0000
    algebraic[5] = 1.00000/(1.00000+numpy.exp((states[0]+45.3000)/6.88410))
    algebraic[18] = 10000.0/(45.1600*numpy.exp(0.0357700*(states[0]+50.0000))+98.9000*numpy.exp(-0.100000*(states[0]+38.0000)))
    algebraic[6] = 1.00000/(1.00000+numpy.exp((states[0]+11.5000)/-11.8200))
    algebraic[19] = 1000.00/(0.118850*numpy.exp((states[0]+80.0000)/28.3700)+0.562300*numpy.exp((states[0]+80.0000)/-14.1900))
    algebraic[8] = 1.00000/(1.00000+numpy.exp((states[0]+138.600)/10.4800))
    algebraic[10] = constants[100]-states[18]
    algebraic[21] = constants[123]*(numpy.power(algebraic[10]/constants[168], constants[128]))
    algebraic[23] = constants[124]+(constants[125]*(numpy.power(states[22], constants[126]-1.00000)))/(numpy.power(states[22], constants[126])+numpy.power(constants[127], constants[126]))
    algebraic[25] = ((constants[7]*constants[8])/constants[9])*numpy.log(constants[23]/states[5])
    algebraic[30] = (constants[145]*states[6]*(constants[21]*states[7]+constants[22]*states[8])*(states[0]-algebraic[25]))/constants[6]
    algebraic[31] = (constants[24]*states[9]*states[10]*(states[0]-algebraic[25]))/constants[6]
    algebraic[32] = (((0.0480000/(numpy.exp((states[0]+37.0000)/25.0000)+numpy.exp((states[0]+37.0000)/-25.0000))+0.0100000)*0.00100000)/(1.00000+numpy.exp((states[0]-(algebraic[25]+76.7700))/-17.0000))+(constants[25]*(states[0]-(algebraic[25]+1.73000)))/((1.00000+numpy.exp((1.61300*constants[9]*(states[0]-(algebraic[25]+1.73000)))/(constants[7]*constants[8])))*(1.00000+numpy.exp((constants[23]-0.998800)/-0.124000))))/constants[6]
    algebraic[39] = 1.00000/(1.00000+numpy.power(constants[34]/states[1], 4.00000))
    algebraic[40] = 1.00000/(1.00000+0.124500*numpy.exp((-0.100000*states[0]*constants[9])/(constants[7]*constants[8]))+0.0365000*constants[148]*numpy.exp((-states[0]*constants[9])/(constants[7]*constants[8])))
    algebraic[41] = (((constants[32]/constants[6])*algebraic[40]*constants[23])/(constants[23]+constants[33]))*algebraic[39]
    algebraic[9] = custom_piecewise([numpy.greater_equal(voi-numpy.floor(voi/constants[11])*constants[11] , 0.00000) & numpy.less_equal(voi-numpy.floor(voi/constants[11])*constants[11] , constants[12]), constants[13]/constants[6] , True, 0.00000])
    algebraic[38] = (constants[31]*constants[29]*(states[0]-algebraic[25]))/constants[6]
    algebraic[27] = (constants[15]*constants[141]*(states[0]-algebraic[25]))/constants[6]
    algebraic[29] = ((constants[17]/(1.00000+numpy.exp(-(10.0000+states[0])/45.0000)))*(states[0]-algebraic[25])*constants[143])/constants[6]
    algebraic[34] = (constants[26]*states[11]*constants[147]*(states[0]-algebraic[25]))/constants[6]
    algebraic[72] = ((constants[7]*constants[8])/constants[9])*numpy.log(states[14]/constants[45])
    algebraic[73] = constants[82]*(states[0]-algebraic[72])
    algebraic[52] = 1000.00*(numpy.power(10.0000, -14.0000+states[13]))
    algebraic[53] = 1.00000+constants[46]/states[14]+(constants[46]*algebraic[52])/(states[14]*constants[47])
    algebraic[54] = 1.00000+constants[47]/algebraic[52]+(constants[47]*states[14])/(algebraic[52]*constants[46])
    algebraic[55] = 1.00000/(constants[174]+(algebraic[54]*(constants[48]+(constants[50]*constants[174])/constants[175]))/(constants[49]+(constants[172]*algebraic[54])/algebraic[53]))
    algebraic[56] = 1.00000/(algebraic[54]+(constants[174]*(constants[49]+(constants[172]*algebraic[54])/algebraic[53]))/(constants[48]+(constants[50]*constants[174])/constants[175]))
    algebraic[57] = ((constants[3]*(constants[49]*algebraic[56]-constants[48]*algebraic[55]))/(60.0000*1000.00))*constants[51]
    algebraic[66] = 1.00000+constants[62]/states[14]+(constants[62]*states[15])/(states[14]*constants[63])
    algebraic[67] = 1.00000+constants[63]/states[15]+(constants[63]*states[14])/(states[15]*constants[62])
    algebraic[68] = 1.00000/(constants[186]+(algebraic[67]*(constants[64]+(constants[66]*constants[186])/constants[187]))/(constants[65]+(constants[180]*algebraic[67])/algebraic[66]))
    algebraic[69] = 1.00000/(algebraic[67]+(constants[186]*(constants[65]+(constants[180]*algebraic[67])/algebraic[66]))/(constants[64]+(constants[66]*constants[186])/constants[187]))
    algebraic[65] = 1000.00*(numpy.power(10.0000, -states[13]))
    algebraic[70] = (((numpy.power(constants[179], constants[68]))/(numpy.power(algebraic[65], constants[68])+numpy.power(constants[179], constants[68])))*(numpy.power(constants[181], constants[70])))/(numpy.power(constants[181], constants[70])+numpy.power(constants[69], constants[70]))
    algebraic[71] = ((constants[3]*algebraic[70]*(constants[65]*algebraic[69]-constants[64]*algebraic[68]))/(60.0000*1000.00))*constants[71]
    algebraic[58] = 1.00000+constants[53]/states[15]+(constants[52]*constants[53])/(states[15]*states[1])
    algebraic[59] = 1.00000+states[1]/constants[52]+(states[1]*states[15])/(constants[52]*constants[53])
    algebraic[61] = 1.00000/(constants[184]+(algebraic[59]*(constants[54]+(constants[56]*constants[184])/constants[185]))/(constants[55]+(constants[176]*algebraic[59])/algebraic[58]))
    algebraic[62] = 1.00000/(algebraic[59]+(constants[184]*(constants[55]+(constants[176]*algebraic[59])/algebraic[58]))/(constants[54]+(constants[56]*constants[184])/constants[185]))
    algebraic[60] = 1000.00*(numpy.power(10.0000, -states[13]))
    algebraic[63] = ((numpy.power(algebraic[60], constants[58]))/(numpy.power(algebraic[60], constants[58])+numpy.power(constants[57], constants[58])))*(1.00000-(numpy.power(constants[177], constants[60]))/(numpy.power(constants[177], constants[60])+numpy.power(constants[59], constants[60])))
    algebraic[64] = ((constants[3]*algebraic[63]*(constants[55]*algebraic[62]-constants[54]*algebraic[61]))/(60.0000*1000.00))*constants[61]
    algebraic[79] = (constants[3]+constants[4])*(constants[75]*states[12]-constants[76]*states[15]*(numpy.power(10.0000, -states[13]))*1000.00)
    algebraic[42] = constants[3]*constants[140]*constants[35]*(constants[182]-states[12])
    algebraic[74] = 1000.00*(numpy.power(10.0000, -states[13]))
    algebraic[75] = ((constants[7]*constants[8])/constants[9])*numpy.log(constants[150]/algebraic[74])
    algebraic[76] = constants[83]*(states[0]-algebraic[75])+float(args.H_constant)
    algebraic[46] = (numpy.power(10.0000, -states[13]))*1000.00
    algebraic[47] = (constants[38]*states[1]*constants[40])/(constants[37]*constants[38]+constants[38]*states[1]+states[1]*algebraic[46]+constants[37]*algebraic[46])
    algebraic[48] = (constants[37]*algebraic[46]*constants[41])/(constants[37]*constants[38]+constants[38]*states[1]+states[1]*algebraic[46]+constants[37]*algebraic[46])
    algebraic[49] = (numpy.power(algebraic[46], constants[43]))/(numpy.power(algebraic[46], constants[43])+numpy.power(constants[160], constants[43]))
    algebraic[50] = (algebraic[49]*(constants[169]*algebraic[48]-algebraic[47]*constants[171]))/(constants[169]+algebraic[48]+algebraic[47]+constants[171])
    algebraic[51] = algebraic[50]*constants[3]*constants[44]
    algebraic[77] = math.log(10.0000)*(numpy.power(10.0000, -states[13])+((numpy.power(10.0000, states[13]+constants[77]))*constants[78])/(numpy.power(numpy.power(10.0000, states[13])+numpy.power(10.0000, constants[77]), 2.00000))+((numpy.power(10.0000, states[13]+constants[79]))*constants[80])/(numpy.power(numpy.power(10.0000, states[13])+numpy.power(10.0000, constants[79]), 2.00000)))
    algebraic[20] = ((constants[7]*constants[8])/constants[9])*numpy.log(constants[19]/states[1])
    algebraic[24] = (constants[144]*(numpy.power(states[2], 3.00000))*states[3]*states[4]*(states[0]-algebraic[20]))/constants[6]
    algebraic[84] = numpy.exp(constants[88]*0.500000*states[0]*constants[92])
    algebraic[85] = numpy.exp(constants[88]*0.500000*states[0]*(constants[92]-1.00000))
    algebraic[86] = numpy.power(states[1], 3.00000)
    algebraic[87] = ((((constants[94]/((constants[151]+numpy.power(constants[90], 3.00000))*(constants[85]+constants[91])))*(algebraic[84]*algebraic[86]*constants[85]-algebraic[85]*constants[151]*states[16]))/(1.00000+constants[93]*algebraic[85]))*constants[3]*constants[9])/constants[6]
    algebraic[37] = (constants[30]*constants[28]*(states[0]-algebraic[20]))/constants[6]
    algebraic[22] = ((constants[15]*constants[141]*(states[0]-algebraic[20]))/constants[6])*constants[142]
    algebraic[33] = (constants[26]*states[11]*constants[27]*(states[0]-algebraic[20]))/constants[6]
    algebraic[36] = algebraic[33]+algebraic[34]
    algebraic[92] = constants[88]*states[0]
    algebraic[93] = numpy.exp(-algebraic[92])
    algebraic[101] = custom_piecewise([numpy.greater(numpy.fabs(algebraic[92]) , 1.00000e-05), (((constants[103]*algebraic[92])/(1.00000-algebraic[93]))*((constants[85]*algebraic[93]-states[16])+(constants[102]/constants[101])*(constants[85]*algebraic[93]-states[17])))/(1.00000+constants[102]/constants[101]+((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93])) , True, (((constants[103]*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))*((constants[85]*numpy.exp(-1.00000e-05)-states[16])+(constants[102]/constants[101])*(constants[85]*numpy.exp(-1.00000e-05)-states[17])))/(1.00000+constants[102]/constants[101]+((constants[103]/constants[101])*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))])
    algebraic[100] = custom_piecewise([numpy.greater(numpy.fabs(algebraic[92]) , 1.00000e-05), (((constants[103]*algebraic[92])/(1.00000-algebraic[93]))*(constants[85]*algebraic[93]-states[16]))/(1.00000+((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93])) , True, (((constants[103]*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))*(constants[85]*numpy.exp(-1.00000e-05)-states[16]))/(1.00000+((constants[103]/constants[101])*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))])
    algebraic[94] = numpy.exp((states[0]-constants[104])/constants[105])
    algebraic[105] = algebraic[94]/(constants[106]*(algebraic[94]+1.00000))
    algebraic[107] = ((1.00000/constants[152])*(numpy.power(states[16], 2.00000)))/(numpy.power(states[16], 2.00000)+numpy.power(constants[115], 2.00000))
    algebraic[97] = custom_piecewise([numpy.greater(numpy.fabs(algebraic[92]) , 1.00000e-09), (states[16]+((constants[103]/constants[101])*constants[85]*algebraic[92]*algebraic[93])/(1.00000-algebraic[93]))/(1.00000+((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93])) , True, (states[16]+(constants[103]/constants[101])*constants[85])/(1.00000+constants[103]/constants[101])])
    algebraic[106] = ((1.00000/constants[152])*(numpy.power(algebraic[97], 2.00000)))/(numpy.power(algebraic[97], 2.00000)+numpy.power(constants[115], 2.00000))
    algebraic[112] = (algebraic[105]+constants[157])*((constants[167]+algebraic[106]+constants[157])*(constants[167]+algebraic[107])+algebraic[105]*(constants[167]+algebraic[106]))
    algebraic[113] = (algebraic[105]*constants[167]*(algebraic[105]+constants[157]+constants[167]+algebraic[107]))/algebraic[112]
    algebraic[115] = (algebraic[105]*(algebraic[106]*(algebraic[105]+constants[167]+algebraic[107])+algebraic[107]*constants[157]))/algebraic[112]
    algebraic[121] = algebraic[101]*algebraic[115]+algebraic[100]*algebraic[113]
    algebraic[123] = (algebraic[100]*algebraic[105])/(algebraic[105]+constants[157])
    algebraic[125] = ((states[19]*algebraic[121]+states[20]*algebraic[123])*constants[5])/constants[3]
    algebraic[127] = (-algebraic[125]*2.00000*constants[3]*constants[9])/constants[6]
    algebraic[82] = numpy.log10(constants[85]/states[16])/constants[88]
    algebraic[83] = (constants[89]*(states[0]-algebraic[82])*2.00000*constants[3]*constants[9])/constants[6]
    algebraic[81] = (((constants[86]*states[16])/(constants[87]+states[16]))*2.00000*constants[3]*constants[9])/constants[6]
    algebraic[108] = ((1.00000/constants[113])*(numpy.power(algebraic[97], 2.00000)+constants[116]*(numpy.power(constants[115], 2.00000))))/(numpy.power(algebraic[97], 2.00000)+numpy.power(constants[115], 2.00000))
    algebraic[109] = ((1.00000/constants[113])*(numpy.power(states[16], 2.00000)+constants[116]*(numpy.power(constants[115], 2.00000))))/(numpy.power(states[16], 2.00000)+numpy.power(constants[115], 2.00000))
    algebraic[116] = (constants[157]*constants[167]*(constants[157]+algebraic[105]+constants[167]+algebraic[106]))/algebraic[112]
    algebraic[118] = algebraic[113]*algebraic[108]+algebraic[116]*algebraic[109]
    algebraic[110] = ((constants[114]/constants[113])*constants[117]*(numpy.power(algebraic[97], 2.00000)+constants[116]*(numpy.power(constants[115], 2.00000))))/(constants[117]*(numpy.power(algebraic[97], 2.00000))+constants[116]*(numpy.power(constants[115], 2.00000)))
    algebraic[111] = ((constants[114]/constants[113])*constants[117]*(numpy.power(states[16], 2.00000)+constants[116]*(numpy.power(constants[115], 2.00000))))/(constants[117]*(numpy.power(states[16], 2.00000))+constants[116]*(numpy.power(constants[115], 2.00000)))
    algebraic[120] = (algebraic[105]*algebraic[110]+constants[157]*algebraic[111])/(algebraic[105]+constants[157])
    algebraic[96] = (states[16]+(constants[102]/constants[101])*states[17])/(1.00000+constants[102]/constants[101])
    algebraic[102] = ((((1.00000/constants[109])*algebraic[96])/constants[110])*(algebraic[94]+constants[107]))/(algebraic[94]+1.00000)
    algebraic[103] = ((((1.00000/constants[109])*states[16])/constants[110])*(algebraic[94]+constants[107]))/(algebraic[94]+1.00000)
    algebraic[114] = (constants[157]*(algebraic[107]*(constants[157]+constants[167]+algebraic[106])+algebraic[106]*algebraic[105]))/algebraic[112]
    algebraic[126] = algebraic[114]*algebraic[102]+algebraic[116]*algebraic[103]
    algebraic[104] = ((1.00000/constants[109])*constants[108]*(algebraic[94]+constants[107]))/(constants[108]*algebraic[94]+constants[107])
    algebraic[128] = algebraic[104]
    algebraic[90] = (constants[95]*(numpy.power(states[16], 2.00000)))/(numpy.power(constants[96], 2.00000)+numpy.power(states[16], 2.00000))
    algebraic[98] = (constants[102]*(states[17]-states[16]))/(1.00000+constants[102]/constants[101])
    algebraic[99] = custom_piecewise([numpy.greater(numpy.fabs(algebraic[92]) , 1.00000e-05), (constants[102]*((states[17]-states[16])+(((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93]))*(states[17]-constants[85]*algebraic[93])))/(1.00000+constants[102]/constants[101]+((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93])) , True, (constants[102]*((states[17]-states[16])+(((constants[103]/constants[101])*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))*(states[17]-constants[85]*numpy.exp(-1.00000e-05))))/(1.00000+constants[102]/constants[101]+((constants[103]/constants[101])*1.00000e-05)/(1.00000-numpy.exp(-1.00000e-05)))])
    algebraic[117] = algebraic[115]*algebraic[99]+algebraic[98]*algebraic[114]
    algebraic[119] = (algebraic[98]*algebraic[107])/(constants[167]+algebraic[107])
    algebraic[129] = ((states[19]*algebraic[117]+states[21]*algebraic[119])*constants[5])/constants[3]
    algebraic[131] = (-algebraic[129]+algebraic[90])-constants[99]*(states[17]-states[16])
    algebraic[130] = (constants[157]*algebraic[103])/(algebraic[105]+constants[157])
    algebraic[132] = algebraic[104]
    algebraic[133] = ((1.00000-states[19])-states[20])-states[21]
    algebraic[122] = (constants[167]*algebraic[109])/(constants[167]+algebraic[107])
    algebraic[124] = algebraic[111]
    algebraic[134] = (constants[122]*states[22])/constants[170]
    algebraic[135] = algebraic[134]*constants[159]
    algebraic[136] = states[23]+states[24]+states[25]
    algebraic[137] = custom_piecewise([numpy.less(algebraic[136] , 0.00000), (algebraic[135]*(constants[133]*algebraic[136]+1.00000))/(1.00000-algebraic[136]) , True, (algebraic[135]*(1.00000+(constants[133]+2.00000)*algebraic[136]))/(1.00000+algebraic[136])])
    algebraic[138] = custom_piecewise([numpy.greater(1.00000-algebraic[137]/(constants[120]*constants[122]) , 0.100000), constants[119]*(1.00000-algebraic[137]/(constants[120]*constants[122])) , True, constants[119]*0.100000])
    algebraic[139] = (constants[100]-states[18])*algebraic[138]-states[16]*states[18]*constants[118]
    algebraic[11] = states[16]
    algebraic[26] = (algebraic[24]*constants[6])/(constants[3]*constants[9])
    algebraic[28] = algebraic[27]+algebraic[22]
    algebraic[35] = (algebraic[33]*constants[6])/(constants[3]*constants[9])
    algebraic[43] = (algebraic[41]*3.00000*constants[6])/(constants[3]*constants[9])
    algebraic[44] = (algebraic[41]*-2.00000*constants[6])/(constants[3]*constants[9])
    algebraic[45] = (-(algebraic[27]+algebraic[31]+algebraic[29]+algebraic[30]+algebraic[32]+algebraic[34]+algebraic[41]*-2.00000+algebraic[38])*constants[6])/(constants[3]*constants[9])
    algebraic[78] = algebraic[51]/constants[3]
    algebraic[80] = algebraic[64]/constants[3]
    algebraic[88] = (-(algebraic[37]+algebraic[22]+algebraic[24]+algebraic[87]*3.00000+algebraic[41]*3.00000+algebraic[33])*constants[6])/(constants[3]*constants[9])
    algebraic[89] = (algebraic[87]*3.00000*constants[6])/(constants[3]*constants[9])
    algebraic[91] = algebraic[88]+algebraic[78]+algebraic[80]
    algebraic[95] = custom_piecewise([numpy.greater(numpy.fabs(algebraic[92]) , 1.00000e-09), (states[16]+(constants[102]/constants[101])*states[17]+((constants[103]/constants[101])*constants[85]*algebraic[92]*algebraic[93])/(1.00000-algebraic[93]))/(1.00000+constants[102]/constants[101]+((constants[103]/constants[101])*algebraic[92])/(1.00000-algebraic[93])) , True, (states[16]+(constants[102]/constants[101])*states[17]+(constants[103]/constants[101])*constants[85])/(1.00000+constants[102]/constants[101]+constants[103]/constants[101])])
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return numpy.select(cases[0::2],cases[1::2])

def solve_model(args,f_log):

    """Solve model with ODE solver"""
    from scipy.integrate import ode
    # Initialise constants and state variables
    (init_states, constants) = initConsts(args)

    # Set timespan to solve over
    if not args.fast:
        dt = 0.02
    else:
        dt = 0.1
    BCL = float(args.bcl)
    nbeats = float(args.nbeats)
    duration = nbeats*BCL

    f_states = open(os.path.join(args.simfolder,"states.dat"),'a')

    init_time = 0.0
    if args.inittime is not None:
        init_time = float(args.inittime)
    voi = numpy.arange(0.0,duration+dt,dt)
    voi += init_time

    dtout = float(args.dtout)
    dtout_int = dtout
    dt_int = dt
    while dt_int<1:
        dt_int *= 10
        dtout_int *= 10
    if math.fmod(dtout_int, dt_int)!=0:
        raise Exception("dtout is not a multiple of dt = "+str(dt))

    # Construct ODE object to solve
    r = ode(computeRates)
    r.set_integrator('vode', method='bdf', atol=1e-06, rtol=1e-06, max_step=1)
    r.set_initial_value(init_states, voi[0])
    r.set_f_params(constants)

    # Solve model
    states = numpy.array([[0.0] * len(voi)] * sizeStates)
    states[:,0] = init_states
    numpy.savetxt(os.path.join(args.simfolder,"states.dat"), 
                  [states[:,0]], 
                  newline="\n",
                  delimiter=' ',
                  fmt="%g")
    for (i,t) in enumerate(voi[1:]):
        # print("Time : "+str(t)+" / "+str(duration)+" ms")
        if r.successful():
            r.integrate(t)
            states[:,i+1] = r.y
        else:
            break   

        if math.fmod(t, dtout)==0:
            f_log.write("Time : "+str(t)+" / "+str(duration+init_time)+" ms\n")
            numpy.savetxt(f_states, 
                          [states[:,i+1]], 
                          fmt="%g",
                          delimiter=' ',
                          newline="\n")

    condition = numpy.mod(voi, dtout)==0
    voi_coarse = numpy.extract(condition, voi)
    numpy.savetxt(os.path.join(args.simfolder,"time.dat"),voi_coarse,fmt="%.2f")

    f_states.close()
    states_saved = numpy.loadtxt(os.path.join(args.simfolder,"states.dat"),dtype=float)
    states_saved = numpy.transpose(states_saved)
    numpy.savetxt(os.path.join(args.simfolder,"states.dat"),states_saved,fmt="%g")

    # Compute algebraic variables
    algebraic = computeAlgebraic(constants, states_saved, voi_coarse)
    numpy.savetxt(os.path.join(args.simfolder,"algebraic.dat"),algebraic,fmt="%g")

    return (voi, states, algebraic)

def plot_model(voi, states, algebraic, figname, f_log):
    """Plot variables against variable of integration"""
    import matplotlib.pyplot as plt

    legend = []
    na_i = states[1,:]*1e03 # intracellular sodium

    ca_i = states[16,:]*1e03 # intracellular calcium

    tension = algebraic[137,:]

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
    if figname is not None:
        # print("Saving figure "+figname+"...")
        f_log.write("Saving figure "+figname+"...\n")
        plt.savefig(figname,dpi=300)
    else:
        plt.show()

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

    parser.add_argument('--iNa_b_scale_factor', type=str, default="0.0", required=False,
                        help='Scales algebraic 37 Na background current (simulating increased late Na current)')

    parser.add_argument('--iK_b_scale_factor', type=str, default="0.0", required=False,
                        help='Scales algebraic 38 K background current')

    parser.add_argument('--H_constant', type=str, default="0.0", required=False,
                        help='Introduce a constant current across the cell membrane. added to algebraic[76] I_H')

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

    f_log = open(os.path.join(args.simfolder,"model.log"),"a")

    with open(os.path.join(args.simfolder,'parameters.json'), 'wt') as f:
        json.dump(vars(args), f, indent=4)

    if run:
        # print("Running model and saving to "+args.simfolder+"...")
        f_log.write("Running model and saving to "+args.simfolder+"...\n")

        voi, states, algebraic = solve_model(args,f_log)
        # numpy.savetxt(os.path.join(args.simfolder,"time.dat"),voi,fmt="%g")
        # numpy.savetxt(os.path.join(args.simfolder,"states.dat"),states,fmt="%g")
        # numpy.savetxt(os.path.join(args.simfolder,"algebraic.dat"),algebraic,fmt="%g")
        init_state = states[:,-1]
        numpy.savetxt(os.path.join(args.simfolder,"init_state.dat"),init_state,fmt="%g")

    else:
        # print("You chose not to overwrite. Not running.")
        f_log.write("You chose not to overwrite. Not running.\n")

    if args.compute_algebraic:
        # print("Computing algebraic...")
        f_log.write("Computing algebraic...\n")
        if not os.path.exists(args.simfolder):
            raise Exception("You have to solve the model first")
        if args.coarse:
            if not os.path.exists(os.path.join(args.simfolder,"time_coarse.dat")) or not os.path.exists(os.path.join(args.simfolder,"states_coarse.dat")):
                raise Exception("Cannot find time_coarse.dat and states_coarse.dat in "+args.simfolder)
            else:
                f_log.write("Using coarse output...\n")
                voi = numpy.loadtxt(os.path.join(args.simfolder,"time_coarse.dat"),dtype=float)
                states = numpy.loadtxt(os.path.join(args.simfolder,"states_coarse.dat"),dtype=float)

        else:
            if not os.path.exists(os.path.join(args.simfolder,"time.dat")) or not os.path.exists(os.path.join(args.simfolder,"states.dat")):
                raise Exception("Cannot find time.dat and states.dat in "+args.simfolder)
            else:
                print("Using fine output...")
                voi = numpy.loadtxt(os.path.join(args.simfolder,"time.dat"),dtype=float)
                states = numpy.loadtxt(os.path.join(args.simfolder,"states.dat"),dtype=float)

        (init_states, constants) = initConsts(args)
        algebraic = computeAlgebraic(constants, states, voi)
        if args.coarse:
            numpy.savetxt(os.path.join(args.simfolder,"algebraic_coarse.dat"),algebraic,fmt="%g")
        else:
            numpy.savetxt(os.path.join(args.simfolder,"algebraic.dat"),algebraic,fmt="%g")

    if args.visualise:

        # print("Plotting results...")
        f_log.write("Plotting results...\n")

        voi = numpy.loadtxt(os.path.join(args.simfolder,"time.dat"),dtype=float)
        states = numpy.loadtxt(os.path.join(args.simfolder,"states.dat"),dtype=float)
        algebraic = numpy.loadtxt(os.path.join(args.simfolder,"algebraic.dat"),dtype=float)

        plot_model(voi, states, algebraic, args.figname, f_log)

    f_log.close()