# CSMatchData
This project is a simple machine learning model that predicts the results of Counter Strike: Global Offensive matches and rounds. 

The data used is professional match data from 2015-2020. Data source:
https://www.kaggle.com/datasets/mateusdmachado/csgo-professional-matches

## Layout of the project
The src folder is divided into three folders

### data
Contains runnable files for processing data as well as helper files. The main objective of the data folder is to process the data into a usable format with create_raw_db.py and convert_data.py. The secondary object is to undestand the data that I'm working with in data_analysis.py.

The raw and modified data is stored in db/CSMatchData.db

### features
Contains a file to convert the sql data from db/CSMatchData.db into a format that can be used to train the machine learning model. Training and testing data is stored into src/model/training_data in .pkl format. 

### models
Contains files to create, train and test the machine learning model with the created data. Saves the trained machine learning models into src/models/saved_models. 

## Set up the project
1. Install extensions with pip install -r requirements.txt
2. done
