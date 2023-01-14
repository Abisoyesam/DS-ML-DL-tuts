#!/usr/bin/env python
# coding: utf-8

# A quick recap of DAY3 discussions:
# 
# - Functions in Python 
#     - Defining a function 
#     - Passing Arguments
#     - Return values
#     - Passing a list
#     - Passing an arbitrary number of arguments 
# - Creating Modules and Storing your functions in Modules.
#     - Importing and renaming modules
#     - Accessing functions stored in modules
# - Lambda Expressions
# - Time and DateTime in Python 

# # ..................................................................................
# ### Tuesday, 14th April, 2020
# # ..................................................................................
# 

# - Python for Data Science and Machine Learning 
# - Modules and standard Python library
# - Data Science tools 
#     - Numpy
#     - Pandas
#     - Statsmodel
#     - Matplotlib
#     - Seaborn 

# ### Data Science
# 
# The amount of data in the world today has grown exponentially due availability of lots of sensors and data-storing technologies everywhere. Leveraging on such enormous information to drive actionable insights is now a source of competitive advantage. Working to drive these insights has ignited interest of many into the field.
# 
# ![image.png](ds.jpg)
#   
#                   **Data Science is multidisciplinary which combines Coding, Mathematics, Statistics and an expert area of                          application (e.g. Medicine, Finance, Agriculture, Security )**
#                   
# 
# **Data science** is a process of using data to understand the world. An attempt to work with data
# to find answers to questions. Data Science provide tools for:
# 
# - Data Extraction:
# 
# Data science is a field about processes and systems, to extract data of forms,whether it is an unstructured or structured form, from various sources
# 
# - Data Understanding:
# 
# Just like biological sciences are the study of biology; physical sciences, it's the study of physical reactions. Data is real, data has properties we need to study them to work on them.
# 
# - Story Telling:
# 
# Data science is the art of uncovering the insights and trends that are hiding behind data
# 
# - Decision / Policy Making:
# 
# With the insights uncovered from data, you can make strategic choices for an organization or institution.
# 
# 
# 
# ####  Data science is a not an act, it is a **science**, subjected to evolvement and change in steps. There is no consensus to how things are done, since the insight to be drawn depends solely on the data under consideration.

# ### Data could be 
# - structured
#     - More like tabular data that you're familiar with in Microsoft Excel format, it has rows and columns,
# - Unstructure
#     - Mostly gathered from web, where it's not arrange into rows and columns since it's text.
#     - Sometimes it's video and audio.
#    
#    **It might require a little bit more effort to get information out of unstructured data eg Web Scraping**

# #### The four Pillars of Data Science
# 1. Data Analysis — turning raw information into knowledge that can be acted upon.
#     - Domain knowledge — learn the business problem/question and understand accuracy vs cost trade-offs.
#     - Research — get the data, design experiments and conduct them (hypothesis testing).
#     - Interpretation — Summarize data, Do Visualization, and show insight from summaries.
#     
# 2. Data Modelling — machine learning, in order to estimate the data we wish we had.
#     - Supervised Learning — classification, regression, anomaly detection.
#     - Unsupervised Learning — clustering, dimensionality reduction, anomaly detection.
#     - Custom Algorithm Development — feature engineering, numerical optimization.
#     
# 3. Data Engineering — making everything work faster, more robustly and at greater scale.
#     - Data Management — database management, pipeline construction, data collection.
#     - Production — automation, system integration, “robustification”.
#     - Software Engineering — ensure maintainability, scaling, collaborative development.
#     
# 4. Data Wrangling — The dirty work of data
#     - Data Formatting — type conversion, string manipulation, fixing errors.
#     - Value Interpretation — dates and times, units of measurement, missing values.
#     - Data Handling — querying, slicing, joining.

# ### Data Science Career Roles
# 
# The demand for various data science roles is increasing by the day. The vast range of careers in the data 
# science industry is accompanied by an avalanche of job postings, with designation and descriptions used 
# loosely. Hence, there is a lot of confusion around who does what in the industry.
# 
# Here is an attempt to help clear some of the confusion. **Please note that this list is not exhaustive**
# - Data Analyst
# - Data Scientist
# - Data Engineer
# - Machine Learning Engineer
# - Data Architect
# - Business Intelligence Analyst
# - Statistician
# - Data Administrator
# 
# #### Data Analyst (‘Data Detective’)
# - Role:
#     - Collects, transforms, manipulate and process large data sets to suit the desired analysis of the company
# - Skills & Talent:
#     ▪ Spreadsheet tools (e.g. Excel)
#     ▪ Database systems (SQL and NO SQL based)
#     ▪ Data Cleaning
#     ▪ Data Visualization
#     ▪ Communication and Presentation
#     ▪ Probability and Statistics
# Rough global average salary: 
# $50,000 (USD) - $110,000
# 
# 
# #### Data Scientist
# - Role:
#     - Data scientists do many of the same things as data analysts, but they also typically build machine learning models to make accurate predictions about the future based on past data.
# - Skills & Talent:
#     - All of the skills required of data analyst, plus: 
#     - A solid understanding of both supervised and unsupervised machine learning models and methods
#     - A strong understanding of statistics and the ability to evaluate statistical models
#     - More advanced data-science-related programming skills in Python or R, and potentially familiarity with other tools like Apache Spark
# - Rough global average salary:
# $85,000 (USD) - $170,000
# 
# 
# #### Data Engineer
# - Role:
#     - Creates blueprints for data management systems to integrate,centralize, protect and maintain data sources. At a company with a data team, the data engineer might be responsible for building data pipelines to get the latest sales, marketing, and revenue data to data analysts and scientists quickly and in a usable format. They’re also likely responsible for building and maintaining the infrastructure needed to store and quickly access past data.
# - Skills & Talent:
#     - Data warehousing solutions
#     - In-depth knowledge of database architecture
#     - Extraction Transformation and Load (ETL), spreadsheet and BI tools
#     - Data modelling
#     - Data APIs
#         
# - Rough global average salary:
# $70,000 (USD) - $165,000
# 
# ![image.png](oppor.jpg)
# ![image.png](oppor1.jpg)

# ### Data Science Tools and Libraries in Python
# 
# - [NUMPY](https://numpy.org/): An extensive collection of high-level mathematical functions and implemented methods to make processing large multidimensional arrays and matrices seamless. It is useful linear algebra, Fourier transform, and random number operations etc
# 
# - [PANDAS](https://pandas.pydata.org/) pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,built on top of the Python programming language. 
# 
# - [SCIPY](https://scipy.org/scipylib/) Another core library for scientific computing is SciPy. It is based on NumPy and therefore extends its capabilities. SciPy main data structure is again a multidimensional array, implemented by Numpy. The package contains tools that help with solving linear algebra, probability theory, integral calculus and many more tasks. 
# 
# - [STATSMODELS](http://www.statsmodels.org/devel/): A Python module that provides many opportunities for statistical data analysis, such as statistical models estimation, performing statistical tests, etc. With its help, you can implement many machine learning methods and explore different plotting possibilities.
# 
# #### Visualization
# - [MATPLOTLIB](https://matplotlib.org/index.html): Matplotlib is a low-level library for creating two-dimensional diagrams and graphs. With its help, you can build diverse charts, from histograms and scatterplots to non-Cartesian coordinates graphs
# 
# - [SEABORN](https://seaborn.pydata.org/): Seaborn is essentially a higher-level API based on the matplotlib library. It contains more suitable default settings for processing charts. Also, there is a rich gallery of visualizations including some complex types like time series, jointplots, and violin diagrams.
# 
# - [PLOTLY](https://plot.ly/python/): Enable users to build interactive reports that are print ready and presentation ready without ever downloading, linking, or reformatting.
# 
# - [BOKEH](https://bokeh.pydata.org/en/latest/): The Bokeh library creates interactive and scalable visualizations in a browser using JavaScript widgets. The library provides a versatile collection of graphs, styling possibilities, interaction abilities in the form of linking plots, adding widgets, and defining callbacks, and many more useful features.
# 
# - [PYDOT](https://pypi.org/project/pydot/): Pydot is a library for generating complex oriented and non-oriented graphs. It is an interface to Graphviz, written in pure Python. With its help, it is possible to show the structure of graphs, which are very often needed when building neural networks and decision trees based algorithms.

# ### NUMPY Example
# To create an 8 by 7, zero matrix, a user might decide to used a repetitive statement (loop) with list data structure. 

# In[7]:


##Using a for loop to create array of zeros
a = []
for x in range(8): #This iterates for the number of rows
    row = []
    for y in range(7): #This iterates for the number of columns
        row.append(0)  #This adds 0 to the list (rows)
    a.append(row)      #This the row to the list (a) whhich represents the matrix
print ('The zero matrix using  a normal for loop is .................\n', a)


    
##Using a for nested loop in list cmprehension to create array of zeros
a = [[0 for y in range(7)] for x in range(8)]
print ('\nThe zero matrix using  list comprehension is .................\n', a)


# Meanwhile, this is not appropriate as list is a data structure that stores data of different types. If user therefore inputs a letter 'o' instead of 0, the list structure accepts it, though basic matrices operations like addition, subtraction, will be impossible. 
# 
# **NUMPY ARRAY** stores a list of elements that belong to the same data type. Manipulation of stored data becomes easier since basic matrices operations like addition, subtraction, multiplications etc can be performed

# In[5]:


# An 8 by 7 zero matrix using numpy array

import numpy
a = numpy.zeros((8,7)) 
print ('\nThe zero matrix using numpy is .................\n', a)


# ### STATSMODEL Example
# 
# https://www.statsmodels.org/stable/stats.html

# In[14]:


###### import statsmodels.api as sm
import numpy as np
X = np.arange(0, 9) * 2
y = [0, 1, 2, 3, 4, 5, 6, 7, 8]
regressor_OLS = sm.OLS(endog = y, exog = X).fit()
regressor_OLS.summary()


# ### Non Programming Data Science Tools
# - **[TABLEAU](https://www.tableau.com/)** Tableau can help anyone see and understand their data. Connect to almost any database, drag and drop to create visualizations, and share with a click.
# 
# - **[POWER BI](https://powerbi.microsoft.com/en-us/)** - Power BI is a business analytics service by Microsoft. It aims to provide interactive visualizations and business intelligence capabilities with an interface simple enough for end users to create their own reports and dashboards.
# 
# - **[BIG ML](https://bigml.com/)** -  an online machine learning platform. The platform solves and automates classification, regression, cluster analysis, anomaly detection, association discovery, and topic modeling task. BigML, Inc. serves analysts, software developers, and scientists to perform machine learning tasks, transform data into actionable models that are used as remote services or, embedded into applications to make predictions.
# 
# - **[MICROSOFT AZURE](https://azure.microsoft.com/en-us/)** - Microsoft Azure is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications and services through Microsoft-managed data centers. It provides software as a service, platform as a service and infrastructure as a service and supports many different programming languages, tools, and frameworks, including both Microsoft-specific and third-party software and systems
# 
# - **KNIME** – This tool is awesome for training machine learning models. It takes some getting used to initially but the GUI is awesome to get started with. It produces results on par with most tools and is free of cost as well
# 
# - **FeatureLab** – It allows easy predictive modeling and deployment using GUI. One of the best selling points it has is automated feature engineering [For more](https://www.analyticsvidhya.com/blog/2018/05/19-data-science-tools-for-people-dont-understand-coding/)
# 
# - **MarketSwitch** – This tool is more focussed on optimization rather than predictive analytics
# 
# - **Logical Glue** – Another GUI based machine learning platform which works from raw data to deployment
# 
# - **Pure Predictive** – This tool uses a patented Artificial Intelligence system which obviates the part of data preparation and model tuning; it uses AI to combine 1000s of models into what they call “supermodels”
# 
# - **ATH Precision** – This tool by Analyttica has 600+ analytical functions inbuilt, which are available at a point of a click. ATH Pr

# In[ ]:




