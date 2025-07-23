import pandas as pd


def calculate_demographic_data(print_data=True):
     # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts() 

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(),1)
    
  
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df['education'] == 'Bachelors'])/len(df))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
   
    higher_education =  df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    # percentage with salary >50K
    higher_education_rich = round((len(higher_education[higher_education['salary'] == ">50K"])/len(higher_education))*100,1)
    lower_education_rich = round((len(lower_education[lower_education['salary'] == ">50K"])/len(lower_education))*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours =  int(df['hours-per-week'].min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minhours = df['hours-per-week'].min()
    
    num_min_workers = df[df['hours-per-week'] == minhours]

    rich_percentage = round((len(num_min_workers[num_min_workers['salary'] == ">50K"])/len(num_min_workers))*100,0)

    ##------------------------------------------

    # What country has the highest percentage of people that earn >50K?
    
    earning_country = pd.pivot_table(df, values='fnlwgt', index='native-country', columns = 'salary', aggfunc="count")
    
    earning_country['total'] = earning_country['<=50K'] + earning_country['>50K']
    earning_country['high_earners_p'] = earning_country['>50K'] / earning_country['total']
    earning_country = earning_country.sort_values(by='high_earners_p', ascending=False)
    
    earning_country = earning_country.reset_index()
    
    highest_earning_country = earning_country['native-country'].iloc[0]
    highest_earning_country_percentage = round(earning_country['high_earners_p'].iloc[0]*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    
    india_highearner = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    
    india_highearner = india_highearner.groupby('occupation').count().sort_values('age', ascending=False)
    india_highearner = india_highearner.reset_index()
    
    top_IN_occupation = india_highearner['occupation'].iloc[0]


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
