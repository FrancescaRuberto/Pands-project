# The goal of this program is to provide a basic analysis of the famous Iris flower dataset
# The analysis will be through a number of steps aimed at providing valuable insights on the dataset.
# Author: Francesca Ruberto

# As first step we are going to summarize variable
# The summary will be outputted as text file to facilitate reading

# Importing pandas in order to read our dataset file
# by adding pandas we can easily maninupulate and analyse the data

import pandas as pd 

# I now define my new function
def summarize_variables (summary_output):
    # Let's upload our dataset
    df = pd.read_csv("dataset_iris.csv")
