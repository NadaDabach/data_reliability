import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore


def resample_data(real_test_case, freq='D'):
    """
    Resample the data to daily frequency.
    """
    data_samples = real_test_case.resample(freq, on='from_date').mean()
    return data_samples


def check_missing_values(real_test_case):
    """
    Check for missing values in the data.
    """
    missing_vals = real_test_case.isnull().sum()
    return missing_vals


def check_duplicates(real_test_case):
    """
    Check for duplicates in the data.
    """
    duplicates = real_test_case[real_test_case.duplicated()]
    return duplicates


def data_preprocessing(real_test_case):
    """
    Check data types and perform data conversion if necessary.
    """
    # Convert to datetime
    real_test_case['from_date'] = pd.to_datetime(real_test_case['from_date'])
    real_test_case['to_date'] = pd.to_datetime(real_test_case['to_date'])

    # Convert 'gender' and 'age' to categorical
    real_test_case['gender'] = real_test_case['gender'].astype('category')
    real_test_case['age'] = real_test_case['age'].astype('category')

    return real_test_case


def detect_outliers(real_test_case):
    """
    Check for outliers in the data.
    """
    # Boxplot
    sns.boxplot(x=real_test_case['count'], y=real_test_case['age'])
    plt.show()

    # Z-score calculation
    real_test_case['score'] = zscore(real_test_case['count'])
    outliers = real_test_case[real_test_case['score'].abs() > 3]

    return outliers

