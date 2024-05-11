# Understanding the Iris Flower Dataset: Basic Data Analysis and Visualization

![Iris Dataset](https://media.licdn.com/dms/image/D5612AQF9X65-BxcKlQ/article-cover_image-shrink_720_1280/0/1659902345087?e=1719446400&v=beta&t=OPwmr3n5GD1rH2psvv2EkgVlc-uxULYb7_4H0_blZtk)

## Introduction to Iris Flower Dataset
The Iris dataset is considered multivariate, indicating that it comprises an analysis object inherently consisting of at least two components. Introduced in 1936 by the British statistician, mathematician, and biologist Ronald Fisher, this dataset includes 150 instances of Iris flowers classified into three species: Iris Setosa, Iris Virginica, and Iris Versicolor. Within the dataset, four variables are taken into account: petal length, petal width, sepal length, and sepal width. This dataset is extensively utilized in statistical and machine learning analyses.

## Purpose of this repository
The goal of this repository is to conduct a basic analysis of the well-known Iris Flower Dataset. The aim is to provide an analysis that is both informative and illustrative, which will be divided into different steps. The initial step involves creating a concise summary of the variables, with the program outputting the results as a text file to facilitate readability. To enhance comprehension and visualization, histograms and scatter plots of each variable will accompany a brief analysis. Additionally, a series of other useful analyses will be performed.

### Summarizing variables (outputted as text file)
This part of the code aims to provide a summary of the Iris flower dataset variables as its first step. The summary is outputted as a text file to facilitate reading and interpretation.
By importing pandas, the dataset file can be easily read and manipulated, enabling efficient data analysis. The summarize_variables() function is defined to achieve this purpose.
Within the function, the dataset is loaded using pandas' read_csv() function, and a text file is opened using Python's built-in open() function. In my Iris dataset analysis project, I've mastered the use of Python's open() function, pivotal in my code. After thorough research, I've learned to employ this function for text file operations, facilitating the creation of a summary file for Iris dataset variables. The summary statistics of each variable in the dataset are calculated using the describe() function from pandas, which generates descriptive statistics.

Based on the provided summary, it's evident that the dataset contains information about the dimensions of sepals and petals of Iris flowers. The summary provides statistical measures such as mean, standard deviation, minimum, maximum, and quartiles for each variable. From this summary, we can collect insights about the range, distribution, and central tendency of each variable, providing valuable information for further analysis and interpretation.

### Visual analysis 1: exploring data through histograms
The second step of this analysis consisted in building histograms for each variable in the Iris dataset. The creation of these plots help us visualizing the distribution of values inside the dataset, and also in understanding the frequency of occurrence of each variable. 
In order to complete this task, I first imported matplotlib.pyplot library, that is an extremely useful library that provides tools for the creation of plots and it is widely used in data analytics. 
Next, I gothrough each column in the dataset. For each colum I:
- Plotted an histogram, specifying the number of bins, the fill color, and edge color. 
- Set the title of the plot to reflect the variable being visualized (I gave as title to each histogram the name of the variable showed).
- I labelled the axes in order to give context to the plot. 
- I saved each histogram as PNG file, naming it by reflecting the title given. 
- Lastly, I used plt.close() to close the plot. I decided to use it since I was having overlapping issues. In this way, I avoid such issues.

#### Observations
 The histograms provide valuable insights into the distribution of each variable within the Iris dataset. They help us understand the range of values, identify potential outliers, and discern any patterns or clusters that may exist within the data.

- Sepal Length Histogram: the histogram for shows an overal normal distribution, with a number of different peaks, and the highest frequency of the sepal is between 5.0 and 6.5.
- Sepal Width Histogram: the histogram shows an frequency between 3.0 and 3.5 with a quite evident central peak compared to sepal lenght 
- Petal Length Histogram: the histogram for petal length reveals clear distinctions between different species. There are multiple peaks or clusters, and the highest frequency is between 1.0 and 1.5. The plot seems suggesting that a specic cluster has smaller petals than others.
- Petal Width Histogram: similar to the petal length  the petal width histogram also shows distinct clusters. As per petal lenght, also in this case the plot seems suggesting that there is a cluster with tighter than others. The highest frequency recorded is between 0.0 and 0.5.

### Understanding Variable Correlations
Correlation analysis is a statistical technique used to measure the strength and direction of the relationship between two variables. It helps in understanding how changes in one variable are associated with changes in another. In order to calculate and then analyse correlation coefficient for couples of choosen variables, I took the following steps:

- I imported the pandas library to facilitate data analysis and loaded the dataset.
- I selected pairs of variables for correlation analysis: sepal length and width, petal length and width, sepal length and petal length, and sepal width and petal width.
- For each pair of variables, I calculated the correlation coefficient using the .corr() method provided by pandas.
- Finally, I printed the correlation coefficients for each pair of variables to observe their relationships.

By performing correlation analysis, I aimed to understand the degree of association between different features of the iris dataset. This analysis helps in gaining insights into the dataset's structure and understanding how variables may influence each other.