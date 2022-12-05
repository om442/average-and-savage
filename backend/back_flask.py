from flask import Flask, request, jsonify, render_template
from LinkedinDataFetch import FetchProfileData
from FormatProfile import FormatData
from FeaturePreprocessing import FeaturePreprocessing
from Cosine import Cosine
from KMeans import KMeans_model
from HybridModel import HybridModel
import json
import pandas as pd
from copy import deepcopy
from flask_cors import CORS, cross_origin
import collections

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def home():
    return render_template('/averageandsavage-main/frontend/my-app/src/page/Recommendation.jsx')

@app.route('/recommendation', methods=['GET'])
def recommendation():

    args = request.args
    name = request.args['name']
    email = request.args['id']
    min_exp = int(request.args['experience'])
    skill = request.args['skills']
    age = int(request.args['age'])
    gender = request.args['gender']

    skill = skill.rstrip(skill[-1])
    skills = skill.split(", ")
    
    # Feature preprocessing
    data = pd.read_csv("linkedin_finaldata.csv", encoding = "ISO-8859-1")

    filters = {'min_exp': 0, 'skills':[], 'age' : 0, 'gender' : '' }

    # these come from the UI
    #min_exp = 2
    #skills = ['Tensorflow', 'Python', 'Machine Learning', 'Data Modelling']

    # Filters
    filters['min_exp'] = min_exp
    filters['skills'] = skills
    # filters['age'] = age
    # filters['gender'] = gender

    # these come from the UI
    # Filters
    filters['min_exp'] = min_exp
    filters['skills'] = skills
    filters['age'] = age
    filters['gender'] = gender

    print(filters)

    # Preprocessing
    FeaturePreprocessing_obj = FeaturePreprocessing(data, filters)
    processed_df = FeaturePreprocessing_obj.preprocess()


    print('Feature processing done')

    # Fetching LinkedIn data
    FetchProfileData_obj = FetchProfileData('Parth Kapadia', 'parthjil@usc.edu')
    profile = FetchProfileData_obj.get_profile()

    if profile:
        print('Profile fetched')
        FormatData_obj = FormatData(profile)
    else:
        print("Error fetching profile")


    # Creating test datafrane
    if profile:
        FormatData_obj = FormatData(profile)

    try:
        test_data = FormatData_obj.get_test_data_format()

        if test_data:
            test_df = pd.DataFrame.from_dict(test_data, orient='index')
            test_df = test_df.T
            print('test data created')

    except:
        print("Error creating test data")




    # # Preprocessing
    # FeaturePreprocessing_obj = FeaturePreprocessing(data, filters)
    # processed_df = FeaturePreprocessing_obj.preprocess()

    # print(processed_df.columns)

    # # print('Feature processing done')

    # # Fetching LinkedIn data
    # FetchProfileData_obj = FetchProfileData(name, email)
    # profile = FetchProfileData_obj.get_profile()
    # print('Profile fetched')
    # print(profile)

    # # Creating test datafrane
    # FormatData_obj = FormatData(profile)
    # test_data = FormatData_obj.get_test_data_format()

    # test_df = pd.DataFrame.from_dict(test_data, orient='index')
    # test_df = test_df.T
    # print(test_df.shape)
    # print('test data created')

    # KMeans
    kmeans_model_obj = KMeans_model(deepcopy(processed_df), deepcopy(test_df))
    kmeans_result = kmeans_model_obj.model()
    kmeans_result_10 = kmeans_result.sample()
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
    #     'avg_prev_tenure_len_x', 'n_pos_x', 'n_prev_tenures_x', 'tenure_len_x',
    #     'age_x', 'african_x', 'celtic_english_x', 'east_asian_x', 'european_x',
    #     'greek_x', 'hispanic_x', 'jewish_x', 'muslim_x', 'nordic_x',
    #     'south_asian_x', 'n_followers_x', 'gender_Female', 'gender_Male',
    #     'ethnicity_Asian', 'ethnicity_Black', 'ethnicity_White',
    #     'similarity_score']


    cols_to_consider = ['name' ,'c_name', 'skills','similarity_score','age_x']
    print(result[cols_to_consider])
    df = result[cols_to_consider]
    df = df.rename(columns={'name': 'Name', 'age_x': 'Age', 'c_name' : 'Previously Worked','skills': 'Skills', 'similarity_score' : 'Similarity Score'})
    args = df.to_dict('index')

    # args = {'tryi':{
    #     'Name1':'Harsha Mishra', 
    #     "Name2":"Nandita Rao",
    #     "Name3":"Zubin Das",
    #     "Name4":"Bradley Booth", 
    #     "Name5":"Janet Bryan"},
    #     'try2' : {
    #     "Name6":name,
    #     "Name7":email, 
    #     "Name8":exp,
    #     "Name9":skill}
    
    # }

    print(type(args))

    return args
    #return 


if __name__ == '__main__':
    app.run()
    
