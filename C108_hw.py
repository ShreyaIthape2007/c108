import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics


file = pd.read_csv('data2.csv')

rating = file['Avg Rating'].tolist()

graph = ff.create_distplot([rating],['Average Ratings'])

mean=statistics.mean(rating)

print('The mean is ',mean)

graph.show()

