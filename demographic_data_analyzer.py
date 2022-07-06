import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?

    df1 = df.loc[df.sex == 'Male']
    average_age_men = round(df1.age.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    df2 = len(df.loc[df.education == 'Bachelors'])
    percentage_bachelors = round(df2/len(df)*100,1)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    df3 = (df[df.education.isin(['Bachelors','Masters','Doctorate'])])
    higher_education_rich = round(len(df3[df3.salary == '>50K'])/len(df3)*100,1)
    df4 = (df[~df.education.isin(['Bachelors','Masters','Doctorate'])])
    lower_education_rich = round(len(df4[df4.salary == '>50K'])/len(df4)*100,1)
    
    # percentage with salary >50K
   
    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df['hours-per-week'].min()
  
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    df5 = df[(df['hours-per-week'] == min_work_hours) & (df.salary == '>50K')] 
    rich_percentage = round(len(df5)/len(df[(df['hours-per-week'] == min_work_hours)])*100,1)
  #round(len(df5)/len(df)*100,1)

    # What country has the highest percentage of people that earn >50K?

    df6 = df['native-country'].value_counts().to_frame()
  
    df7 = df[(df.salary == '>50K')]
    df8 = df7['native-country'].value_counts().to_frame()

    df8['total-employee'] = df6['native-country']
    df8['avg_country'] = round(df8['native-country']/df8['total-employee']*100,1)
    df8 = df8.sort_values('avg_country',ascending = False)
  
    highest_earning_country = df8.index[0]
    highest_earning_country_percentage = df8.values[0][2]

    # Identify the most popular occupation for those who earn >50K in India.

    df9 = df[(df.salary == '>50K') & (df['native-country'] == 'India')]
    df10 = df.occupation.value_counts()
    top_IN_occupation = df10.index[0] 
    

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
