### LOAD LIBRARIES ###

# Data wrangling & processing: 
import numpy as np
import pandas as pd
import sys
import datetime


# Read in the data as a Pandas DataFrame:
df = pd.read_json('./historical.json').reset_index()


# Correct column names:
df.columns = ['date', 'gold', 'silver']


# Correct data types, 'if' needed:
if df.date.dtype != 'datetime64[ns]':
    df.date = df.date.astype('datetime64[ns]')
if df.gold.dtype != 'float64':
    df.gold = df.gold.str.replace(',', '').astype('float')
if df.silver.dtype != 'float64':
    df.silver = df.silver.str.replace(',', '').astype('float')

    
# Check if the user specified arguments:
args = len(sys.argv) - 1

# Define start date:
if args == 3:
    # Use provided start date:
    print('Valid start dates are between %s and %s.' 
        %(df.date.min().strftime('%Y-%m-%d'), 
        df.date.max().strftime('%Y-%m-%d')))
    start = sys.argv[1]
else:    
    # Collect a start date:
    start = input('Please give a start date between %s and %s:\n> ' 
        %(df.date.min().strftime('%Y-%m-%d'), 
        df.date.max().strftime('%Y-%m-%d')))

        
# Validate that the start date is in range:
def validate_start(start):
    try:
        datetime.datetime.strptime(start, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD.")
    if start in pd.date_range(df.date.min().strftime('%Y-%m-%d'), 
        df.date.max().strftime('%Y-%m-%d')):
        print('Start date:  ', start, '\n')
    else:             
        print('\nPlease provide a date within the specified range.')
        start = input('> ')
        validate_start(start)    
    return start
    
    
# Record validated start date:
start = validate_start(start)


# Define end date:
if args == 3:
    # Use provided end date:
    print('Valid end dates are between %s and %s.' 
        %(start, df.date.max().strftime('%Y-%m-%d')))
    end = sys.argv[2]
else:    
    # Collect an end date:     
    end = input('Please give a end date between %s and %s:\n> ' 
    %(start, df.date.max().strftime('%Y-%m-%d')))

    
# Validate that the end date is in range:
def validate_end(end):
    try:
        datetime.datetime.strptime(end, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD.")
    if end in pd.date_range(start, df.date.max().strftime('%Y-%m-%d')):
        print('End date:    ', end, '\n')
    else:
        print('\nPlease provide a date within the specified range.')
        end = input('> ')
        validate_end(end)
    return end

    
# Record validated end date:
end = validate_end(end)


# Define commodity:
if args == 3:
    # Use provided commodity:
    print('Valid commodities are either %s or %s.' 
        %(df.columns[1], df.columns[2]))
    commodity = sys.argv[3]
else:    
    # Collect a commodity:
    commodity = input('Please give a commodity, either %s or %s:\n> ' 
    %(df.columns[1], df.columns[2]))

    
# Verify that the commodity is valid:
def validate_commodity(commodity):
    if (commodity == df.columns[1]) | (commodity == df.columns[2]):
        print('Commodity:   ', commodity, '\n')
    else:
        print("\nPlease provide a correct input, should be 'gold' or 'silver'.")
        commodity = input('> ')
        validate_commodity(commodity)
    return commodity  
 

# Record validated commodity: 
commodity = validate_commodity(commodity)


# Calculate the commodity's price mean & variance over the date range:
date_range = pd.date_range(start, end)
df_range = df[df.loc[:, 'date'].isin(date_range)]
mean_price = '{:.2f}'.format(np.mean(
    df_range.loc[:, commodity].dropna()))
price_var = '{:.2f}'.format(np.var(
    df_range.loc[:, commodity].dropna()))

    
# Print the results as a tuple:
print('Out[]: ', commodity, mean_price, price_var)