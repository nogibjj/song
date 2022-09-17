import pandas as pd
import dask.dataframe as dd


def pandas_load_news(location="datasets/news.csv"):
    """Load the news dataset into a pandas dataframe

    Assumes the dataset is in the datasets folder in the root of the project
    """
    return pd.read_csv(location)


def pandas_print_news(location="datasets/news.csv", record_number=0):
    """Display the news dataset

    print and returns a single news record from the news dataset
    """

    df = pd.read_csv(location)
    record = df["Summary"][record_number]
    print(record)
    return record


def dask_query_news(location="datasets/news.csv"):
    """Query the news dataset

    Assumes the dataset is in the datasets folder in the root of the project
    """

    ddf = dd.read_csv(location, blocksize=None)
    return ddf