# DAY 16: FIRST LOCAL SCRIPT
import pandas as pd
import numpy as np

print("--- SYSTEM CHECK ---")
print("General Nesredin, VS Code is Ready!")

# Create a simple DataFrame
data = {
    'Tool': ['VS Code', 'Pandas', 'Linux'],
    'Status': ['Installed', 'Active', 'Running']
}

df = pd.DataFrame(data)

print("\n--- MY ARSENAL ---")
print(df)

print("\n>>> MISSION SUCCESSFUL.")