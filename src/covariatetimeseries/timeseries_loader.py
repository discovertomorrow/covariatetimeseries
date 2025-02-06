import pandas as pd

DATASET_INFO_PATH='src/covariatetimeseries/data_collections/_collection_info.csv'
DATASET_DIR_PATH="src/covariatetimeseries/data_collections"

def load_timeseries(dataset_name, target_name, ts_name=None, other_targets_as_covs=True, exclude_time_covariates=False, verbose=False):
    """
    Loads a time series dataset, prints descriptions, and returns pandas dataframe.

    Args:
        dataset_name (str): The name of the dataset (without the .csv extension).
        target_name (str): The name of the target column.
        ts_name (str, optional): The name of the time series if more than one is given in dataset. Defaults to None.
        other_targets_as_covs (bool, optional): If True, adds targets except of "target_name" as past covariates.
        exclude_time_covariates (bool, optional): If True, removes time-related covariates. Defaults to False.
        verbose (bool, optional): If True, prints the dataset description. Defaults to True.

    Returns:
        pandas.DataFrame: The loaded dataframe with the time series.
    """

    table_df = pd.read_csv(DATASET_INFO_PATH, sep=';')

    dataset_info = table_df[table_df["name"] == dataset_name].iloc[0]

    file_path = f"{DATASET_DIR_PATH}/{dataset_name}.csv"
    try:
        df = pd.read_csv(file_path, sep=';')

    except FileNotFoundError:
        return f"Error: Dataset '{dataset_name}' not found at path '{file_path}'"

    targets = eval(dataset_info['targets'])
    past_covariates = eval(dataset_info['past_covariates'])
    future_covariates = eval(dataset_info['future_covariates'])
    categorical_covariates = eval(dataset_info['categorical_covariates'])

    if target_name not in targets:
        return f"Error: Target '{target_name}' not in the target list"
    
    other_targets = [target for target in targets if target != target_name]
    if other_targets_as_covs:
        past_covariates.extend(other_targets)
    else:
        df.drop(columns=other_targets, inplace=True)

    if ts_name:
        ts_column = dataset_info['ts_column']
        if ts_name not in df[ts_column].unique():
            return f"Error: Time series name '{ts_name}' not in dataset column {ts_column}"
        df = df[df[ts_column] == ts_name]

    time_covariates =  ["minute", "hour", "weekday", "monthday", "week", "month", "quarter", "year"]
    if exclude_time_covariates:
        cols_to_drop = [col for col in df.columns if col in time_covariates]
        df.drop(columns=cols_to_drop, inplace=True)

    if verbose:
        print(f"Dataset: {dataset_name}")
        print(f"Target: {target_name}")
        print("\nCovariates:")

        if past_covariates:
            print(f"  Past Covariates: {past_covariates}")
        if future_covariates:
            print(f"  Future Covariates: {future_covariates}")
        if categorical_covariates:
            print(f"  Categorical Covariates: {categorical_covariates}")

    return df

