### LOAD LIBRARIES ###

# Data wrangling & processing: 
import numpy as np
import pandas as pd

# Statistical testing:
from statsmodels.tsa.stattools import adfuller

# Machine learning:
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



## PREPARE DATA FOR ANALYSES ###

# Read & print the data as a Pandas DataFrame:
ts = pd.read_json('./historical.json').rename_axis('date').sort_index()

# Correct data types, 'if' needed:
if ts.gold.dtype != 'float64':
    ts.gold = ts.gold.str.replace(',', '').astype('float')
if ts.silver.dtype != 'float64':
    ts.silver = ts.silver.str.replace(',', '').astype('float')

    
    
### RUN A STATIONALITY TEST ###

# Dickey-Fuller test:
def dft(timeseries):
    #Determining the rolling mean:
    rolmean = timeseries.rolling(center=False, window=3).mean()
    
    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=[
        'Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'% key] = value
    print(dfoutput)

    
# Print the test results:
print('GOLD STATIONARITY TEST:')
dft(ts.gold.dropna())
print('--------------------------------')

print('\nSILVER STATIONARITY TEST:')
dft(ts.silver.dropna())
print('--------------------------------\n')



### SPLIT THE DATA INTO TRAINING & TESTING SETS ###

# Create a column to predict upon; predict the next day's price:
ts['gold_y'] = ts.gold.shift(-1)
ts['silver_y'] = ts.silver.shift(-1)

# Split the data into 80% training & 20% testing sets:
train = ts.iloc[:int(ts.shape[0] * 0.8), ]
test = ts[~ts.index.isin(train.index)]


### LINEAR REGRESSION MODELING ###


# Separate the training & test data from the other commodity:
t = train[['gold', 'gold_y']].dropna()
te = test[['gold', 'gold_y']].dropna().append(test[['gold', 'gold_y']].iloc[-1, :])


# Define training input & output arrays:
X = t.iloc[:, 0].values.reshape(-1, 1)
y = t.iloc[:, 1]


# Define testing input & output arrays:
x_test = te.iloc[:, 0].values.reshape(-1, 1)
y_test = te.iloc[:, 1]


# Create empty lists to hold model data:
y_pred = []
y_true = []


# Define model type:
model = LinearRegression(normalize=True)


## WALK FORWARD METHOD:
# Walk through the testing data points, predicting 
# only one day ahead at a time:
for i in range(test.shape[0]):

    
    # Fit the model on training data:
    model.fit(X, y)
    
    
    # Run the first prediction off of the last known data point:
    if i == 0:
        training_predicts = model.predict(X)
        y_pred.append(model.predict(X[-1][0]))
        y_true.append(x_test[i])
    
    
    # Run the other predictions off of the subsequent points:
    else:
        y_pred.append(model.predict(x_test[i][0]))
        y_true.append(x_test[i])
    
    
    # Update the training set with the new, 'known' point:
    X = np.append(X, te.iloc[i, 0]).reshape(-1, 1)
    y = np.append(y, te.iloc[i, 1])
        

# Calculate the mean squared error and R^2 values:
MSE = mean_squared_error(y_pred, y_true)
R2 = model.score(y_pred, y_true)


# Print model scores:
print('\nGOLD Predictive model results:')
print('Mean Squared Error: %.3f' % MSE)
print('R-square value:     %.3f' % R2)


# Make some arbitrary cut-off points for MSE & R^2, print results:
if (MSE < 3) & (R2 > 0.8):
    print('\nOne-day-ahead prediction *is* possible!')
else:
    print('\nOne-day-ahead prediction is *not* reliable!')
    


### CHECK IF AN INCREASE OR DECREASE IS PREDICTABLE ###

commodity = 'gold'
if model.predict(test[commodity][-1]) > test[commodity][-1]:
    print("Tomorrow's prediction is an *increase*.")
else:
    print("Tomorrow's prediction is a *decrease*.\n\n")
print('--------------------------------')
    

    
### LINEAR REGRESSION MODELING ###


# Separate the training & test data from the other commodity:
t = train[['silver', 'silver_y']].dropna()
te = test[['silver', 'silver_y']].dropna().append(test[['silver', 'silver_y']].iloc[-1, :])


# Define training input & output arrays:
X = t.iloc[:, 0].values.reshape(-1, 1)
y = t.iloc[:, 1]


# Define testing input & output arrays:
x_test = te.iloc[:, 0].values.reshape(-1, 1)
y_test = te.iloc[:, 1]


# Create empty lists to hold model data:
y_pred = []
y_true = []


# Define model type:
model = LinearRegression(normalize=True)


## WALK FORWARD METHOD:
# Walk through the testing data points, predicting 
# only one day ahead at a time:
for i in range(test.shape[0]):

    
    # Fit the model on training data:
    model.fit(X, y)
    
    
    # Run the first prediction off of the last known data point:
    if i == 0:
        training_predicts = model.predict(X)
        y_pred.append(model.predict(X[-1][0]))
        y_true.append(x_test[i])
    
    
    # Run the other predictions off of the subsequent points:
    else:
        y_pred.append(model.predict(x_test[i][0]))
        y_true.append(x_test[i])
    
    
    # Update the training set with the new, 'known' point:
    X = np.append(X, te.iloc[i, 0]).reshape(-1, 1)
    y = np.append(y, te.iloc[i, 1])
        

# Calculate the mean squared error and R^2 values:
MSE = mean_squared_error(y_pred, y_true)
R2 = model.score(y_pred, y_true)


# Print model scores:
print('\nSILVER Predictive model results:')
print('Mean Squared Error: %.3f' % MSE)
print('R-square value:     %.3f' % R2)


# Make some arbitrary cut-off points for MSE & R^2, print results:
if (MSE < 3) & (R2 > 0.8):
    print('\nOne-day-ahead prediction *is* possible!')
else:
    print('\nOne-day-ahead prediction is *not* reliable!')


### CHECK IF AN INCREASE OR DECREASE IS PREDICTABLE ###

commodity = 'silver'
if model.predict(test[commodity][-1]) > test[commodity][-1]:
    print("Tomorrow's prediction is an *increase*.")
else:
    print("Tomorrow's prediction is a *decrease*.\n\n")
