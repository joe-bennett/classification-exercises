import pandas as pd

import env

titanic_connection=env.get_db_url('titanic_db')

#this is my initial function before I added caching to it

# def get_titanic_data():
#     return pd.read_sql('SELECT * FROM passengers',titanic_connection)


#this is my final function that searches for local csv file and if not there runs queriry, cache it, and brings up the dataframe

def get_titanic_data():
    filename = 'titanic_db.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        titanic_db= pd.read_sql('SELECT * FROM passengers',titanic_connection)
        titanic_db.to_csv('titanic_db')
        return titanic_db 





iris_connection=env.get_db_url('iris_db')



#this is my initial function before I added caching to it

# def get_iris_data():
#         return pd.read_sql('''SELECT * FROM measurements
#             JOIN species USING (species_id)''', iris_connection)



#this is my final function that searches for local csv file and if not there runs queriry, cache it, and brings up the dataframe


def get_iris_data():
     filename = 'iris_db.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        iris_db= pd.read_sql('''SELECT * FROM measurements
        JOIN species USING (species_id)''', iris_connection)
        iris_db.to_csv('iris_db')
        return iris_db




telco_connnect=env.get_db_url('telco_churn')



#this is my initial function before I added caching to it

# def get_telco_data():
#     return pd.read_sql('''SELECT * FROM contract_types
#                             JOIN customers USING (contract_type_id)
#                             JOIN internet_service_types USING (internet_service_type_id)
#                             JOIN payment_types USING (payment_type_id)''', telco_connnect)



#this is my final function that searches for local csv file and if not there runs queriry, cache it, and brings up the dataframe




def get_telco_data():
    filename = 'telco_churn.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else: telco_churn=pd.read_sql('''SELECT * FROM contract_types
    JOIN customers USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)''', telco_connnect)
    telco_churn.to_csv('telco_churn.csv')
    return telco_churn