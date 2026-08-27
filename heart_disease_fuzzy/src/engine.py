import skfuzzy as fuzz
from src.membership import get_membership_functions
from src.rules import evaluate_rules
from config.settings import RISK_RANGE

def diagnose_heart_disease(chest_pain, cholesterol):
    """Runs full fuzzification, inference, and centroid defuzzification."""
    mfs = get_membership_functions()
    
    # Aggregate active rules
    aggregated_outputs = evaluate_rules(chest_pain, cholesterol, mfs, RISK_RANGE)
    
    # Defuzzification using Centroid Method
    try:
        calculated_risk = fuzz.defuzz(RISK_RANGE, aggregated_outputs, 'centroid')
    except AssertionError:
        # Default fallback if no rules fire
        calculated_risk = 0.0
        
    return calculated_risk
