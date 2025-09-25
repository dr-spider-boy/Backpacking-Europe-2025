#Origonal program by Jack Watson. This program is designed to help the user plan a fun yet affordable backing trip accross Europe.


#csv is to read csv file.
#os is to clear the terminal at certain points to make more appeasing visually.
import csv
import os

#This is the main function.
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    

    print()
    input('Welcome to the ultimate \'Backpacing Europe\' guide!')
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print()
    print('This program will allow you to select a variety of destinations')
    input('and give you an accurate estimation of how much the trip will cost.')
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print()
    print('This estimation will include: ')
    print('1. Hostel prices')
    print('2. Local attraction prices')
    print('3. Daily treat such as gelato')
    print('4. Daily meals(3)')
    input('5. Local taxi rides per day(2)')
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print('Disclaimer:')
    print('Estimation does not include:')
    print('1. Flights')
    print('2. Eurorail pass')
    input('3. Souvenirs...Suveneers...however you spell it...')
    os.system('cls' if os.name == 'nt' else 'clear')


    basic_dictionary = read_csv('European Backpackers Index 2018.csv')
    daily_cost_dictionary = money_per_day('European Backpackers Index 2018.csv')

    print()
    print()


    duration = int(input('How many days do you want to stay in Europe?'))
    print()
    Eurorail = int(input('How many Eurorail trips do you want(5,7,10):'))

    os.system('cls' if os.name == 'nt' else 'clear')

    desired_destinations = country_choosing('European Backpackers Index 2018.csv', Eurorail)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    days_in_each_city = duration_in_each_city(desired_destinations, duration)
    
    
    total_trip_cost = total_price_of_living_in_europe_daily(desired_destinations, daily_cost_dictionary, days_in_each_city)


    os.system('cls' if os.name == 'nt' else 'clear')
    
    print()
    print()
    print(f'Your desired trip will cost about ${total_trip_cost:.2f}!')
    print('Happy Travels!!')
    print()
    print()





#This lets user decide how many days to spend in each city.
def duration_in_each_city(desired_destinations, duration):

    cities = []
    total_trip_cost = 0
    for item in desired_destinations:
        city = item[0]
        country = item[1]
        cities.append(city)

    days_left = duration
    counter = 0
    days_in_each_city = {}
    cities_left = len(cities)
    while days_left > 0:
        print()
        print()
        print(f'You have {days_left} days left and {cities_left} destinations left.')
        print('Choose how many days you want to spend in each destination.')
        days = int(input(f'{cities[counter]}:'))
        if days > days_left:
            print()
            print('Too many days. Try again.')
            print()
        else:
            days_in_each_city[cities[counter]] = days
            counter += 1
            days_left = days_left - days
            cities_left = cities_left - 1
    return days_in_each_city
#This calculates the total price of the trip.
def total_price_of_living_in_europe_daily(desired_destinations, daily_cost_dictionary, days_in_each_city):
    cities = []
    total_trip_cost = 0
    for item in desired_destinations:
        city = item[0]
        country = item[1]
        cities.append(city)
    
    for city in cities:
        daily_cost = float(daily_cost_dictionary[city])
        city_duration = float(days_in_each_city[city])
        city_cost = city_duration * daily_cost
        
        total_trip_cost = total_trip_cost + city_cost

    return total_trip_cost
#This function allows the user to select the destinations that they wish to visit based on how many eurorail trips they have chosen.
def country_choosing(file, trips):
    
    with open(file,mode='rt') as file:
        possible_destinations = []
        dictionary = {}
        altered_csv = csv.reader(file)
        next(altered_csv)

        trips = trips + 1
        dictionary = {}
        counter = 1
        for line in altered_csv:
            city = line[2]
            country = line[3]
            destination = [city, country]
            dictionary[counter] = destination
            counter = counter + 1
            possible_destinations.append(destination)

        for key,value in dictionary.items():
            print(f'{key}. {value}')
        print()
        print()
        print(f'Choose {trips} destinations from the list above(Only number).')
        print()
        desired_destinations = []

        destination_number = 1
        #While loop that allows user to pick from list.
        while trips > 0:
            number = int(input(f'Destination {destination_number}:'))
            country = dictionary[number]
            desired_destinations.append(country)
            trips = trips - 1
            destination_number = destination_number + 1

    return desired_destinations
#This function reads the csv file and makes a dictionary. key = country name, value = daily cost of living.
def money_per_day(file):

    with open(file,mode='rt') as file:
        daily_price_dictionary = {}
        altered_csv = csv.reader(file)
        next(altered_csv)


        for line in altered_csv:
            key = line[2]
            value = line[7]

            daily_price_dictionary[key] = value
    return daily_price_dictionary
#This function reads the csv file and turns it into a dictionary. key = country name. value = remainder of list.
def read_csv(file):

    with open(file, mode='rt') as file:
        country_dictionary = {}
        altered_csv = csv.reader(file)
        next(altered_csv)

        
        for line in altered_csv:
            key = line[3]
            value = line.pop(3)
            country_dictionary[key] = line
        
        
        
    return country_dictionary
#This calls main function.
if __name__ == '__main__':
    main()