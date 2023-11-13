import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("report/ExhaustSearch.csv")

# Extract the date and close price columns
vertices = df['Vertices']
edges = df['Edges']
operations = df['Operations']
time = df['Time']

# Create a line plot
plt.scatter(vertices, time)

# Show the plot
plt.show()