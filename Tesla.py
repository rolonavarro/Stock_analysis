# Import tesla data for the last two year Date(From: 04/07/2020 To: 04/07/2018)
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

# Read csv file. The making the date to be the index
df = pd.read_csv("DATA/TSLA.csv", parse_dates=True, index_col=0)

df['Adj Close'].plot()