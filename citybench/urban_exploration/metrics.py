import os
import pandas as pd
from config import RESULTS_PATH

parent_folder = os.path.join(RESULTS_PATH, "exploration_results")
output_file = os.path.join(parent_folder, "exploration_benchmark_result.csv")

all_data = []
if not os.path.exists(parent_folder): os.makedirs(parent_folder)
for file_name in os.listdir(parent_folder):
    file_path = os.path.join(parent_folder, file_name)
    if os.path.isfile(file_path) and file_name.endswith('.csv'):
        try:
            df = pd.read_csv(file_path)
            all_data.append(df)  
        except Exception as e:
            print(f"Error {file_path} : {e}")  

if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv(output_file, index=False)
    print("Exploration results have been saved!")
else:
    print("No exploration results found!")
