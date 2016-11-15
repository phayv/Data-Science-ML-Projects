import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

from sklearn.cluster import KMeans
from sklearn import preprocessing, cross_validation

df = pd.read_excel('data/titanic.xls',header=0)

#############################################################PIPELINE - START
#useless data
df.drop(['body','name'],axis = 1,inplace = True)

df.convert_objects(convert_numeric = True)
#pd.to_numeric(df[])
df.fillna(0,inplace = True)

def fix_non_numeric_data(df):
    columns = df.columns.values

    for column in columns:
        #dictionary to hold unique values for each unique column value.
        text_digit_vals = {}

        #if type is not numeric...
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)

            #creating unique values for dict index
            count = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = count
                    count += 1
            df[column] = list(map(lambda val: text_digit_vals[val], df[column]))
    return df

df = fix_non_numeric_data(df)
df.drop(['boat','ticket'],axis = 1,inplace = True)
X = np.array(df.drop(['survived'], axis = 1).astype(float))
X = preprocessing.scale(X)   
y = np.array(df['survived'])

KM = KMeans(n_clusters = 2)
KM.fit(X)

correct = 0
for i in range(len(X)):
    predict_survived = np.array(X[i].astype(float))
    predict_survived = predict_survived.reshape(-1,len(predict_survived))
    prediction = KM.predict(predict_survived)
    if prediction[0] == y[i]:
        correct += 1

print(float(correct)/float(len(X)))
#############################################################PIPELINE - END
