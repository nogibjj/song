# Run server using command: uvicorn test_fast_api:app --reload
# FastAPI is the framework used to build APIs
# Uvicorn is the server that will use the API to serve requests

from fastapi import FastAPI

# creates instance of class FastAPI
# name of instance should be used in the command used to run uvicorn

app = FastAPI()

# path operation decorator - define path and http method
@app.get("/")
def root():
    # FastAPI takes care of serializing Python dict to JSON
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def get_item(item_id):
    item_id = int(item_id)
    items = ["apple", "orange", "banana", "mango"]

    if item_id in range(4):
        return {"item": items[item_id]}
    else:
        return {"item": "We only have four fruits"}