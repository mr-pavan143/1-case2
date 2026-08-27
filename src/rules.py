import numpy as np
import skfuzzy as fuzz
from config.settings import CHEST_PAIN_RANGE, CHOLESTEROL_RANGE

def evaluate_rules(cp_level, chol_level, mfs, risk_range):
    cp_fuzz_low = fuzz.interp_membership(CHEST_PAIN_RANGE, mfs['cp_low'], cp_level)
    cp_fuzz_med = fuzz.interp_membership(CHEST_PAIN_RANGE, mfs['cp_medium'], cp_level)
    cp_fuzz_high = fuzz.interp_membership(CHEST_PAIN_RANGE, mfs['cp_high'], cp_level)

    chol_fuzz_norm = fuzz.interp_membership(CHOLESTEROL_RANGE, mfs['chol_normal'], chol_level)
    chol_fuzz_bord = fuzz.interp_membership(CHOLESTEROL_RANGE, mfs['chol_borderline'], chol_level)
    chol_fuzz_high = fuzz.interp_membership(CHOLESTEROL_RANGE, mfs['chol_high'], chol_level)

    rule1_activation = np.fmin(cp_fuzz_low, chol_fuzz_norm)
    risk_activation_low = np.fmin(rule1_activation, mfs['risk_low'])

    rule2_activation = np.fmax(cp_fuzz_med, chol_fuzz_bord)
    risk_activation_med = np.fmin(rule2_activation, mfs['risk_medium'])

    rule3_activation = np.fmax(cp_fuzz_high, chol_fuzz_high)
    risk_activation_high = np.fmin(rule3_activation, mfs['risk_high'])

    aggregated = np.fmax(risk_activation_low, np.fmax(risk_activation_med, risk_activation_high))
    return aggregated
