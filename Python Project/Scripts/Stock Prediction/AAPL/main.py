import pandas as pd
import quandl, math

import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/AAPL')
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/ df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Close']-df['Adj. Open'])/ df['Adj. Open'] * 100.0
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace = True)

forecast_out = int(math.ceil(0.0034*len(df)))
print forecast_out

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace = True)

X = np.array(df.drop(['label'],axis=1))
y = np.array(df['label'])
X = preprocessing.scale(X)

X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size = 0.2)

LR = LinearRegression()
LR.fit(X_train,y_train)
accuracy = LR.score(X_test,y_test)

print "LinearRegression"
print "Accuracy: ",accuracy
print 'y = {}x_adjcl + {}x_hlpct + {}x_pctch + {}x_adjvol + {}'.format(\
    LR.coef_[0],LR.coef_[1],LR.coef_[2],LR.coef_[3],LR.intercept_)
print "---------------------------------------------------------------\n"
clf = svm.SVR()
clf.fit(X_train,y_train)
accuracy2 = clf.score(X_test,y_test)
print "SVM"
print "Accuracy: ",accuracy2
print clf.support_vectors_
