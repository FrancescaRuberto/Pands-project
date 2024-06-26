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
df = pd.read_csv("iris_dataset.csv")

# Now I generate histograms for each variable and I save them as PNG
# For each column in the dataset
for column in df.columns:
    # Plot an histogram in the current column
    # I added the bins, the fill color, and also the edge color
    plt.hist(df[column], bins=10, color='skyblue', edgecolor='black')
    #I set the title of the plot with the name of the column
    plt.title(f'Histogram of {column}')
    # I labelled x axis
    plt.xlabel('Value')
    # I labelled y axis
    plt.ylabel('Frequency')
    # I gave the input to save the plots as image
    # I set the image name as their title
    plt.savefig(f'{column}_histogram.png')
# Since I was having overlapping issues I added plt.close
# In this ways I should prevent overlaps 
    plt.close()



#I procede my examination with a correlation analysis
#I import pandas that help me with data analysis
import pandas as pd
#I reload the dataset
df = pd.read_csv("iris_dataset.csv")

#I first calulate the correlation between sepal lenght and width
sepal_lenght = df["sepal_lenght"]
sepal_width = df["sepal_width"]
#Now I calculate the correlation between petal lenght and petal width
petal_lenght = df["petal_lenght"]
petal_width = df["petal_width"]
#Now I calculate correlation between sepal and petal lenght
sepal_lenght = df["sepal_lenght"]
petal_lenght = df["petal_lenght"]
#Now I calculate correlation between sepal and petal width
sepal_width = df["sepal_width"]
petal_width = df["petal_width"]

#I calculate the correlation coefficient of each couple of variables I took
correlation_sepals = sepal_lenght.corr(sepal_width)
correlation_petals = petal_lenght.corr(petal_width)
correlation_sepal_petal_lenght = sepal_lenght.corr(petal_lenght)
correlation_sepal_petal_width = sepal_width.corr(petal_width)

#I print the results of the correlation coefficient for each couple of variables
print("Correlation coefficient between sepal lenght and width: ", correlation_sepals)
print("Correlation coefficient between petal lenght and width: ", correlation_petals)
print("Correlation coefficient between sepal and petal lenght: ", correlation_sepal_petal_lenght)
print("Correlation coefficient between sepal and petal width: ", correlation_sepal_petal_width)


# Now, I would like to conclude my analysis by plotting some scatter variables
# So we can have a visual and clearer visualization of relations between varibales in the dataset
# Let's output a scatter plot of each pair of variables
# I re-import the dataset
df = pd.read_csv("dataset_iris.csv")

# I use the loop function to examinate couples in the dataset 
# In this way I can create a plot for each couple of varibales
for col1 in df.columns:  #For each column in the dataset # I use for instead of while because I know the exact number of variables I want to iterate
    for col2 in df.columns: # Again for each column, in order to avoid overlapping and creating the plot with the same variable (inner loop)
        if col1 != col2: # After a couple of attempts, I understood that I have to make sure that I am not creating a plot of a varible with itself. 
            plt.scatter(df[col1], df[col2], color='blue')  # Create scatter plot
            plt.xlabel(col1)  # I label the x axis
            plt.ylabel(col2)  # I label the y axis
            plt.title(f'Scatter plot of {col1} vs {col2}')  # I add the plot title
            plt.show()  # Lastly, I show the plot    
