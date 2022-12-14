# **User Recommendation System for Data Enthusiasts**


### **Introduction**
The goal of this project is to provide users with a personalized list of recommended LinkedIn profiles that they are likely to be interested in for work collaboration. The idea is to create a platform to help users easily find fellow collaborators, removing the hassle and struggle of finding fellow team members that match the required skills and background and are equally enthusiastic about working together on a particular project.

Using only their LinkedIn profile parameters, users will be given a recommended list of highly similar individuals which can be filtered to user specifications. The recommendation system uses a combination of K-Means and Cosine Similarity to determine a user-similarity score.

### **The Data**
Our dataset for user features comes from a Kaggle dataset of LinkedIn profile data containing information about profile and job data.
For a detailed description of the metadata or to download the dataset, refer to the Kaggle dataset listed below.

Link: https://www.kaggle.com/datasets/killbot/linkedin 


### **Architecture & Design**
See below for a high-level common process map of the system:

![processmap](assets/Common%20Process%20Map%20DSCI560.png)


### **Functions & Components**
The following functions/components are available in the application:
- Users can input the full name and email address associated with their LinkedIn profile to receive a list of recommendations.
- Users can filter results by age, experience, skills, etc.
- Curated list of project collaboration websites available for future collaboration.


### **Software & Tools**
The following software and tools were used to create this application:

**Frontend**
- HTML
- CSS
    - Bootstrap
- JavaScript
    - React
    - Node

**Backend**
- Python
    - Flask
    - Pandas
    - Numpy
    - Scikit-Learn
    - JSON
    - Requests


## ***To view a demo of the application, click [here](https://drive.google.com/file/d/1gDdcGGiblHYjUHNzHyMxkigXe7z9Y4ZW/view?usp=share_link).***