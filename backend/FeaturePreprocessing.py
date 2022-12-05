from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

class FeaturePreprocessing:
    def __init__(self, data, filters):
        self.df = data
        self.filters = filters

    def filter(self):

        # Yrs of exp
        if self.filters['min_exp'] > 0:
            self.filters['min_exp'] = self.filters['min_exp'] * 365
        self.df = self.df[self.df['tenure_len'] > self.filters['min_exp']]

        # skills
        if self.filters['skills']:
            for skill in  self.filters['skills']:
                self.df = self.df[self.df[skill] == 1]

        # age
        if self.filters['age']:
            self.df = self.df[self.df['age'] > self.filters['age']]

        # gender
        if self.filters['gender']:
            if self.filters['gender'] == 'Male':
                self.df = self.df[self.df['gender_Male'] == 1]
            else:
                self.df = self.df[self.df['gender_Female'] == 1]

    def preprocess(self):

        skills = ['Python', 'Tensorflow', 'Statistical Analysis', 'Project Management', 'Scrum Master',
          'Data Modelling', 'Machine Learning', 'Database Management', 'Deep Learning']

        labelencoder = LabelEncoder()
        # Assigning numerical values and storing in another column
        self.df['c_name_type'] = labelencoder.fit_transform(self.df['c_name'])

        self.df = pd.get_dummies(self.df, columns = ['gender', 'ethnicity'])

        self.filter()

        self.df.drop(skills, axis=1, inplace=True)

        self.df.drop([
                      'm_urn', 'beauty', 'beauty_female', 'beauty_male', 'blur',
                      'blur_gaussian', 'blur_motion', 'emo_anger', 'emo_disgust',
                      'emo_fear', 'emo_happiness', 'emo_neutral', 'emo_sadness',
                      'emo_surprise', 'face_quality', 'glass', 'head_pitch',
                      'head_roll', 'head_yaw','img', 'mouth_close', 'mouth_mask',
                      'mouth_open', 'mouth_other', 'skin_acne', 'skin_dark_circle',
                      'skin_health', 'skin_stain', 'smile','c_name', 'nationality',
                      'c_name_type', 'name', 'skills'
                      ],axis=1, inplace=True)

        self.df = self.df.drop_duplicates()
        self.df = self.df.reset_index(drop=True)
        return self.df


# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
# import pandas as pd

# class FeaturePreprocessing:
#     def __init__(self, data, filters):
#         self.df = data
#         self.filters = filters

#     def filter(self):

#         # Yrs of exp
#         if self.filters['min_exp'] > 0:
#             self.filters['min_exp'] = self.filters['min_exp'] * 365
#         self.df = self.df[self.df['tenure_len'] > self.filters['min_exp']]

#         # skills
#         if self.filters['skills']:
#             for skill in  self.filters['skills']:
#                 self.df = self.df[self.df[skill] == 1]
        
#         # age
#         if self.filters['age']:
#             self.df = self.df[self.df['age'] > self.filters['age']]
        
#         # gender
#         if self.filters['gender']:
#             if self.filters['gender'] == 'Male':
#                 self.df = self.df[self.df['gender_Male'] == 1]
#             elif self.filters['gender'] == 'Female':
#                 self.df = self.df[self.df['gender_Female'] == 1]
#             else:
#                 pass
            

#     def preprocess(self):

#         skills = ['Python', 'Tensorflow', 'Statistical Analysis', 'Project Management', 'Scrum Master',
#           'Data Modelling', 'Machine Learning', 'Database Management', 'Deep Learning']

#         labelencoder = LabelEncoder()
#         # Assigning numerical values and storing in another column
#         self.df['c_name_type'] = labelencoder.fit_transform(self.df['c_name'])

#         self.df = pd.get_dummies(self.df, columns = ['gender', 'ethnicity'])

#         self.filter()

#         self.df.drop(skills, axis=1, inplace=True)

#         self.df.drop([
#                       'm_urn', 'beauty', 'beauty_female', 'beauty_male', 'blur',
#                       'blur_gaussian', 'blur_motion', 'emo_anger', 'emo_disgust',
#                       'emo_fear', 'emo_happiness', 'emo_neutral', 'emo_sadness',
#                       'emo_surprise', 'face_quality', 'glass', 'head_pitch',
#                       'head_roll', 'head_yaw','img', 'mouth_close', 'mouth_mask',
#                       'mouth_open', 'mouth_other', 'skin_acne', 'skin_dark_circle',
#                       'skin_health', 'skin_stain', 'smile','c_name', 'nationality',
#                       'c_name_type', 'name', 'skills'
#                       ],axis=1, inplace=True)

#         self.df = self.df.drop_duplicates()
#         self.df = self.df.reset_index(drop=True)
#         return self.df