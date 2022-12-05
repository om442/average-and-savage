from LinkedinDataFetch import FetchProfileData
from FormatProfile import FormatData
from FeaturePreprocessing import FeaturePreprocessing
from Cosine import Cosine
from KMeans import KMeans_model
from HybridModel import HybridModel
import json
import pandas as pd
from copy import deepcopy


# Feature preprocessing
data = pd.read_csv("linkedin_data.csv", encoding = "ISO-8859-1")
FeaturePreprocessing_obj = FeaturePreprocessing(data)
processed_df = FeaturePreprocessing_obj.preprocess()

print('Feature processing done')

# Fetching LinkedIn data
FetchProfileData_obj = FetchProfileData('Parth Kapadia', 'parthjil@usc.edu')
profile = FetchProfileData_obj.get_profile()
print('Profile fetched')

# Creating test datafrane
FormatData_obj = FormatData(profile)
test_data = FormatData_obj.get_test_data_format()

test_df = pd.DataFrame.from_dict(test_data, orient='index')
test_df = test_df.T
print('test data created')

# KMeans
kmeans_model_obj = KMeans_model(deepcopy(processed_df), deepcopy(test_df))
kmeans_result = kmeans_model_obj.model()
kmeans_result_10 = kmeans_result.sample(10)
# print('List of users in the same cluster:')
# print(kmeans_result_10)

# Cosine Similarity
cosine_model_obj = Cosine(deepcopy(processed_df), deepcopy(test_df))
cosine_result = cosine_model_obj.model()

# print('List of users most similar using cosine similarity:')
# print(cosine_result)

# Hybrid Model
hybrid_model_obj = HybridModel(kmeans_result, deepcopy(test_df))
hybrid_model_result = hybrid_model_obj.model()

print('List of users most similar using hybrid model:')
print(hybrid_model_result) 

