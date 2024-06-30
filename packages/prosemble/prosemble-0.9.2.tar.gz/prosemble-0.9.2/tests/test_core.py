"""prosemble core test suite"""

import unittest
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
import prosemble as ps


# Distances
class TestDistances(unittest.TestCase):

    def setUp(self):
        self.nx, self.mx = 32, 6
        self.ny, self.my = 8, 6
        self.x = np.random.randn(self.nx, self.mx)
        self.y = np.random.randn(self.ny, self.my)

    def test_manhattan(self):
        actual = np.empty([self.nx, self.ny])
        desired = actual.copy()
        for i in range(self.nx):
            for j in range(self.ny):
                actual[i][j] = ps.core.manhattan_distance(
                    self.x[i],
                    self.y[j],
                )               
                desired[i][j] = pairwise_distances(
                    self.x[i].reshape(1, -1),
                    self.y[j].reshape(1, -1),
                    metric = "manhattan",
                )
        mismatch = np.testing.assert_array_almost_equal(
            actual,
            desired,
            decimal=2
            )
        self.assertIsNone(mismatch)

    def test_euclidean(self):
        actual = np.empty([self.nx, self.ny])
        desired = actual.copy()
        for i in range(self.nx):
            for j in range(self.ny):
                actual[i][j] = ps.core.euclidean_distance(
                    self.x[i],
                    self.y[j]
                )
                desired[i][j] = pairwise_distances(
                    self.x[i].reshape(1, -1),
                    self.y[j].reshape(1, -1),
                    metric = "euclidean",
                )
        mismatch = np.testing.assert_array_almost_equal(
            actual,
            desired,
            decimal=3
            )
        self.assertIsNone(mismatch)

    def test_squared_euclidean(self):

        actual = np.empty([self.nx, self.ny])
        desired = actual.copy()
        for i in range(self.nx):
            for j in range(self.ny):
                actual[i][j] = (ps.core.squared_euclidean_distance(
                    self.x[i],
                    self.y[j],
                )**2)
                
                desired[i][j] = (pairwise_distances(
                    self.x[i].reshape(1, -1),
                    self.y[j].reshape(1, -1),
                    metric="sqeuclidean",
                )**2)
        mismatch = np.testing.assert_array_almost_equal(actual,
                                                        desired,
                                                        decimal=2)
        self.assertIsNone(mismatch)       
    def tearDown(self):
        del self.x, self.y
