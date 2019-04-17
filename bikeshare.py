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

    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('please enter the city name which you wish to analyze(e.g. chicago, new york city, washington)\n').lower()
        if city in cities:
            break
        else :
            print('Oops you did not type correctly !!!! \n')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('tell us about the month you wish to analyze(note: month should be only from january, february, march, april, may, june)\n'
                    'please type \'all\'  for no filter \n').lower()
        if month in months:
            break
        else :
            print('Oops you did not type correctly the month name !!!! \n')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True :
        day = input('please tell us about the day of week you wish to analyze(e.g. any day from monday to sunday)\n'\
                'please type \'all\' if you don\'t need any filter\n').lower()
        if day in days :
            break
        else :
            print('Oops you did not type correctly the day !!!! \n')


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) #converting Start Time column into datetime format
    df['month'] = df['Start Time'].dt.month #extracting month from Start Time, creating new column
    df['day_of_week'] = df['Start Time'].dt.weekday_name # extracting day from Start Time, creating new column
    df['hour'] = df['Start Time'].dt.hour # extracting hour from Start Time, creating new column

    if month != 'all': #logic for month index
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month] #filter by month to create new dataframe

    if day != 'all':
        df = df[df['day_of_week'] == day.title()] #filter by day of week to create new dataframe



    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print('Most common month : ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print('Most common day of week : ', most_common_day_of_week)
    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print('Most common start hour : ', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('most commonly used start station : ', most_common_start_station)


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('most commonly used end station : ', most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("most frequent combination of start station and end station trip : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trav_time = df['Trip Duration'].sum()
    print('total travel time : ', total_trav_time)

    # TO DO: display mean travel time
    mean_trav_time = df['Trip Duration'].mean()
    print('mean travel time : ', mean_trav_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('total no. of users : ', user_counts)
    # TO DO: Display counts of gender
    if 'Gender' not in df.columns : #to avoid error for Washington file
        print('Sorry no data on Gender')
    else :
        gender_counts = df['Gender'].value_counts()
        print('counts of gender : ', gender_counts)
    if 'Birth Year' not in df.columns: #to avoid error for Washington file
        print('Sorry no data on Birth year')
    else :
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_yr = df['Birth Year'].min() #computing most recent year
        print('earliest year of birth : ', earliest_birth_yr)

        most_recent_birth_yr = df['Birth Year'].max() #computing most recent year of birth
        print('most recent year of birth : ', most_recent_birth_yr)

        most_common_birth_yr = df['Birth Year'].value_counts().idxmax() #computing most common year of birth
        print('most common year of birth : ', most_common_birth_yr)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    user_input = input('Do you want to see raw data? Enter yes or no.\n').lower()
    line_number = 0

    while True :
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see more raw data? Enter yes or no.\n').lower()
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
