from random import random

import numpy as np
import matplotlib.pyplot as plt


class KMeans:
    """
    1. Choose the number of clusters(K) and obtain the data points
    2. Place the centroids c_1, c_2, ..... c_k randomly
    3. Repeat steps 4 and 5 until convergence or until the end of a fixed number of iterations
    4. for each data point x_i:
           - find the nearest centroid(c_1, c_2 .. c_k)
           - assign the point to that cluster
    5. for each cluster j = 1..k
           - new centroid = mean of all points assigned to that cluster
    6. End
    """

    def __init__(self, k: int = 5):
        self.k = k
        self.centers = None
        self.ini_centers = None

    def fit(self, data: np.array):
        """
        Fits kmeans
        """
        n_samples, _ = data.shape

        # initialize cluster centers
        self.centers = np.array(random.sample(list(data), self.k))
        self.ini_centers = np.copy(self.centers)

        old_data_point_assignment = None
        n_iters = 0

        while True:
            data_point_assignment = [self.classify(datapoint) for datapoint in data]

            # If data point assignments stop changing, then we find the model
            if data_point_assignment == old_data_point_assignment:
                print(f"Training finished.. {n_iters} iterations!")
                print(f"Points assignment: {data_point_assignment}")
                return

            old_data_point_assignment = data_point_assignment
            n_iters = n_iters + 1

            # recalculate centers
            for i in range(self.k):
                points_idx = np.where(np.array(data_point_assignment) == i)
                datapoints = data[points_idx]
                self.centers[i] = datapoints.mean(axis=0)

    def euclidean_distance(self, data):
        return np.sqrt(np.sum((self.centers - data) ** 2, axis=1))

    def classify(self, data):
        """
        Return the cluster ID of that cluster.
        """
        return np.argmin(self.euclidean_distance(data))

    def show_clusters(self, data):
        plt.figure(figsize=(10, 8))
        plt.title("Initial centers in black, final centers in red")
        plt.scatter(data[:, 0], data[:, 1], marker='.', c=y)
        plt.scatter(self.centers[:, 0], self.centers[:, 1], c='r')
        plt.scatter(self.ini_centers[:, 0], self.ini_centers[:, 1], c='k')
        plt.show()
