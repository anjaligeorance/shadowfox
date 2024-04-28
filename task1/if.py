# Define a dictionary with city-country pairs
city_country = {
    'Mumbai': 'India',
    'Chennai': 'India',
    'Sydney': 'Australia',
    'Dubai': 'United Arab Emirates'
}

# Ask the user to enter two cities
city1 = input('Enter the first city: ')
city2 = input('Enter the second city: ')

# Check if the cities belong to the same country
if city_country[city1] == city_country[city2]:
    print('Both cities are in', city_country[city1])
else:
    print("They don't belong to the same country")