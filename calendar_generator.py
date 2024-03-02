# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:43:27 2024

@author: funky
"""

import pandas as pd

days = ('Sunday Monday Tuesday Wednesday Thursday Friday Saturday').split()
dates = list(range(1, 32))
months = ('January February March April May June July August September October November December').split()
filepath = r'C:\Users\funky\OneDrive\Desktop\Python\Calendar Generator\GrowCaldendar.xlsx'


# Create an empty DataFrame
df = pd.DataFrame()
x = 4#what ever day you want to start on. 0 would start on sunday, 1 starts on monday and so on.

# Iterate over the dates
for date in dates:
    # Calculate the day of the week index for the current date
    day_index = (date + x) % 7  # Start from Thursday (index 4) and wrap around

    # Create a new column name for the current date
    column_name = f'{days[day_index]}_{date}'

    # Add the column to the DataFrame
    df[column_name] = ''

# Save the DataFrame to Excel
df.to_excel(filepath, index=False)
print('excel created')