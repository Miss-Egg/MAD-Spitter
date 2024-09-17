# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 04:09:47 2023

@author: Dr.Frost

Save this program into the same directory as the file you want to MAD on.
Note to use a csv file and that it has to be the only csv file in it.

It will find the median aboslute deviation of each valid header.
Valid header = nothing with "subj", "subjectid", "subject", "trials" in it.

Asks user to input the desired MAD multiplier. 3 is the default if user just presses "ENTER" on the keyboard

2 Output files into a created folder
1: valid values
2: MAD info

"""
import os
import pandas as pd
import numpy as np
from datetime import datetime

# Function to calculate MAD
def calculate_mad(data):
    median = np.median(data)
    absolute_diff = np.abs(data - median)
    mad = np.median(absolute_diff)
    return mad

# Function to filter and save valid values
def filter_and_save_values(input_file, output_folder, mad_multiplier):
    df = pd.read_csv(input_file)

    # Filter out headers containing "trials" in their names and "subject," "subj," or "subjectid"
    excluded_keywords = ["trials", "subject", "subj", "subjectid"]
    valid_headers = [col for col in df.columns if not any(keyword in col.lower() for keyword in excluded_keywords)]

    all_filtered_data = pd.DataFrame()
    info_data = []

    for header in valid_headers:
        data = df[header].apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()
        if data.empty:
            continue

        mad = calculate_mad(data)
        new_header = f"{header}_times{mad_multiplier:.0f}"

        lower_bound = mad_multiplier * mad
        upper_bound = mad_multiplier * mad

        filtered_data = df[(df[header] >= data.median() - lower_bound) & (df[header] <= data.median() + upper_bound)]
        all_filtered_data[new_header] = filtered_data[header]
        info_data.extend([new_header, mad, mad - lower_bound, mad + upper_bound])

    # Construct the output file paths with date and time
    output_ed_file = os.path.join(output_folder, f"MAD-ed-{datetime.now().strftime('%Y%m%d-%H%M%S')}.csv")
    output_info_file = os.path.join(output_folder, f"MAD-info-{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt")

    all_filtered_data.to_csv(output_ed_file, index=False)
    with open(output_info_file, 'w') as info_file:
        info_file.write('\n'.join(map(str, info_data)))

# Get a list of CSV files in the current directory
csv_files = [file for file in os.listdir() if file.endswith('.csv')]

if len(csv_files) == 0:
    print("No CSV files found in the current directory.")
else:
    if len(csv_files) > 1:
        print("Multiple CSV files found in the current directory.")
        print("Please move the desired CSV file and this script into its own folder.")
    else:
        input_file = csv_files[0]

        # Create the output folder with date and time
        output_folder = os.path.join("MAD-ed", datetime.now().strftime('%Y%m%d-%H%M%S'))
        os.makedirs(output_folder, exist_ok=True)

        # Default MAD multiplier
        mad_multiplier = input("Enter the MAD multiplier (default is 3): ")
        if mad_multiplier == '':
            mad_multiplier = 3
        else:
            mad_multiplier = int(mad_multiplier)

        # Process and filter data for valid headers
        filter_and_save_values(input_file, output_folder, mad_multiplier)

        print(f"Filtered data saved in folder {output_folder}")