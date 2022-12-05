import pandas as pd
import numpy as np
from numpy.linalg import norm

class Cosine:

    def __init__(self, data, test_df):
        self.df = data
        self.test_data = test_df

    def model(self):

        df_cosine = pd.DataFrame().reindex_like(self.df)
        df_cosine = df_cosine.dropna()
        df_cosine.loc[len(df_cosine.index)] = self.test_data.loc[0]
        print(df_cosine)
        cosine_list = []
        for index, row in self.df.iterrows():
            cosine_list.append(
                np.dot(row.values, df_cosine.loc[0].values)
                                /
                (norm(row.values)*norm(df_cosine.loc[0].values))
            )

        list_of_users = np.array(cosine_list).argsort()[-10:][::-1]
        scores = sorted(cosine_list)[-10:][::-1]
        print(scores)
        final_result = self.df.loc[list_of_users]
        final_result['similarity_score'] = scores

        return final_result