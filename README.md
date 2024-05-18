# Understanding the Iris Flower Dataset: Basic Data Analysis and Visualization

![Iris Dataset](https://media.licdn.com/dms/image/D5612AQF9X65-BxcKlQ/article-cover_image-shrink_720_1280/0/1659902345087?e=1719446400&v=beta&t=OPwmr3n5GD1rH2psvv2EkgVlc-uxULYb7_4H0_blZtk)

## Table of Contents

1. [Introduction](#introduction-to-iris-flower-dataset)
  - 1.1 [References](#references) 
2. [Purpose](#purpose-of-this-repository)
3. [Variable summary](#summarizing-variables-outputted-as-text-file)
  - 3.1 [References](#references-1)
4. [Exploring data through histograms](#visual-analysis-1-exploring-data-through-histograms)
  - 4.1 [Observations on histograms](#observations)
  - 4.2 [References](#references-2)
5. [Correlation analysis](#understanding-variable-correlations)
  - 5.1 [Observations on correlation](#observations-1)
  - 5.2 [References](#references-3)
6. [Exploring data relation through scatter plots](#visual-analysis-2-exploring-data-through-scatter-plots)
  - 6.1 [Observations on scatter plots](#observations-2)
  - 6.2 [References](#references-4)
7. [Conclusion](#conclusion)
8. [References](#referencesliterature)


## Introduction to Iris Flower Dataset
The Iris dataset is considered multivariate, indicating that it comprises an analysis object inherently consisting of at least two components. Introduced in 1936 by the British statistician, mathematician, and biologist Ronald Fisher, this dataset includes 150 instances of Iris flowers classified into three species: Iris Setosa, Iris Virginica, and Iris Versicolor. Within the dataset, four variables are taken into account: petal length, petal width, sepal length, and sepal width. This dataset is extensively utilized in statistical and machine learning analyses.

#### References 
- Bozkus, E. (December 2022). Exploring the Iris Flower Dataset. Medium. [Retrieved here](https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c)
- Cui, Y. (April 2020). The Iris Dataset - A little bit of history and biology. Published in: Towards Data Science. [Retrieved here](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)
- Rouse, M. (August 2017). Iris Flower Data Set. Technopedia. [Retrieved here](https://www.techopedia.com/definition/32880/iris-flower-data-set)
- Fisher, R.A. (1936). The use of multiple meaurements in taxonomic problems. Annual Eugenics, vol. 7, n. 2. [Retrieved here](https:/onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1469-1809.1936.tb02137.x)
- Fisher, R. A.. (1988). Iris. UCI Machine Learning Repository.[Retrieved here](https://doi.org/10.24432/C56C76).
- panData. (2023). "Unveiling the mysteries of the Iris dataset: A comprehensive analysis and Machine Learning Classification." [Retrieved here](https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d)

## Purpose of this repository
The goal of this repository is to conduct a basic analysis of the well-known Iris Flower Dataset. The aim is to provide an analysis that is both informative and illustrative, which will be divided into different steps. The initial step involves creating a concise summary of the variables, with the program outputting the results as a text file to facilitate readability. To enhance comprehension and visualization, histograms and scatter plots of each variable will accompany a brief analysis. Additionally, a series of other useful analyses will be performed.

## Summarizing variables (outputted as text file)
This part of the code aims to provide a summary of the Iris flower dataset variables as its first step. The summary is outputted as a text file to facilitate reading and interpretation.
By importing pandas, the dataset file can be easily read and manipulated, enabling efficient data analysis. The summarize_variables() function is defined to achieve this purpose.
Within the function, the dataset is loaded using pandas' read_csv() function, and a text file is opened using Python's built-in open() function. In my Iris dataset analysis project, I've mastered the use of Python's open() function, pivotal in my code. After thorough research, I've learned to employ this function for text file operations, facilitating the creation of a summary file for Iris dataset variables. The summary statistics of each variable in the dataset are calculated using the describe() function from pandas, which generates descriptive statistics.

Based on the provided summary, it's evident that the dataset contains information about the dimensions of sepals and petals of Iris flowers. The summary provides statistical measures such as mean, standard deviation, minimum, maximum, and quartiles for each variable. From this summary, we can collect insights about the range, distribution, and central tendency of each variable, providing valuable information for further analysis and interpretation.

#### References
- Anis, A. (April 2022). 5 different ways to load data in Python. KDnuggets.com. [Retrieved here](https://www.kdnuggets.com/2020/08/5-different-ways-load-data-python.html)
- Cloud, S. (July 2023). Python: Display All Columns of a Pandas DataFrame in '.describe()'. SaturnCloud.io. [Retrieved here](https://saturncloud.io/blog/python-spyder-display-all-columns-of-a-pandas-dataframe-in-describe/#:~:text=describe()%20method%20in%20Pandas,and%20maximum%20of%20the%20columns.)
- Dogan, A. (August 2021). 5 ways to load datasets in Python. Published in: Python in Plain English. [Retrieved here](https://python.plainenglish.io/5-ways-to-load-datasets-in-python-2ca28101a345)
- Fagbuyiro, D. (August 2022). File handling in Python - How to create, read, and write to a file. FreeCodeCamp.org. [Retrieved here](https://www.freecodecamp.org/news/file-handling-in-python/)
- Mertz, J. (February 2019). Reading and Writing Files in Python (Guide). Realpython.com. [Retrieved here](https://realpython.com/read-write-files-python/)
- (February 2024). Print the content of a txt file in Python. Geeksforgeeks.org. [Retrieved here](https://www.geeksforgeeks.org/print-the-content-of-a-txt-file-in-python/)
- (December 2023). Reading and writing to txt files in Python. Geeksforgeeks.org.[Retrieved here](https://www.geeksforgeeks.org/reading-writing-text-files-python/)
- (n.a). pandas.DataFrame.describe. Pandas.pydata.org. [Retrieved here](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
- (n.d.). How to Write in Text File Using Python. Javapoint.com. [Retrieved here](https://www.javatpoint.com/how-to-write-in-text-file-using-python#:~:text=The%20write()%20function%20is,in%20the%20file%20at%20once.&text=The%20writelines()%20function%20can,the%20set%20of%20strings%2C%20etc.)


## Visual analysis 1: exploring data through histograms
The second step of this analysis consisted in building histograms for each variable in the Iris dataset. The creation of these plots help us visualizing the distribution of values inside the dataset, and also in understanding the frequency of occurrence of each variable. 
In order to complete this task, I first imported matplotlib.pyplot library, that is an extremely useful library that provides tools for the creation of plots and it is widely used in data analytics. 
Next, I gothrough each column in the dataset. For each colum I:
- Plotted an histogram, specifying the number of bins, the fill color, and edge color. 
- Set the title of the plot to reflect the variable being visualized (I gave as title to each histogram the name of the variable showed).
- I labelled the axes in order to give context to the plot. 
- I saved each histogram as PNG file, naming it by reflecting the title given. 
- Lastly, I used plt.close() to close the plot. I decided to use it since I was having overlapping issues. In this way, I avoid such issues.

### Observations
 The histograms provide valuable insights into the distribution of each variable within the Iris dataset. They help us understand the range of values, identify potential outliers, and discern any patterns or clusters that may exist within the data.

- Sepal Length Histogram: the histogram for shows an overal normal distribution, with a number of different peaks, and the highest frequency of the sepal is between 5.0 and 6.5.
- Sepal Width Histogram: the histogram shows an frequency between 3.0 and 3.5 with a quite evident central peak compared to sepal lenght 
- Petal Length Histogram: the histogram for petal length reveals clear distinctions between different species. There are multiple peaks or clusters, and the highest frequency is between 1.0 and 1.5. The plot seems suggesting that a specic cluster has smaller petals than others.
- Petal Width Histogram: similar to the petal length  the petal width histogram also shows distinct clusters. As per petal lenght, also in this case the plot seems suggesting that there is a cluster with tighter than others. The highest frequency recorded is between 0.0 and 0.5.

#### References
- Alexandru, D. (n/a). "Simple Analysis of Iris Dataset." Kaggle. [Retrieved here](https://www.kaggle.com/code/danalexandru/simple-analysis-of-iris-dataset)
- Angela1C. (n/a). "Investigating the Iris Dataset." Angela1C. [Retrieved here](https://www.angela1c.com/projects/iris_project/investigating-the-iris-dataset/)
- GeeksforGeeks. (n/a). "Box Plot and Histogram Exploration on Iris Data." GeeksforGeeks. [Retrieved here](https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/)
- Tutorialspoint. (n/a). "How to Save a Histogram Plot in Python." Tutorialspoint. [Retrieved here](https://www.tutorialspoint.com/how-to-save-a-histogram-plot-in-python)
- Welch, AJ., (n/a). "How to Save a Plot to a File Using Matplotlib." Atlassian. [Retrieved here](https://www.atlassian.com/data/notebook/how-to-save-a-plot-to-a-file-using-matplotlib)

## Understanding Variable Correlations
Correlation analysis is a statistical technique used to measure the strength and direction of the relationship between two variables. It helps in understanding how changes in one variable are associated with changes in another. In order to calculate and then analyse correlation coefficient for couples of choosen variables, I took the following steps:

- I imported the pandas library to facilitate data analysis and loaded the dataset.
- I selected pairs of variables for correlation analysis: sepal length and width, petal length and width, sepal length and petal length, and sepal width and petal width.
- For each pair of variables, I calculated the correlation coefficient using the .corr() method provided by pandas.
- Finally, I printed the correlation coefficients for each pair of variables to observe their relationships.

By performing correlation analysis, I aimed to understand the degree of association between different features of the iris dataset. This analysis helps in gaining insights into the dataset's structure and understanding how variables may influence each other.

### Observations
From the correlation matrix, we can draw some conclusions about the relationships between variables in the Iris dataset:

- Correlation coefficient between sepal length and width: The coefficient (-0.117) suggests a weak negative correlation between sepal length and width. This means that there's a slight tendency for sepals with longer lengths to have slightly narrower widths, but the relationship is not very strong.
- Correlation coefficient between petal length and width: With a coefficient of 0.963, there's a strong positive correlation between petal length and width. This indicates that as petal length increases, petal width tends to increase as well, and vice versa.
- Correlation coefficient between sepal and petal length: The coefficient (0.872) indicates a strong positive correlation between sepal and petal length. This means that there's a noticeable tendency for flowers with longer sepals to also have longer petals, and vice versa.
- Correlation coefficient between sepal and petal width: With a coefficient of -0.366, there's a weak negative correlation between sepal and petal width. This suggests that while there may be some tendency for flowers with wider sepals to have slightly narrower petals, the relationship is not very strong.

#### References
- BMJ. (n/a). "11. Correlation and regression." BMJ. [Retrieved here]( https://www.bmj.com/about-bmj/resources-readers/publications/statistics-square-one/11-correlation-and-regression)
- Brownlee, J. (November 2023). "How to Use Correlation to Understand the Relationship Between Variables." Machine Learning Mastery. [Retrieved here](https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/)
- Canales Luna, J. (February 2022). Python Details on Correlation Tutorial. DataCamp. [Retrieved here](https://www.datacamp.com/tutorial/tutorial-datails-on-correlation)
- Field, A. (2018). Discovering Statistics Using IBM SPSS Statistics (Fifth Edition). Sage Publications Ltd.
- Schober, P., Boer, C., & Schwarte, L. A. (n/a). Correlation Coefficients: Appropriate Use and Interpretation.
- Stojiljković, M. (2019, December 23). NumPy, SciPy, and pandas: Correlation With Python. Real Python. [Retrieved here](https://realpython.com/numpy-scipy-pandas-correlation-python/)

## Visual analysis 2: exploring data through scatter plots
After analyzing the correlation coefficient of the four pairs of variables in the Iris dataset, I believe that visualizing the relationships through scatter plots will provide valuable insights. Therefore, I proceeded to create a scatter plot for each pair of variables in the dataset. These scatter plots are valuable for visualizing the relationships between different variables and identifying potential patterns or correlations.

To accomplish this, I utilized a loop to go through each pair of variables in the dataset. For each pair of variables, I performed the following steps:

- Created a scatter plot using plt.scatter(), with one variable represented on the x-axis and the other on the y-axis.
- Set the x-axis and y-axis labels to reflect the variables being visualized.
- Assigned a title to each plot indicating the variables being compared.
- Displayed each scatter plot using plt.show().

It's worth mentioning that I encountered a challenge in ensuring that each scatter plot displayed unique variable combinations and avoided plotting a variable against itself. To address this, I implemented a conditional check within the loop to skip cases where the same variable was being compared. This solution was inspired by a code snippet I found on Stack Overflow (1), which helped me overcome the issue effectively.

(1) How to make a loop for multiple scatterplots in python?. Stack Overflow.[Linke here](https://stackoverflow.com/questions/56974174/how-to-make-a-loop-for-multiple-scatterplots-in-python)

### Observations
Overall, the scatter plots offer valuable insights into the relationships between different variables in the Iris dataset, aiding in the exploration and analysis of the data. Some other useful insights we can extract from the scatter plots:

- Sepal Width vs Petal Length:
From the scatter plot, there seems to be a slight tendency for flowers with longer petals to have slightly greater sepal width. However, the dispersion of points indicates significant variation within each species.: from the scatter plot, there seems to be a slight tendency for flowers with longer petals to have slightly greater sepal width. However, we may have significant variation within each species.
- Sepal Length vs Petal Width:
The scatter plot in this case seems suggestic a positiva realtion between sepal lenght and petal width. Theoretically, this means that as sepal lenght increase, there tends to be a greater petal width.

#### References
- GeeksforGeeks. (n/a). Python Nested Loops. GeeksforGeeks. [Retrieved from](https://www.geeksforgeeks.org/python-nested-loops/)
- PyNative. (Updated on: September 2021). Python Nested Loops. PyNative. [Retrieved here](https://pynative.com/python-nested-loops/)
- Gruppetta, S., (May 2021). "Visualizing Python plt.scatter().". Real Python. [Retrieved from](https://realpython.com/visualizing-python-plt-scatter/)
- User: andrej. (2019). How to make a loop for multiple scatterplots in Python?. Stack Overflow.[Retrieved from](https://stackoverflow.com/questions/56974174/how-to-make-a-loop-for-multiple-scatterplots-in-python)
- W3Schools. (n/a). Matplotlib scatter plot. [Retrieved from](https://www.w3schools.com/python/matplotlib_scatter.asp)

## Conclusion 
Through the analysis of the Iris Flower Dataset, we've gained valuable insights into the characteristics and relationships within the dataset. Here are some key conclusions drawn from the analysis:

Variable Summarization: By summarizing the variables in the dataset, we obtained descriptive statistics such as mean, standard deviation, minimum, maximum, and quartiles for each variable. This provided a comprehensive overview of the dataset's structure and distribution.
Visual Analysis 1 - Histograms: The histograms helped us visualize the distribution of each variable. We observed distinct patterns and clusters within the data, providing insights into the frequency and range of values for each variable.
Understanding Variable Correlations: By calculating correlation coefficients between pairs of variables, we gained insights into the relationships within the dataset. These correlations revealed both strong and weak associations between different features of Iris flowers, such as sepal length and width, petal length and width, and combinations thereof.
Visual Analysis 2 - Scatter Plots: The scatter plots further elucidated the relationships between variables by providing visual representations of their associations. We observed patterns and trends within the data, such as positive and negative correlations between sepal and petal dimensions.
Overall, this analysis deepened our understanding of the Iris Flower Dataset and highlighted the interplay between its variables. These insights can be invaluable for various applications, including species classification, botanical research, and machine learning model development. Through continued exploration and analysis, further insights and discoveries can be made, contributing to our understanding of this classic dataset and its implications in various fields.

## References/Literature
- Alexandru, D. (n/a). "Simple Analysis of Iris Dataset." Kaggle. [Retrieved here](https://www.kaggle.com/code/danalexandru/simple-analysis-of-iris-dataset)
- Angela1C. (n/a). "Investigating the Iris Dataset." Angela1C. [Retrieved here](https://www.angela1c.com/projects/iris_project/investigating-the-iris-dataset/)
- Anis, A. (April 2022). 5 different ways to load data in Python. KDnuggets.com. [Retrieved here](https://www.kdnuggets.com/2020/08/5-different-ways-load-data-python.html)
- BMJ. (n/a). "11. Correlation and regression." BMJ. [Retrieved here](https://www.bmj.com/about-bmj/resources-readers/publications/statistics-square-one/11-correlation-and-regression)
- Bozkus, E. (December 2022). Exploring the Iris Flower Dataset. Medium. [Retrieved here](https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c)
- Brownlee, J. (November 2023). "How to Use Correlation to Understand the Relationship Between Variables." Machine Learning Mastery. [Retrieved here](https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/)
- Cloud, S. (July 2023). Python: Display All Columns of a Pandas DataFrame in '.describe()'. SaturnCloud.io. [Retrieved here](https://saturncloud.io/blog/python-spyder-display-all-columns-of-a-pandas-dataframe-in-describe/#:~:text=describe()%20method%20in%20Pandas,and%20maximum%20of%20the%20columns.)
- Cui, Y. (April 2020). The Iris Dataset - A little bit of history and biology. Published in: Towards Data Science. [Retrieved here](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)
- Dogan, A. (August 2021). 5 ways to load datasets in Python. Published in: Python in Plain English. [Retrieved here](https://python.plainenglish.io/5-ways-to-load-datasets-in-python-2ca28101a345)
- Fagbuyiro, D. (August 2022). File handling in Python - How to create, read, and write to a file. FreeCodeCamp.org. [Retrieved here](https://www.freecodecamp.org/news/file-handling-in-python/)
- Field, A. (2018). Discovering Statistics Using IBM SPSS Statistics (Fifth Edition). Sage Publications Ltd.
- Fisher, R.A. (1936). The use of multiple measurements in taxonomic problems. Annual Eugenics, vol. 7, n. 2. [Retrieved here](https:/onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1469-1809.1936.tb02137.x)
- Fisher, R. A.. (1988). Iris. UCI Machine Learning Repository.[Retrieved here](https://doi.org/10.24432/C56C76.)
- GeeksforGeeks. (n/a). Python Nested Loops. GeeksforGeeks. [Retrieved here](https://www.geeksforgeeks.org/python-nested-loops/)
- GeeksforGeeks. (n/a). "Box Plot and Histogram Exploration on Iris Data." GeeksforGeeks. [Retrieved here](https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/)
- Gruppetta, S., (May 2021). "Visualizing Python plt.scatter().". Real Python. [Retrieved here](https://realpython.com/visualizing-python-plt-scatter/)
- Mertz, J. (February 2019). Reading and Writing Files in Python (Guide). Realpython.com. [Retrieved here](https://realpython.com/visualizing-python-plt-scatter/)
- panData. (2023). "Unveiling the mysteries of the Iris dataset: A comprehensive analysis and Machine Learning Classification." [Retrieved here]https://levelup.gitconnected.com/unveiling-the-mysteries-of-the-iris-dataset-a-comprehensive-analysis-and-machine-learning-f5c4f9dbcd6d)
- PyNative. (Updated on: September 2021). Python Nested Loops. PyNative. [Retrieved here](https://pynative.com/python-nested-loops/)
- Rouse, M. (August 2017). Iris Flower Data Set. Technopedia. [Retrieved here](https://www.techopedia.com/definition/32880/iris-flower-data-set)
- Schober, P., Boer, C., & Schwarte, L. A. (n/a). Correlation Coefficients: Appropriate Use and Interpretation.
- Stojiljković, M. (2019, December 23). NumPy, SciPy, and pandas: Correlation With Python. Real Python. [Retrieved here](https://realpython.com/numpy-scipy-pandas-correlation-python/)
- Tutorialspoint. (n/a). "How to Save a Histogram Plot in Python." Tutorialspoint. [Retrieved here](https://www.tutorialspoint.com/how-to-save-a-histogram-plot-in-python)
- User: andrej. (2019). How to make a loop for multiple scatterplots in Python?. Stack Overflow. [Retrieved from](https://stackoverflow.com/questions/56974174/how-to-make-a-loop-for-multiple-scatterplots-in-python)
- Welch, AJ., (n/a). "How to Save a Plot to a File Using Matplotlib." Atlassian. [Retrieved here](https://www.atlassian.com/data/notebook/how-to-save-a-plot-to-a-file-using-matplotlib)
- W3Schools. (n/a). Matplotlib scatter plot. [Retrieved from](https://www.w3schools.com/python/matplotlib_scatter.asp)

##
End