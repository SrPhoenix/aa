import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# n = 4
# skip_func = lambda x: x%n != 0

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("results/GreedySearch.csv") 

# Extract the date and close price columns
vertices = df['Vertices']
edges = df['Edges'][0:-1:4]
operations = df['Operations']
time = df['Time'][0:-1:4]
attemps = df['Attemps'][0:-1:4]

# Create a line plot
plt.plot(vertices, np.log2(operations), linestyle ='dashed', marker = 'o', label = "Operations")

# Show the plot
plt.show()

