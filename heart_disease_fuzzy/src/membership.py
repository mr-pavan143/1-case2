import skfuzzy as fuzz
from config.settings import CHEST_PAIN_RANGE, CHOLESTEROL_RANGE, RISK_RANGE

def get_membership_functions():
    """Defines linguistic variables and their fuzzy sets."""
    mfs = {}

    # Chest Pain Membership Functions (Type: Typical/Angina)
    mfs['cp_low'] = fuzz.trimf(CHEST_PAIN_RANGE, [0, 0, 4])
    mfs['cp_medium'] = fuzz.trimf(CHEST_PAIN_RANGE, [2, 5, 8])
    mfs['cp_high'] = fuzz.trimf(CHEST_PAIN_RANGE, [6, 10, 10])

    # Cholesterol Membership Functions
    mfs['chol_normal'] = fuzz.trimf(CHOLESTEROL_RANGE, [100, 100, 200])
    mfs['chol_borderline'] = fuzz.trimf(CHOLESTEROL_RANGE, [180, 220, 260])
    mfs['chol_high'] = fuzz.trapmf(CHOLESTEROL_RANGE, [240, 300, 400, 400])

    # Target: Heart Disease Risk Membership Functions
    mfs['risk_low'] = fuzz.trimf(RISK_RANGE, [0, 0, 45])
    mfs['risk_medium'] = fuzz.trimf(RISK_RANGE, [30, 50, 70])
    mfs['risk_high'] = fuzz.trimf(RISK_RANGE, [55, 100, 100])

    return mfs
