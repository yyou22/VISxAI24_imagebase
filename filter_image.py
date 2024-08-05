import os
import shutil
import pandas as pd

# Read the CSV file
df = pd.read_csv('lvl4.csv')

# Create the new folder if it doesn't exist
if not os.path.exists('img_data_'):
    os.makedirs('img_data_')

# Iterate through the rows of the dataframe
for index, row in df.iterrows():
    ogi = row['ogi']
    vis = row['vis']

    # Convert ogi to integer
    ogi_int = int(ogi)

    # Check if vis column is 1
    if vis == 1:
        source_folder = os.path.join('img_data', str(ogi_int))
        destination_folder = os.path.join('img_data_', str(ogi_int))

        # Copy the folder if it exists
        if os.path.exists(source_folder):
            shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)
            print(f'Copied {source_folder} to {destination_folder}')
        else:
            print(f'Source folder {source_folder} does not exist.')

print('Completed copying folders.')
