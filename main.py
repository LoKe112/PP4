import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_processed_df(path: str) -> pd.DataFrame:
    """read csv file and create dataframe
    Args:
      path: path to dataset
    Returns:
      Dataframe
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
    """Filtering std deviation
    Args:
      df: Dataframe with original values
      std_deviation: std deviation
    Returns:
      Dataframe with deviation
    """
    return df[df["StdDeviation"] >= std_deviation]

def date_filtration(df: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    """Filtering by date
    Args:
      df: Dataframe with original values
      start_date: date_from
      end_date: End date_to
    Returns:
      Dataframe with days that range [date_from; date_to]
    """
    start_date = pd.to_datetime(start_date, format='%Y-%m-%d')
    end_date = pd.to_datetime(end_date, format='%Y-%m-%d')
    return df[(start_date <= df["Date"]) & (df["Date"] <= end_date)]
  
def group_by_month_with_average_value(df: pd.DataFrame) -> pd.Series:
    """Grouping by month with calculation of the average value
    Args:
      df: Dataframe with original values
      
    Returns:
      A series indicating the average value for all months
    """
    
    return df.groupby(df.Date.dt.month)["Value"].mean()
  
def show_value_graph(df: pd.DataFrame) -> None:
    """Show of the value for the entire period
    Args:
      df: Dataframe with original values
      
    """
   
    fig = plt.figure(figsize=(19, 5))
    plt.ylabel("Value")
    plt.xlabel("date")
    plt.title('Курс долара(американские горки в конце)')
    plt.plot(df["Date"], df["Value"], color='blue',
                linestyle='-', linewidth=1)
    plt.show()
    
def show_value_graph_median_average(df: pd.DataFrame, month: int) -> None:
    """Showing graph for the specified month
    Args:
      df: Dataframe with original values
      month: The month for which the temperature graph is drawn
      
    """
    month_df = df[(df.Date.dt.month == month)]
    fig = plt.figure(figsize=(18, 8))

    fig.add_subplot(1, 3, 1)
    plt.ylabel("Value")
    plt.xlabel("date")
    plt.plot(month_df.Date.dt.day, month_df["Value"],
             color='blue', linestyle='--', linewidth=2, label='Value')
    plt.axhline(y=month_df["Value"].mean(
    ), color='orange', label="Average value")
    plt.axhline(y=month_df["Value"].median(
    ), color='black', label="Median")
    plt.legend(loc=2, prop={'size': 8})


def show_value_graph_median_average_year(df: pd.DataFrame, month: int, year: int) -> None:
    """Showing graph for the specified month
    Args:
      df: Dataframe with original values
      month: The month for which the temperature graph is drawn
      
    """
    month_df = df[(df.Date.dt.month == month) & (df.Date.dt.year == year)]
    fig = plt.figure(figsize=(18, 8))

    fig.add_subplot(1, 3, 1)
    plt.ylabel("Value")
    plt.xlabel("date")
    plt.plot(month_df.Date.dt.day, month_df["Value"],
             color='blue', linestyle='--', linewidth=2, label='Value')
    plt.axhline(y=month_df["Value"].mean(
    ), color='orange', label="Average value")
    plt.axhline(y=month_df["Value"].median(
    ), color='black', label="Median")
    plt.legend(loc=2, prop={'size': 8})
    

    plt.show()

df = get_processed_df("dataset.csv")
      

print(get_processed_df("dataset.csv"))

print(get_statistical_info(df, "Value"))
print(get_statistical_info(df, "MedianDeviation"))
print(get_statistical_info(df, "StdDeviation"))
print(std_deviation_filtration(df, 25))
print(date_filtration(df, "2021-11-11", "2021-11-22"))
print(group_by_month_with_average_value(df))