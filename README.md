# Demographic Data Analyzer

This is the boilerplate for the Demographic Data Analyzer project. 

This is a learning project provided by freecodecamp.org, below are the main page for the project

https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer


Using Python, The project aims to Analyze Demographic Data using Pandas. The dataset used are from the 1994 Census database.

### Below are the question to be solved

- How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
- What is the average age of men?
- What is the percentage of people who have a Bachelor's degree?
- What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
- What percentage of people without advanced education make more than 50K?
- What is the minimum number of hours a person works per week?
- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
- What country has the highest percentage of people that earn >50K and what is that percentage?
- Identify the most popular occupation for those who earn >50K in India.

The dataset are saved in adult.data.csv, and the answer with the question are in demographic_data_analyzer.py

I'll try to explain all the codes on demographic_data_analyzer.py

### Start with importing pandas

Since we are going to use pandas for this project, we need to import it first

`import pandas as pd`

### Read CSV

We need to read our data thus we need to access the CSV. We are using pd.read_csv to access the data.

`df = pd.read_csv('adult.data.csv')`

### 1. How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

We can use .value_counts() to easily count each of the data based on given column
    
`race_count = df.race.value_counts()` or `race_count = df[race].value_counts()`

It will return both the name of the 'Race' and its 'count value'

### 2.  What is the average age of men?

First, we need to separate the data to only Male. We can use .loc to locate based on the column.

`df1 = df.loc[df.sex == 'Male']`

Then we can find the average age using .mean() function and round() to round the numbers 1 digit behind comma.
    
`average_age_men = round(df1.age.mean(),1)`

### 3. What is the percentage of people who have a Bachelor's degree?
    
First we need to locate people who have a Bachelor's degree using .loc(), and find the total of people using len.

`df2 = len(df.loc[df.education == 'Bachelors'])`

Then we can count the bachelor's percentage by dividing the number we got earlier with the total number of data then times 100. We can round the numbers 1 to 1 digit behind comma using round().
    
`percentage_bachelors = round(df2/len(df)*100,1)`


### 3. What percentage of people with advanced education ('Bachelors', 'Masters', or 'Doctorate') make more than 50K?
### 4. What percentage of people without advanced education make more than 50K?

To answer the both 3rd and 4th question we need to split the data between the people who received higher educatuon, and those who are not.

We can use loc() but instead I want to use .isin() to get the data
    
`df3 = (df[df.education.isin(['Bachelors','Masters','Doctorate'])])`

Then we can find how much people that having salary more than >50K, divide it with how much people who received higher education and round it.
    
`higher_education_rich = round(len(df3[df3.salary == '>50K'])/len(df3)*100,1)`
    
Same issues to answer the 4th question, but instead we are gonna use ~ to locate the inverse of the data
    
`df4 = (df[~df.education.isin(['Bachelors','Masters','Doctorate'])])`

`lower_education_rich = round(len(df4[df4.salary == '>50K'])/len(df4)*100,1)`








