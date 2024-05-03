# The goal of this program is to provide a basic analysis of the famous Iris flower dataset
# The analysis will be through a number of steps aimed at providing valuable insights on the dataset.
# Author: Francesca Ruberto

# As first step we are going to summarize variables
# The summary will be outputted as text file to facilitate reading

# Importing pandas in order to read our dataset file
# by adding pandas we can easily maninupulate and analyse the data

import pandas as pd 

# I now define my new function
def summarize_variables (summary_output):
    # Let's upload our dataset
    df = pd.read_csv("iris_dataset.csv")

    # In order to start wiriting a txt I need to open it
    # To do so, I need to use the build in function open()
    # Two parameters to write this function: file name and mode specifying file access
    with open (summary_output, "w") as file:
        # Now I give instructions to write a summary
        # The summary contains the statistics of each variable in the file
        file.write("Summary of variables in Iris dataset\n\n") # NB we use \n\n to separates the text in different rows
        # Now we need to calculate our summary statistics 
        # To do do I use the pandas describe function
        # This is a basic pandas function that generates descriptive statistics
        summary = df.describe()
        # We need to make sure we write string to the summary
        file.write(str(summary))

# Call the summarize_variables function with the output file name
summarize_variables("summary.txt")

# Our second step consist in creating histograms of each variable
# I will save each histogram as png file
# I import matplotlib that will help me in creating the plot

import matplotlib.pyplot as plt 

# I upload the dataset with pandas
df = pd.read_csv("dataset_iris.csv")

# Now I generate histograms for each variable and I save them as PNG
# For each column in the dataset