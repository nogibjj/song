Individual Project 1 (Data Engineering Systems)

# Objective
This project is to run big data on Dask using a Pandas API so as to work with the dataset in the workspace. The raw file of datasets are saved in "datasets" directory.

# Contents
1. Build a git repo: nogibjj/song

2. Scaffolding
- README.md
- Makefile
- requirements.txt
- .gitignore
- LICENSE
- project1.py
- test_project1.py

3. Load datasets
- Bicycle Dataset: bike_test.csv, bike_train.csv
- NFL Dataset: nfl.csv

4. Exploratory Data Analysis
- bike.ipynb: using Jupyter Notebook

5. Run big data on Dask using a Pandas API
- nfl.py
- dask_nfl.py

6. Streamlit
- streamlit_nfl.py

7. Hook up to FastAPI
- test_fast_api.py

# Dataset
1. Bicycle (provided by Kaggle)
- This dataset provides hourly rental data spanning two years.
- The training set is comprised of the first 19 days of each month.
- The test set is the 20th to the end of the month.

2. NFL Players (provided by Kaggle)
- This dataset provides 43,540 images of dimension 64x64 representing NFL players with their jersey numbers potentially visible.
- Due to the process, the dataset may be slightly noisy.
- Images were only extracted once every 20 frames to avoid having images that are too similar.

# Variables
1. Bicycle Dataset
- datetime: hourly date + timestamp  
- season:  1 = spring, 2 = summer, 3 = fall, 4 = winter 
- holiday: whether the day is considered a holiday
- workingday: whether the day is neither a weekend nor holiday
- weather: 1: Clear, Few clouds, Partly cloudy, Partly cloudy 
           2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist 
           3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds 
           4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog 
- temp: temperature in Celsius
- atemp: "feels like" temperature in Celsius
- humidity: relative humidity
- windspeed: wind speed
- casual: number of non-registered user rentals initiated
- registered: number of registered user rentals initiated
- count: number of total rentals

2. NFL Dataset
- filename: full filename of the image
- video_frame: video frame name in the same format as the original dataset
- player: groundtruth with the team and jersey number of the player in the image
- label: jersey number of the player in the image
- left: left of the original bounding box
- top: top of the original bounding box
- right: right of the original bounding box
- bottom: bottom of the original bounding box
- filepath: full path to the image

