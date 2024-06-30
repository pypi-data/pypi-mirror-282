"""
Implementation of Kernel Possibilistic Fuzzy c-Means Alternative Optimization Algorithm
"""

# Author: Nana Abeka Otoo <abekaotoo@gmail.com>
# License: MIT

from collections import Counter

import numpy as np
from matplotlib import pyplot as plt
from prosemble.core.distance import (
    euclidean_distance,
    squared_euclidean_distance
)
from .fcm import FCM
from .kfcm import KFCM


class KPFCM:
    """
    params:

    data : array-like:
        input data

    c: int:
        number of clusters

    m: int:
        fuzzy parameter

    k: float:
        gamma parameter

    k: float:
        parameter for gamma

    num_iter: int:
        number of iterations

    epsilon: float:
        small difference for termination of algorithm

    ord:  {non-zero int, inf, -inf, ‘fro’, ‘nuc’}
          order of the norm

    eta: int:
        eta parameter

    a: int:
        a parameter

    b: int:
        b parameter

    sigma:int
        sigma parameter

    set_centroids: array-like:
        initial prototypes to  begin with. default is None


   set_U_matrix: array-like:
        initial U matrix to  begin with. default is None

    plot_steps: bool:
        True for visualisation of training and False otherwise

   """

    def __init__(self, data, c, m, k, num_iter, epsilon, ord, eta, a, b, sigma,
                 set_centroids=None,
                 set_U_matrix=None,
                 plot_steps=False):
        self.data = data
        self.num_clusters = c
        self.fuzzifier = m
        self.k = k
        self.num_iter = num_iter
        self.epsilon = epsilon
        self.set_U_matrix = set_U_matrix
        self.set_centroids = set_centroids
        self.set_prototypes = []
        self.plot_steps = plot_steps
        self.ord = ord
        self.eta = eta
        self.a = a
        self.b = b
        self.sigma = sigma
        self.objective_function = []
        self.fit_cent = []
        self.fit_clus = []

        if self.set_U_matrix == 'fcm':
            self.model1 = FCM(
                data=self.data,
                c=self.num_clusters,
                m=self.fuzzifier,
                num_iter=self.num_iter,
                epsilon=self.epsilon,
                ord=self.ord
            )
            self.model1.fit()
            self.set_U_matrix = self.model1.predict_proba_(self.data)
            self.set_prototypes.append(self.model1.final_centroids())

        if self.set_U_matrix == 'kfcm':
            self.model2 = KFCM(
                data=self.data,
                c=self.num_clusters,
                m=self.fuzzifier,
                num_iter=self.num_iter,
                epsilon=self.epsilon,
                sigma=self.sigma,
                ord=self.ord
            )
            self.model2.fit()
            self.set_U_matrix = self.model2.predict_proba_(self.data)
            self.set_prototypes.append(self.model2.final_centroids())

        if not isinstance(self.data, np.ndarray):
            self.data = np.array(self.data)

        if self.set_U_matrix is not None:
            if not isinstance(self.set_U_matrix, np.ndarray):
                self.set_U_matrix = np.array(self.set_U_matrix)
            if self.set_U_matrix.shape[1] != self.num_clusters:
                raise ValueError(f'The input dim of fuzzy U matrix {self.set_U_matrix.shape[1]} '
                                 f'!= number of cluster {self.num_clusters}')
            if len(self.set_U_matrix) != self.data.shape[0]:
                raise ValueError('There should one prototype per class')

    def randomly_initialised_fuzzy_matrix(self):
        return np.random.dirichlet(np.ones(self.num_clusters), size=self.data.shape[0])

    def _select_centroids_randomly(self):
        random_samples_feature_space = np.random.choice(
            self.data.shape[0],
            self.num_clusters, replace=False
        )
        return [self.data[index] for index in random_samples_feature_space]

    def compute_centroids(self, fuzzy_matrix, t_matrix, centroids):

        fuzzified_assignments = \
            [(np.power([u_ik[i] for _, u_ik in enumerate(fuzzy_matrix)], self.fuzzifier) * self.a) +
             (np.power([t_ik[i] for _, t_ik in enumerate(t_matrix)], self.eta) * self.b)
             for i in range(self.num_clusters)]

        centroid_numerator = \
            [[np.multiply(fuzzified_assignments[cluster_index][index], sample) *
              self.gaussian_kernel(sample, centroids[cluster_index])
              for index, sample in enumerate(self.data)]
             for cluster_index in range(self.num_clusters)]

        centroid_denomenator = [
            [np.multiply(fuzzified_assignments[cluster_index][index],
                         self.gaussian_kernel(sample, centroids[cluster_index]))
             for index, sample in enumerate(self.data)]
            for cluster_index in range(self.num_clusters)
        ]

        sum_centroid_denomenator = [np.sum(i) for i in centroid_denomenator]

        centroid = np.array(
            [np.sum(v, axis=0) / sum_centroid_denomenator[i]
             for i, v in enumerate(centroid_numerator)]
        )

        return centroid

    def compute_gamma(self, fuzzy_matrix, centriods):

        fuzzified_assignments = \
            [np.power([u_ik[i] for _, u_ik in enumerate(fuzzy_matrix)], self.fuzzifier)
             for i in range(self.num_clusters)]

        sum_fuzzified_assigments = [np.sum(i) for i in fuzzified_assignments]

        centroid_numerator = [
            [np.multiply(fuzzified_assignments[cluster_index][index],
                         (2 - 2 * self.gaussian_kernel(sample, centriods[cluster_index]))) for
             index, sample in enumerate(self.data)] for cluster_index in range(self.num_clusters)]

        gamma = np.array(
            [np.sum(v, axis=0) * self.k / sum_fuzzified_assigments[i]
             for i, v in enumerate(centroid_numerator)]
        )

        return gamma

    def update_fuzzy_matrix(self, centroids, u_matrix):
        initial_u_matrix = u_matrix
        for i in range(len(self.data)):
            denomenator = 0
            for j in range(self.num_clusters):
                denomenator += np.power(
                    1 / (1 - self.gaussian_kernel(centroids[j], self.data[i])),
                    1 / (self.fuzzifier - 1))
            for j in range(self.num_clusters):
                uik_new = np.power(1 / (1 - self.gaussian_kernel(centroids[j], self.data[i])),
                                   1 / (self.fuzzifier - 1)) / denomenator
                initial_u_matrix[i][j] = uik_new
        return initial_u_matrix

    def update_tipicality_matrix(self, centroids, g_matrix, t_matrix):
        initial_t_matrix = t_matrix
        for i in range(len(self.data)):
            for j in range(self.num_clusters):
                denomenator = \
                    np.power(self.b * (
                            2 * (1 - self.gaussian_kernel(centroids[j], self.data[i])) / g_matrix[j]
                    ), 1 / (self.eta - 1))
                tik_new = 1 / (1 + denomenator)
                initial_t_matrix[i][j] = tik_new
        return initial_t_matrix

    def _select_fuzzy_U_matrix(self):
        if self.set_U_matrix is None:
            return self.randomly_initialised_fuzzy_matrix()
        return self.set_U_matrix

    def _select_prototypes(self):
        if self.set_centroids is None:
            return self._select_centroids_randomly()
        if self.set_centroids == 'fcm':
            return self.set_prototypes[0]
        if self.set_centroids == 'kfcm':
            return self.set_prototypes[0]

    def compute_objective_function_0(self, centroids, u_matrix, t_matrix):
        objective_distance = \
            np.sum([[(2 - 2 * self.gaussian_kernel(self.data[i], centroids[j])) *
                     (self.a * np.power(u_matrix[i][j], self.fuzzifier) +
                      np.power(t_matrix[i][j], self.eta) * self.b)
                     for i in range(len(self.data))] for j in range(self.num_clusters)])

        return objective_distance

    def compute_objective_function_1(self, t_matrix, gamma):
        objective_function = \
            np.sum([gamma[j] * (np.sum([
                np.power((1 - t_matrix[i][j]), self.eta)
                for i in range(len(self.data))])) for j in range(self.num_clusters)]
                   )

        return objective_function

    def compute_objective_function(self, centroids, gamma, u_matrix, t_matrix):
        return self.compute_objective_function_0(centroids, u_matrix, t_matrix) + \
            self.compute_objective_function_1(t_matrix=t_matrix, gamma=gamma)

    @staticmethod
    def _distance_(samples, centroid):
        return np.sum([euclidean_distance(sample, centroid) for index, sample in enumerate(samples)])

    def gaussian_kernel(self, x, y):
        return np.exp(-squared_euclidean_distance(x, y) / (self.sigma ** 2))

    @staticmethod
    def _nearest_centroids(sample, centroids):
        return np.argmin([euclidean_distance(sample, centroid) for centroid in centroids])

    def _centroid_stability(self, centroids_num, centroids):
        if self.ord is not None and self.epsilon is None:
            distance = np.linalg.norm((centroids_num - centroids), ord=self.ord)
            return distance == 0
        if self.ord is not None and self.epsilon is not None:
            distance = np.linalg.norm((centroids_num - centroids), ord=self.ord)
            return distance <= self.epsilon
        if self.ord is None and self.epsilon is None:
            distance = [euclidean_distance(centroids_num[index], centroids[index]) for index in
                        range(self.num_clusters)]
            return np.sum(distance) == 0
        if self.ord is None and self.epsilon is not None:
            distance = [euclidean_distance(centroids_num[index], centroids[index]) for index in
                        range(self.num_clusters)]
            return np.sum(distance) <= self.epsilon
        return None

    def _get_cluster_results(self, cluster_result):
        labels = np.empty(self.data.shape[0])
        for cluster_index, cluster in enumerate(cluster_result):
            for sample_index in cluster:
                labels[sample_index] = cluster_index
        return labels

    def initialise_cluster(self, centroids):
        clusters = [[] for _ in range(len(centroids))]
        for index, sample in enumerate(self.data):
            centroid_index = self._nearest_centroids(sample, centroids)
            clusters[centroid_index].append(index)
        return clusters

    def get_centroids(self):
        u_matrix = self._select_fuzzy_U_matrix()
        t_matrix = self.randomly_initialised_fuzzy_matrix()
        centroids = self.compute_centroids(u_matrix, t_matrix, self._select_prototypes())
        for num in range(self.num_iter):
            centroids_old = centroids
            clusters = self.initialise_cluster(centroids_old)
            self.get_plot(clusters, centroids_old)
            u_matrix = self.update_fuzzy_matrix(centroids_old, u_matrix)
            gamma = self.compute_gamma(u_matrix, centroids)
            t_matrix = self.update_tipicality_matrix(centroids, gamma, t_matrix)
            obj = self.compute_objective_function(centroids, gamma, u_matrix, t_matrix)
            self.objective_function.append(obj)
            centroids = self.compute_centroids(u_matrix, t_matrix, centroids_old)
            self.get_plot(clusters, centroids)
            if self._centroid_stability(centroids_old, centroids) or num == self.num_iter - 1:
                self.fit_clus.append(clusters)
                self.fit_cent.append(centroids)
                break

    def get_centroids_(self):
        u_matrix = self._select_fuzzy_U_matrix()
        t_matrix = self.randomly_initialised_fuzzy_matrix()
        centroids = self.compute_centroids(u_matrix, t_matrix, self._select_prototypes())
        optimize = True
        while optimize:
            clusters = self.initialise_cluster(centroids)
            self.get_plot(clusters, centroids)
            gamma = self.compute_gamma(u_matrix, centroids)
            t_matrix = self.update_tipicality_matrix(centroids, gamma, t_matrix)
            u_matrix = self.update_fuzzy_matrix(centroids, u_matrix)
            centroid_num = centroids
            centroids = self.compute_centroids(u_matrix, t_matrix, centroids)
            self.objective_function.append(self.compute_objective_function(
                centroids,
                gamma,
                u_matrix,
                t_matrix)
            )
            self.get_plot(clusters, centroids)
            if self._centroid_stability(centroid_num, centroids):
                self.fit_clus.append(clusters)
                self.fit_cent.append(centroids)
                optimize = False

    def get_plot(self, cluster, centroids):
        if self.plot_steps:
            for _, v in enumerate(cluster):
                plt.scatter(self.data[v][:, 0], self.data[v][:, 1])
            for cent in centroids:
                plt.scatter(cent[0], cent[1], marker='v', color='black')
            plt.pause(0.3)
            plt.clf()

    def get_objective_function(self):
        """

        :return: The objective function
        """

        return self.objective_function

    def predict(self):
        """

        :return: array-like: cluster labels of the input dataset
        """
        return self._get_cluster_results(self.fit_clus[0])

    def predict_new(self, x):
        """

        :param x: array-like: input vector
        :return: cluster label of input vector
        """

        return [
            self._nearest_centroids(sample, self.fit_cent[0]) for index, sample in enumerate(x)
        ]

    def get_clusters_index_cent(self):
        return self.fit_clus, self.fit_cent

    def fit(self):
        """

        :return: fits the data set to the model
        """
        if self.num_iter is None:
            return self.get_centroids_()
        return self.get_centroids()

    def get_distance_space(self, x):
        """

        :param x: array-like: input vector
        :return: distance space of the input vector
        """

        distance_space = \
            np.array([[euclidean_distance(sample, centroid)
                       for centroid in self.get_clusters_index_cent()[1][0]]
                      for index, sample in enumerate(x)])
        return distance_space

    def predict_proba_(self, x):
        """

        :param x: array-like: input vector
        :return: confidence of predicted label
        """
        final_matrix = np.zeros((len(x), self.num_clusters))
        for i in range(len(x)):
            denomenator = 0
            for j in range(self.num_clusters):
                denomenator += np.power(
                    1 / (1 - self.gaussian_kernel(self.fit_cent[0][j], x[i])),
                    1 / (self.fuzzifier - 1))
            for j in range(self.num_clusters):
                uik_new = np.power(1 / (1 - self.gaussian_kernel(self.fit_cent[0][j], x[i])),
                                   1 / (self.fuzzifier - 1)) / denomenator
                final_matrix[i][j] = uik_new
        return final_matrix

    def get_prototypes(self, labels):
        """

        :param labels: array-like: labels of the input data set
        :return: prototypes for the GNPC classifier design
        """
        self.fit()
        clusters_indices, centroids = self.fit_clus[0], self.fit_cent[0]
        clusters = [labels[cluster_with_indices] for cluster_with_indices in clusters_indices]
        max_occurrence = [dict(Counter(cluster)) for _, cluster in enumerate(clusters)]
        reposition_centroids = np.argsort([max(count, key=count.get) for count in max_occurrence])
        prototypes = centroids[reposition_centroids]
        return prototypes, centroids

    def final_centroids(self):
        """

        :return: learned centroids
        """
        return self.fit_cent[0]
