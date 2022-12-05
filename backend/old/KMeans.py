from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

class KMeans_model:

    def __init__(self, data, test_data):
        self.df = data
        self.test_data = test_data

    def model(self):
        kmeans = KMeans(5)
        kmeans.fit(self.df.iloc[:,:22])
        kmeans_out = kmeans.predict(self.df.iloc[:,:22])
        self.df['class_k'] = kmeans_out
        test_class = kmeans.predict(self.test_data)[0]
        result_df = self.df[self.df['class_k'] == test_class]
        result_df = result_df.drop('class_k', axis=1).reset_index(drop=True)
        return result_df
