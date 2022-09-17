from nfl import dask_query_nfl

ddf = dask_query_nfl()
print("One record from the nfl dataset without compute:")
print(ddf["player"][0])
print("One record from the nfl dataset with compute:")
print(ddf["player"][0].compute())