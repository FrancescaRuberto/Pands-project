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