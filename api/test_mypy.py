"""Script de test pour MyPy contournant le problème de nom de package"""

import subprocess
import sys
import os

def run_mypy():
    """Exécute mypy avec les bonnes options"""
    os.chdir("api")
    
    # Test simple sur un fichier à la fois
    files_to_check = [
        "app/main.py",
        "app/models.py", 
        "app/predictor.py",
        "app/routes.py"
    ]
    
    for file_path in files_to_check:
        cmd = [
            "uv", "run", "mypy",
            "--ignore-missing-imports",
            "--no-strict-optional",
            "--config-file", "setup.cfg",
            file_path
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f" {file_path}: OK")
        except subprocess.CalledProcessError as e:
            print(f" {file_path}: FAILED")
            print(e.stdout)
            if e.stderr:
                print(f"STDERR: {e.stderr}")
            return e.returncode
    
    print(" All MyPy checks passed!")
    return 0

if __name__ == "__main__":
    sys.exit(run_mypy())
