import os
import sys

# Forces python to search inside the current directory for packages
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.engine import diagnose_heart_disease

def run_simulation():
    print("=" * 50)
    print("SOFT COMPUTING DIAGNOSTIC SYSTEM: HEART DISEASE")
    print("=" * 50)
    
    sample_chest_pain = 4.0
    sample_cholesterol = 215.0
    
    risk_score = diagnose_heart_disease(sample_chest_pain, sample_cholesterol)
    
    print(f"Patient Inputs:")
    print(f"  - Chest Pain Intensity: {sample_chest_pain}/10")
    print(f"  - Cholesterol Level   : {sample_cholesterol} mg/dL\n")
    print(f"Diagnostic Output:")
    print(f"  - Calculated Risk of Heart Disease: {risk_score:.2f}%")
    print("=" * 50)

if __name__ == '__main__':
    run_simulation()
