import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns


def prep_iris(iris_db):
    iris_db.drop(['species_id', 'measurement_id'], axis=1, inplace=True)
    iris_db.rename(columns={'species_name':'species'},inplace=True)
    dummy_df=pd.get_dummies(iris_db.species)
    iris_db=pd.concat([iris_db,dummy_df], axis=1)
    return iris_db

def prep_titanic(titanic_db):
    titanic_db.drop(['passenger_id','class','embark_town'],axis=1, inplace=True)
    dum_var=pd.get_dummies(titanic_db[['sex','embarked']],drop_first=True)
    titanic_db=pd.concat([titanic_db,dum_var],axis=1)
    return titanic_db
    


def prep_telco(telco_db):
    telco_db.drop(['payment_type_id','internet_service_type_id','contract_type_id'], axis=1, inplace=True)
    dum_var=pd.get_dummies(telco_db[['gender','partner','dependents','phone_service','multiple_lines','online_security',
                                'device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn', 'internet_service_type','payment_type']],drop_first=True)
    telco_db=pd.concat([telco_db,dum_var],axis=1)
    return telco_db




def split_data(df, target):
    '''
    Takes in a dataframe and return train, validate, test subset dataframes
    '''
    train, test = train_test_split(df, test_size=.2, 
                               random_state=123, stratify=df[target])
    train, validate = train_test_split(train, test_size=.25, 
                 random_state=123, stratify=train[target])
    
    return train, validate, test