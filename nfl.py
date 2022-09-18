import pandas as pd
import dask.dataframe as dd


def pandas_load_nfl(location="datasets/nfl.csv"):
    """Load the nfl dataset into a pandas dataframe
    Assumes the dataset is in the datasets folder in the root of the project
    """
    return pd.read_csv(location)


def pandas_print_nfl(location="datasets/nfl.csv", record_number=0):
    """Display the nfl dataset
    print and returns a single nfl player number from the nfl dataset
    """

    df = pd.read_csv(location)
    record = df["player"][record_number]
    print(record)
    return record


def dask_query_nfl(location="datasets/nfl.csv"):
    """Query the nfl dataset
    Assumes the dataset is in the datasets folder in the root of the project
    """

    ddf = dd.read_csv(location, blocksize=None)
    return ddf