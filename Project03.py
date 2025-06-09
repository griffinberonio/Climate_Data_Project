import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math 
import numpy as np 

# Project 3 Code:
def climatedata(path):
    df = pd.read_csv(path,
        parse_dates = ["DATE"],
        low_memory=False)
    df["DATE"] = pd.to_datetime(df['DATE'], format="%Y-%m-%dT%H:%M:%S")
    df["year"] = pd.to_datetime(df['DATE']).dt.year
    df['day'] = pd.to_datetime(df['DATE']).dt.day
    df['time'] = df['DATE'].dt.time
    return df.head()





if __name__ == "__main__":
    mainpath = r"C:\Users\griff\OneDrive\718\raw data\climate.csv" 
    # (^Madison climatological data)
    
    print('hello')
    print(climatedata(mainpath))