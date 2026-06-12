
#master script that runs the entire ETL and analytics pipeline end to end.
#run this from the project root: python scripts/run_pipeline.py


import subprocess
import sys
from pathlib import Path


BASE = Path(__file__).parent

scripts = [
    ("Data Ingestion",    BASE / "data_ingestion.py"),
    ("Data Cleaning",     BASE / "data_cleaning.py"),
    ("Database Loading",  BASE / "load_database.py"),
]

print("=" * 60)
print("  BLUESTOCK MF CAPSTONE — FULL PIPELINE RUN")
print("=" * 60)

all_passed = True

for step_name, script_path in scripts:
    print(f"\nRunning: {step_name}...")
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f" {step_name} completed successfully")
    else:
        print(f" {step_name} FAILED")
        print(result.stderr[-500:])
        all_passed = False

print("\n" + "=" * 60)
if all_passed:
    print("Full pipeline completed successfully!")
    print("  Next: Open notebooks/ for EDA and analytics.")
    print("  Next: Open dashboard/ for Power BI file.")
else:
    print(" Some steps failed. Check errors above.")
print("=" * 60)