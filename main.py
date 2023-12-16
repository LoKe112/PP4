import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_processed_df(path: str) -> pd.DataFrame:
    """read csv file and create dataframe
    Args:
      path: path to dataset
    Returns:
      Dataframe without NaN values and with the addition of the Fahrenheit temperature column
    """
    df = pd.read_csv(path, header=None)
    df.columns = ["Date",
                  "Value"]
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    if not ((df.isnull().sum()).eq(0).all()):
        df.dropna(inplace=True, ignore_index=True)
    curestd,curemean = df['Value'].std(),df['Value'].mean()
    df['MeanDeviation'] = curemean-df['Value']
    df['StdDeviation'] = curestd-df['Value']
    return df



print(get_processed_df("dataset.csv"))
