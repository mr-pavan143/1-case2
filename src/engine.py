import skfuzzy as fuzz
from src.membership import get_membership_functions
from src.rules import evaluate_rules
from config.settings import RISK_RANGE

def diagnose_heart_disease(chest_pain, cholesterol):
    mfs = get_membership_functions()
    aggregated_outputs = evaluate_rules(chest_pain, cholesterol, mfs, RISK_RANGE)
    try:
        calculated_risk = fuzz.defuzz(RISK_RANGE, aggregated_outputs, 'centroid')
    except AssertionError:
        calculated_risk = 0.0
    return calculated_risk
