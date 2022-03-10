import plotly.figure_factory as ff
import pandas as pd 
import csv
 
df = pd.read_csv("projectdata.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist = True)
fig.show()