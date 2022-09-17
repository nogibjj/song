from news import dask_query_news

ddf = dask_query_news()
print("One record from the news dataset without compute:")
print(ddf["Summary"][0])
print("One record from the news dataset with compute:")
print(ddf["Summary"][0].compute())