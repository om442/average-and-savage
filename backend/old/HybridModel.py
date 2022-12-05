import pandas as pd
import numpy as np
from numpy.linalg import norm

class HybridModel:

    def __init__(self, kmeans_result, test_df):
        self.kmeans_result = kmeans_result
        self.test_data = test_df

    def model(self):
        self.cosine_list = []
        for index, row in self.kmeans_result.iterrows():
            self.cosine_list.append(
                np.dot(row.values, self.kmeans_result.loc[0].values)
                                /
                (norm(row.values)*norm(self.kmeans_result.loc[0].values))
            )

        list_of_users = np.array(self.cosine_list).argsort()[-10:][::-1]
        scores = sorted(self.cosine_list)[-10:][::-1]

        final_result = self.kmeans_result.loc[list_of_users]
        final_result['similarity_score'] = scores

        return final_result