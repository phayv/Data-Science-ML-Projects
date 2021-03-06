import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')



class K_Means:
    def __init__(self, n_clusters = 2, tol = .001, max_iterations = 300):
        self.n_clusters = n_clusters
        self.tol = .001
        self.max_iterations = max_iterations

    def fit(self, data):
        self.centroids = {}

        for i in range(self.n_clusters):
            #initial centers
            self.centroids[i] = data[i]

        for i in range(self.max_iterations):
            # make empty list for classifications for number of clusters
            self.classifications = {}
            for i in range(self.n_clusters):
                self.classifications[i] = []
            
            for row_of_features in data:
                #sets can change classification as max_iterations changes
                distances = [np.linalg.norm(row_of_features - self.centroids[centroid]) \
                                            for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(row_of_features)

            #dict makes prev not change as self.centroid changes    
            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification],axis = 0)
            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                # If moving more than self.tol, then it will
                if np.sum((current_centroid - original_centroid)/original_centroid*100.0) > self.tol:
                    optimized = False

            if optimized:
                break
    
    def predict(self,data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) \
                                            for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification
