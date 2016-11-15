import pandas as pd
import quandl, math, datetime

import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

df = quandl.get('WIKI/GOOGL')

#--------------------------------------PIPELINE - START
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/ df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Close']-df['Adj. Open'])/ df['Adj. Open'] * 100.0
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace = True)

forecast_out = int(math.ceil(0.0034*len(df)))
print forecast_out

df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'],axis=1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]


df.dropna(inplace = True)
y = np.array(df['label'])

X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size = 0.2)

LR = LinearRegression()
LR.fit(X_train,y_train)
accuracy = LR.score(X_test,y_test)

print "-------------------------------------------------------------------------------------"

forecast_set = LR.predict(X_lately)
print forecast_set,accuracy,forecast_out

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] =[np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc = 'upper right')
plt.ylabel('Price')
plt.xlabel('Date')
plt.show()
#--------------------------------------PIPELINE - END