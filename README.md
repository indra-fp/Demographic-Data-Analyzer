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

The dataset are saved in `adult.data.csv`, and the answer with the question are in `demographic_data_analyzer.py`

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

### 5. What is the minimum number of hours a person works per week (hours-per-week feature)?

We can easily get the number using .min() on house-per-week column
`min_work_hours = df['hours-per-week'].min()`

### 6. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
We can access the data using basic & to get the list of people who get min_work_hours(the variable that searched before) and have >50K salary

note: to be honest I don't really know the difference between using basic selection like this one, using .isin, or using .loc on copying data to new dataframes. I'm still new on this and didn't really know which one to use for which, so I just try and error all those things until it produce the needed results. 

    df5 = df[(df['hours-per-week'] == min_work_hours) & (df.salary == '>50K')] 

Then we can calculate the percentage using the data we acquired above, divided it with the total number of people who are work the minimum number of hours per week that aren't received >50K salary.

    rich_percentage = round(len(df5)/len(df[(df['hours-per-week'] == min_work_hours)])*100,1)


### 7. What country has the highest percentage of people that earn >50K? and what is that percentage?

This is a tricky question and I actually really messed up the way I got my result. If you read this and have a proper solution, feel free to hit me up and show the proper way to answer this.

The data we need to answer this is a list of country and people who earn >50K

First I save the list of total of people based on their country, using .value_counts(). Since that function return Series datatype, I'm using to_frame() to return it to DataFrame

`df6 = df['native-country'].value_counts().to_frame()`

Then I save all the people who received more than >50K, (Since the data is only provided 2 types of data, It is doable)

`df7 = df[(df.salary == '>50K')]`

After that I create another dataframe that similar to the first dataframe I created, but based on the people who received >50K

`df8 = df7['native-country'].value_counts().to_frame()`


Now is the fun and confusing part

I add a total-employee column on df8 dataframe, based on df6 dataframe

`df8['total-employee'] = df6['native-country']`

Then I add another column called avg_country that will count the percentage of people who received more than 50K divided with those who received less then 50K based on each country
    
`df8['avg_country'] = round(df8['native-country']/df8['total-employee']*100,1)`

After that, I sort the values Descending based on avg_country
    
`df8 = df8.sort_values('avg_country',ascending = False)`

And thats it, now we can see that the highest percentage of each country. The top one is the Country with the higest percentage of people who earn >50k. We can access using index[0], and the percentage we can access it using .values[0][2] (the Index [0] represent the first row of the list, and the [0][2], represent the first row and the third column)

`highest_earning_country = df8.index[0]`
`highest_earning_country_percentage = df8.values[0][2]`

### 8. Identify the most popular occupation for those who earn >50K in India.

First we need to isolate the dataframe that contains people who earn >50K and from India
 
`df9 = df[(df.salary == '>50K') & (df['native-country'] == 'India')]`

Then we can count the occupation using .value_counts()

`df10 = df.occupation.value_counts()`

Lastly we can use .index[] to access the data
    
`top_IN_occupation = df10.index[0]`


-----------------------------------------------------


The rest of the code are used for printing results, and for unit testing.


