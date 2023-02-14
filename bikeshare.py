import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #User input information from personal notes and from https://pynative.com/python-accept-list-input-from-user/
city=input('Please enter your city here: ')
while city not in ['chicago', 'washington', 'new york city']
	city=input("Please choose between: Chicago, Washington, or New York City."


    # TO DO: get user input for month (all, january, february, ... , june)
month=input('Please enter your desired month: ')
while month not in['january', 'february', 'march', 'april', 'may', 'june'].title()
	month=input('Please enter a month between January and June: ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
day=input('Please enter your desired day of the week: ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
               #Personal notes and https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column were used to generate the most common value questions. 
print("The most common month is: ", df['month].value_counts().idmax())

    # TO DO: display the most common day of week
print("The most common day of the week is: ", df['day_of_week'].value_counts().idmax())

    # TO DO: display the most common start hour
df['hour']=df['Start Time'].dt.hour
print("The most common start hour is: ", df['hour'].value_counts().idmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
 print("The most common station to START at is: ", df ['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
 print("The most common station to END at is: ", df ['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
 print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #User input information from personal notes and from https://pynative.com/python-accept-list-input-from-user/
city=input('Please enter your city here: ')
while city not in ['chicago', 'washington', 'new york city']
	city=input("Please choose between: Chicago, Washington, or New York City."


    # TO DO: get user input for month (all, january, february, ... , june)
month=input('Please enter your desired month: ')
while month not in['january', 'february', 'march', 'april', 'may', 'june'].title()
	month=input('Please enter a month between January and June: ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
day=input('Please enter your desired day of the week: ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
               #Personal notes and https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column were used to generate the most common value questions. 
print("The most common month is: ", df['month].value_counts().idmax())

    # TO DO: display the most common day of week
print("The most common day of the week is: ", df['day_of_week'].value_counts().idmax())

    # TO DO: display the most common start hour
df['hour']=df['Start Time'].dt.hour
print("The most common start hour is: ", df['hour'].value_counts().idmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
 print("The most common station to START at is: ", df ['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
 print("The most common station to END at is: ", df ['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
 print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
#the following section was created using personal notes and https://sparkbyexamples.com/pandas/pandas-get-column-average-mean/#:~:text=To%20calculate%20the%20mean%20of,all%20numeric%20columns%20using%20DataFrame.
    # TO DO: display total travel time
total_duration = df['Trip Duration'].sum()
    print("total travel time in hours is: ", total_duration)

    # TO DO: display mean travel time
 mean_duration = df['Trip Duration'].mean() 
    print("mean travel time in hours is: ", mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
#information pulled from practice questions and personal notes; also from https://www.w3schools.com/python/pandas/ref_df_min.asp
    # TO DO: Display counts of user types
 user_type = df['User Type'].value_counts()
    print(user_type)

    # TO DO: Display counts of gender
 user_gender = df['Gender'].value_counts()
    print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
earliest_year_of_birth = int(df['Birth Year'].min())
    most_recent_year_of_birth = int(df['Birth Year'].max())
    most_common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
    print("The earliest year of birth is:",earliest_year_of_birth,
          ", most recent one is:",most_recent_year_of_birth,
           "and the most common one is: ",most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
