# pandas--python
Title Page

Project Name: Study of Pandas Library in Python
Purpose: Understanding Data Manipulation and Analysis using Pandas
Language: Python

🎯 Aim of the Study

The aim of this project is to study the Pandas library in Python and understand how it is used for data manipulation and analysis.

This project focuses on:

Creating Series and DataFrames
Reading and writing data files
Data selection and filtering
Handling missing values
Performing statistical operations
Grouping and sorting data
📌 Introduction

Pandas is one of the most important Python libraries used for data analysis and data manipulation.

It provides powerful data structures such as:

Series (1D data structure)
DataFrame (2D tabular data structure)
Pandas is built on top of NumPy and is widely used in:

Data Science
Machine Learning
Finance
Business Analytics
It allows easy handling of structured data like CSV files, Excel files, and databases.

📖 Study of Pandas (Instructions)

Import Pandas library
Create Series objects
Create DataFrame objects
Load dataset from CSV file
Perform indexing and slicing
Filter data using conditions
Handle missing values
Apply statistical functions
Sort and group data
🔑 Key Concepts Covered

Importing pandas
Series creation
DataFrame creation
Reading CSV files
Head() and Tail()
Indexing (loc and iloc)
Filtering data
Handling null values
Sorting data
GroupBy operations
Descriptive statistics
📘 THEORY (Pandas Library)

1️⃣ Importing Pandas

Pandas is imported using:

import pandas as pd

Here, pd is an alias used for convenience.

2️⃣ Pandas Series

📌 Definition

A Series is a one-dimensional labeled array capable of holding data of any type.

Example:

import pandas as pd

data = pd.Series([10, 20, 30, 40]) print(data)

A Series consists of:

Values
Index
Custom index can also be provided:

pd.Series([10,20,30], index=["a","b","c"])

3️⃣ Pandas DataFrame

📌 Definition

A DataFrame is a two-dimensional, size-mutable, and labeled data structure with rows and columns.

It is similar to a table in a database or an Excel sheet.

Example:

data = { "Name": ["A", "B", "C"], "Marks": [85, 90, 88] }

df = pd.DataFrame(data) print(df)

4️⃣ Reading Data from CSV File

Pandas allows reading data from external files.

df = pd.read_csv("file.csv")

Common functions:

df.head() → First 5 rows
df.tail() → Last 5 rows
df.info() → Information about dataset
df.describe() → Statistical summary
5️⃣ Data Selection and Indexing

Using loc (label-based indexing)

df.loc[0]

Using iloc (position-based indexing)

df.iloc[0]

Selecting specific column:

df["Marks"]

Selecting multiple columns:

df[["Name", "Marks"]]

6️⃣ Filtering Data

Filtering is done using conditions.

df[df["Marks"] > 85]

This returns rows where marks are greater than 85.

7️⃣ Handling Missing Values

Missing values are common in datasets.

Functions used:

df.isnull()
df.notnull()
df.dropna() → Remove missing values
df.fillna() → Replace missing values
Example:

df.fillna(0)

8️⃣ Sorting Data

Sorting data using:

df.sort_values("Marks")

Sorting by multiple columns:

df.sort_values(["Marks", "Name"])

9️⃣ GroupBy Operation

GroupBy is used to group data based on certain categories.

df.groupby("Department").mean()

It is commonly used in data analysis for aggregation.

🔟 Descriptive Statistics

Pandas provides built-in statistical functions:

df.mean()
df.sum()
df.min()
df.max()
df.count()
df.std()
Example:

df["Marks"].mean()

📊 Advantages of Pandas

Easy data handling
Powerful data manipulation tools
Handles large datasets efficiently
Integrates well with NumPy and Matplotlib
Essential for Data Science
❌ Disadvantages of Pandas

Requires installation
Consumes more memory for very large datasets
Slightly complex for beginners
🛠 Tools Used

Python Interpreter
Jupyter Notebook (.ipynb)
VS Code / IDLE
Pandas Library
📂 Applications of Pandas

Data Cleaning
Data Analysis
Financial Analysis
Business Reporting
Machine Learning Preprocessing
Research and Statistics
🎯 Conclusion

Pandas is a powerful and flexible library used for data analysis in Python.

Through this study, we learned:

How to create Series and DataFrames
How to read datasets from CSV files
How to filter and manipulate data
How to handle missing values
How to apply statistical functions
Understanding Pandas is essential for becoming proficient in Data Science, Machine Learning, and Data Analytics.

📎 Extra Notes

DataFrame is the most commonly used Pandas structure
Always check missing values before analysis
loc is label-based, iloc is position-based
head() and describe() are very useful during EDA
