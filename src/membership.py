import skfuzzy as fuzz
from config.settings import CHEST_PAIN_RANGE, CHOLESTEROL_RANGE, RISK_RANGE

def get_membership_functions():
    mfs = {}
    mfs['cp_low'] = fuzz.trimf(CHEST_PAIN_RANGE, [0, 0, 5])
    mfs['cp_medium'] = fuzz.trimf(CHEST_PAIN_RANGE, [2, 5, 8])
    mfs['cp_high'] = fuzz.trimf(CHEST_PAIN_RANGE, [5, 10, 10])

    mfs['chol_normal'] = fuzz.trimf(CHOLESTEROL_RANGE, [100, 150, 220])
    mfs['chol_borderline'] = fuzz.trimf(CHOLESTEROL_RANGE, [200, 240, 280])
    mfs['chol_high'] = fuzz.trapmf(CHOLESTEROL_RANGE, [260, 300, 400, 400])

    mfs['risk_low'] = fuzz.trimf(RISK_RANGE, [0, 0, 45])
    mfs['risk_medium'] = fuzz.trimf(RISK_RANGE, [30, 50, 70])
    mfs['risk_high'] = fuzz.trimf(RISK_RANGE, [55, 100, 100])
    return mfs
