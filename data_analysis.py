import pandas as pd
import matplotlib.pyplot as plt


def read_data(file_path):
    """
    Read the CSV file and perform data preprocessing.
    """
    simple_test_case = pd.read_csv(file_path)
    simple_test_case['gender'] = simple_test_case['gender'].astype('category')
    simple_test_case['age'] = simple_test_case['age'].astype('category')
    simple_test_case['from_date'] = pd.to_datetime(simple_test_case['from_date'])
    simple_test_case['to_date'] = pd.to_datetime(simple_test_case['to_date'])
    return simple_test_case


def calculate_store_daily_visits(data):
    """
    Calculate the store daily visits.
    """
    data['visits_date'] = data['from_date'].dt.date
    store_daily_visits = data.groupby('visits_date')['count'].sum().reset_index(name='store_daily_visits')
    return store_daily_visits


def calculate_gender_repartition(data):
    """
    Calculate the gender repartition in the store daily visits.
    """
    gender_repartition = data.groupby(['visits_date', 'gender'])['count'].sum().reset_index(name='store_daily_visits')
    pivot_gender_repartition = gender_repartition.pivot(index='visits_date', columns='gender', values='store_daily_visits').fillna(0)
    return pivot_gender_repartition


def calculate_age_proportions(data):
    """
    Calculate the proportion of young, adult, and older people in the store daily visits.
    """
    proportion = data.groupby(['visits_date', 'age'])['count'].sum().reset_index()
    proportions_by_age = proportion.pivot(index='visits_date', columns='age', values='count')
    store_daily_visits = proportions_by_age.sum(axis=1)
    proportions_by_age['daily_visits'] = store_daily_visits
    proportions_by_age['young'] = proportions_by_age['young'] / proportions_by_age['daily_visits']
    proportions_by_age['adult'] = proportions_by_age['adult'] / proportions_by_age['daily_visits']
    proportions_by_age['old'] = proportions_by_age['old'] / proportions_by_age['daily_visits']
    return proportions_by_age[['young', 'adult', 'old']]