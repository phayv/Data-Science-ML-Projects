from scipy.spatial import distance

def euc_dist(a,b)
    """a: point from training data, b: point from testing data"""
    return distance.euclidean(a,b)

class Self_KNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
    predictions = []
    for row in X_test:
        label = self.closest(row)
        predictions.append(label)
    return predictions

    def closest(self,row):
        best_dist = euc_dist(row, self.X_train[0])
        best_indx = 0
        for i in range(1,len(self.X_train)):
            dist = euc(row, slef.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train