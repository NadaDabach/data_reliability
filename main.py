import data_analysis as da
import data_visualization as dv
import anomalies_identification as ai
import glob
import pandas as pd


def main():
    file_path = "dataset/simple_test_case/data_0.csv"
    save_dir = "visualizations"

    # Read data
    simple_test_case = da.read_data(file_path)

    # Calculate store daily visits
    store_daily_visits = da.calculate_store_daily_visits(simple_test_case)

    # Visualize store daily visits
    dv.visualize_store_daily_visits(store_daily_visits, save_dir=save_dir)

    # Calculate gender repartition
    gender_repartition = da.calculate_gender_repartition(simple_test_case)

    # Visualize gender repartition
    dv.visualize_gender_repartition(gender_repartition, save_dir=save_dir)

    # Calculate age proportions
    age_proportions = da.calculate_age_proportions(simple_test_case)

    # Visualize age proportions
    dv.visualize_age_proportions(age_proportions)

    # Define the directory path
    data_dir = "dataset/real_test_case"

    # Get a list of all CSV files matching the pattern
    file_paths = glob.glob(data_dir + '/*.csv')

    # Read data
    dfs = [pd.read_csv(file) for file in file_paths]
    real_test_case = pd.concat(dfs, ignore_index=True)

    # Preprocess data
    real_test_case = ai.data_preprocessing(real_test_case)

    # Check for missing values
    missing_vals = ai.check_missing_values(real_test_case)
    print("Missing Values:\n", missing_vals)

    # Check for duplicates
    duplicates = ai.check_duplicates(real_test_case)
    print("Duplicates:\n", duplicates)

    # Check data types and perform data conversion
    real_test_case = ai.data_preprocessing(real_test_case)
    print("Data Types after Conversion:\n", real_test_case.dtypes)

    # Detect outliers
    outliers = ai.detect_outliers(real_test_case)
    print("Outliers:\n", outliers)


if __name__ == "__main__":
    main()
