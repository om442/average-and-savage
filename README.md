# **User Recommendation System for Data Enthusiasts**


### **Introduction**
The goal of this project is to provide users with a personalized list of other users that they are likely to be interested in for work collaboration. The idea is to create a platform to help users easily find fellow collaborators, removing the hassle and struggle of finding fellow team members that match the required skills and background and are equally enthusiastic about working together on a particular project. 


### **The Data**
Our dataset for user features comes from a Kaggle dataset of LinkedIn profile data containing information about profile and job data.
For a detailed description of the metadata or to download the dataset, refer to the Kaggle dataset listed below.
Link: https://www.kaggle.com/datasets/killbot/linkedin 


### **Architecture & Design**
See below for a high-level common process map of the system.
![processmap](assets/Common%20Process%20Map%20DSCI560.pdf)


### **Functions & Components**
The following functions/components are available in the application:
- Users can upload and view their own traffic collision data as a CSV file and attain monthly predictions for collision risk.
- Automatic cleaning, transforming, feature engineering, and uploading of data onto production cloud databases.
- Intuitive data exploration interface for exploring raw data, transformed features, geospatial mappings, and model results.
- Utilizing Pyspark for data streaming, feature extraction, and training ML models in parallel.
- Attain predicted risk ratings for Los Angeles City collision levels using Machine Learning models.
- Live data streaming and extraction using Apache Kafka.
- Projection and visualization of traffic collision data using geographical coordinates onto interactive geospatial maps.


### **Software & Tools**
The following software and tools were used to create this application:

**Databases & Storage**
- AWS Redshift: Cloud Relational Database
- AWS S3: Cloud Data Storage
- AWS EC2: Cloud Computing
- Apache Kafka: Data Streaming & Processing

**Software and Libraries**
- Python
    - Pandas
    - Numpy
    - Matplotlib
    - Seaborn
    - Requests
    - GeoPandas
    - Redshift_connector
    - JSON
    - SQL
    - PySpark
    - Spark Streaming
    - Spark MLlib
    - Streamlit
    - Kepler.gl

- Tools
    - Github
    - Git
    - Jupyter Notebook


## ***To view a demo of the application, click [here](https://drive.google.com/file/d/1hB8RYxFXCXPB5-pG7UXwCKUV-_z8JEYn/view?usp=sharing).***