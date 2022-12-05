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
data = pd.read_csv("linkedin_finaldata.csv", encoding = "ISO-8859-1")

filters = {'min_exp': 0, 'skills':[]}

# these come from the UI
min_exp = 2
skills = ['Tensorflow', 'Python', 'Machine Learning', 'Data Modelling']

# Filters
filters['min_exp'] = min_exp
filters['skills'] = skills

# Preprocessing
FeaturePreprocessing_obj = FeaturePreprocessing(data, filters)
processed_df = FeaturePreprocessing_obj.preprocess()

print(processed_df.columns)

# print('Feature processing done')

# Fetching LinkedIn data
FetchProfileData_obj = FetchProfileData('Parth Kapadia', 'parthjil@usc.edu')
profile = FetchProfileData_obj.get_profile()
print('Profile fetched')

# Creating test datafrane
FormatData_obj = FormatData(profile)
test_data = FormatData_obj.get_test_data_format()

test_df = pd.DataFrame.from_dict(test_data, orient='index')
test_df = test_df.T
print(test_df.shape)
print('test data created')

# KMeans
kmeans_model_obj = KMeans_model(deepcopy(processed_df), deepcopy(test_df))
kmeans_result = kmeans_model_obj.model()
kmeans_result_10 = kmeans_result.sample(10)
print('List of users in the same cluster:')
print(kmeans_result_10)

# Cosine Similarity
cosine_model_obj = Cosine(deepcopy(processed_df), deepcopy(test_df))
cosine_result = cosine_model_obj.model()

print('List of users most similar using cosine similarity:')
print(cosine_result)

# Hybrid Model
hybrid_model_obj = HybridModel(kmeans_result, deepcopy(test_df))
hybrid_model_result = hybrid_model_obj.model()

print('List of users most similar using hybrid model:')
print(hybrid_model_result)

result = hybrid_model_result.merge(data, on='ID', how='left')
# cols_to_consider = ['ID', 'name' ,'c_name', 'skills', 'avg_n_pos_per_prev_tenure_x', 'avg_pos_len_x',
#        'avg_prev_tenure_len_x', 'n_pos_x', 'n_prev_tenures_x', 'tenure_len_x',
#        'age_x', 'african_x', 'celtic_english_x', 'east_asian_x', 'european_x',
#        'greek_x', 'hispanic_x', 'jewish_x', 'muslim_x', 'nordic_x',
#        'south_asian_x', 'n_followers_x', 'gender_Female', 'gender_Male',
#        'ethnicity_Asian', 'ethnicity_Black', 'ethnicity_White',
#        'similarity_score']
cols_to_consider = ['ID', 'name' ,'c_name', 'skills', 'avg_n_pos_per_prev_tenure_x', 'avg_pos_len_x','similarity_score']
result = result.rename(columns={'name': 'Name', 'oldName2': 'newName2'})

print(result[cols_to_consider])

df = result[cols_to_consider]

df2 = df.to_dict('index')
print(df2)
