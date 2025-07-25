import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from time import time

class Kmeans():
    """
    Kmeans clustering model.
    
    Kmeans fits a clustering model with k clusters.

    Parameters
    -----------
    k:int,
        Number of clusters 
    max_iter:int, 
        Maximum number of iterations 
    epsilon:float,
        Precision needed for termination (with iterations in [0,max_iter[)    
    """


    def __init__(
        self,
        k:int, 
        max_iter:int, 
        epsilon:float
    ):
        self.k = k
        self.max_iter = max_iter
        self.epsilon = epsilon
        self.centroids = None # list of centroid
        self._fit_time = None
        self._predict_time = None

    def pick_distinct(self,X):
        """
        Returns self.k random and distinct rows in X.
        Use case : Initialize centroids in fit method.
        
        Parameters
        -----------
        X:np.array,
            data     
        
        Returns
        -----------
        list of self.k rows of X
        """
        
        indices = np.random.randint(low = 0,high = len(X), size = self.k)
        return([X[i] for i in indices])

    def partition(self,X):
        """
        Returns the clusters in data X with centroids self.centroids.
        
        Parameters
        -----------
        X:np.array,
            data     
        
        Returns
        -----------
        np.array of shape(self.k, X.shape[1])
        """

        clusters = np.zeros(shape=len(X))
        for (i,e) in enumerate(X):
            nearest_cluster = None
            min_distance = 1e14
            for (j,c) in enumerate(self.centroids):
                distance = np.sqrt(sum((e - c)**2))
                if distance < min_distance:
                    min_distance = distance
                    nearest_cluster = j
            clusters[i]=nearest_cluster
        return(clusters)
    
    def cluster_mean(self,cluster,X):
        """
        Returns the mean of each clusters in data X.
        Warning : Crash with empty cluster (We think)
        
        Parameters
        -----------
        cluster: np.array,
            Precondition : cluster.shape = len(X)
            For each index i of X, cluster[i] is the number of the cluster of X[i].
        X:np.array,
            data     
        
        Returns
        -----------
        np.array of shape(self.k, X.shape[1])
        """
        means_of_cluster = np.zeros(shape=(self.k,X.shape[1]))
        for i in range(len(self.centroids)):
            means_of_cluster[i]=np.mean(X[cluster==i], axis=0)
        return means_of_cluster

    def max_distance_centroids_clusterMeans(self,clusterMeans):
        """
        Returns the maximum euclydian distance between a centroid 
        (in self.centroids) and its mean.
        
        Parameters
        -----------
        clusterMeans: np.array,
            Precondition : clusterMeans.shape == self.centroids.shape
            Generated by self.cluster_mean().
        
        Returns
        -----------
        np.float
        """
        max_distance = -1e14
        for (j,c) in enumerate(self.centroids):
            distance = np.sqrt(sum((c-clusterMeans[j])**2))
            if distance > max_distance:
                max_distance = distance
        return(max_distance)
    
    def fit(self,X_train):
        """
        Fit clustering model.
        self.centroids is updated for future predictions

        Parameters
        -----------
        X_train:np.array,
            training data     
        """
        init_time = time()
        self.centroids = self.pick_distinct(X_train)
        max_distance_centroids = 1 + self.epsilon
        n_iter = 0
        while n_iter < self.max_iter and max_distance_centroids > self.epsilon:
            clusters = self.partition(X_train)
            next_centroids = self.cluster_mean(clusters,X_train)
            max_distance_centroids = self.max_distance_centroids_clusterMeans(next_centroids)
            self.centroids = next_centroids
        self._fit_time = time() - init_time

    def predict(self,X_test):
        """
        Returns predicted cluster on given data X_test.

        Parameters
        -----------
        X_test:np.array,
            test data for predictions

        Returns
        -----------
        np.array of shape len(X_test)     
        """
        init_time = time()
        partition = self.partition(X_test)
        self._predict_time = time() - init_time
        return(partition)
    
    def display(self,X, feature_x_axis, feature_y_axis):
        """
        Displays the cluster predicted on data X.

        Parameters
        -----------
        X:np.array,
            data to be displayed
        feature_x_axis : int,
            index of feature displayed on x axis
        feature_y_axis : int,
            index of feature displayed on y axis
        """
        cluster = self.predict(X)      
        for i in range(self.k):
            plt.scatter(x=X[cluster==i][:,feature_x_axis], y=X[cluster==i][:,feature_y_axis], label=f'cluster {i}',alpha=0.7, marker='.') 
        plt.scatter(x=self.centroids[:,feature_x_axis],y=self.centroids[:,feature_y_axis], label='centroids')
        plt.title(f'Kmeans clustering\n(fit time = {np.format_float_scientific(self._fit_time,2)} s, predict time = {np.format_float_scientific(self._predict_time,2)} s)')
        plt.xlabel(f'feature {feature_x_axis}')
        plt.ylabel(f'feature {feature_y_axis}')
        plt.legend()
        plt.show()   




if __name__=="__main__":
    from sklearn.datasets import make_blobs

    X, y = make_blobs(n_samples=250, centers=5, n_features=5,random_state=50)
    model = Kmeans(k=5,max_iter=100, epsilon=0.1)
    model.fit(X)
    # print(model.predict(X))
    model.display(X,0,1)

