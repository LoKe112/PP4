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
    curestd,curemedian = df['Value'].mean(),df['Value'].median()
    df['MedianDeviation'] = abs(curemedian-df['Value'])
    df['StdDeviation'] = abs(curestd-df['Value'])
    return df

def get_statistical_info(df: pd.DataFrame, parametr: str) -> pd.Series:
    """Getting statistical information
    Args:
      df: Dataframe with original values
      parametr: column for statistic
    Returns:
      A series containing a statistical info
    """
    if parametr in df.columns:
        return df[parametr].describe()
      
def std_deviation_filtration(df: pd.DataFrame, std_deviation: float) -> pd.DataFrame:
    """Filtering by column temperature in degrees Celsius
    Args:
      df: Dataframe with original values
      celsius_temp: temperature in degrees Celsius
    Returns:
      Dataframe with days in which the temperature is not less than the set temperature
    """
    return df[df["StdDeviation"] >= std_deviation]

df = get_processed_df("dataset.csv")
      

print(get_processed_df("dataset.csv"))

print(get_statistical_info(df, "Value"))
print(get_statistical_info(df, "MedianDeviation"))
print(get_statistical_info(df, "StdDeviation"))
print(std_deviation_filtration(df, 25))
