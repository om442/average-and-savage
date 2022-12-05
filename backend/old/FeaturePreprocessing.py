from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

class FeaturePreprocessing:
    def __init__(self, data):
        self.df = data

    def preprocess(self):
        labelencoder = LabelEncoder()
        # Assigning numerical values and storing in another column
        self.df['c_name_type'] = labelencoder.fit_transform(self.df['c_name'])

        self.df = pd.get_dummies(self.df, columns = ['gender', 'ethnicity'])

        self.df.drop([
                      'm_urn', 'beauty', 'beauty_female', 'beauty_male', 'blur',
                      'blur_gaussian', 'blur_motion', 'emo_anger', 'emo_disgust',
                      'emo_fear', 'emo_happiness', 'emo_neutral', 'emo_sadness',
                      'emo_surprise', 'face_quality', 'glass', 'head_pitch',
                      'head_roll', 'head_yaw','img', 'mouth_close', 'mouth_mask',
                      'mouth_open', 'mouth_other', 'skin_acne', 'skin_dark_circle',
                      'skin_health', 'skin_stain', 'smile','c_name','Unnamed: 0',
                      'nationality','tenure_len','c_name_type'
                      ],axis=1, inplace=True)

        self.df = self.df.drop_duplicates()
        return self.df
