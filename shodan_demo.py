from shodan import Shodan
import pandas as pd
import matplotlib.pyplot as plt

# Define number of countries to process from input file
N_COUNTRIES = 3

# Read API key from file and initialiye shodan API
with open('input/api.key', 'r') as file:
    key = file.read().rstrip()
api = Shodan(key)

## EXAMPLES

# Lookup an IP
# ipinfo = api.host('8.8.8.8')
# print(ipinfo)

# domaininfo = api.dns.domain_info("www.google.com")
# print(domaininfo)

# Search for websites that have been "hacked"
# for banner in api.search_cursor('http.title:"hacked by"'):
#     print(banner)


# function to get the total number of industrial control systems services on the Internet per Country
def get_ics_counts(country_code):
    return api.count(f'tag:ics country:{country_code}')['total']


# Initialize Data Frame with population data and country codes from file
countries = pd.read_csv('input/countries.csv', nrows=N_COUNTRIES, header=0)
print(countries)


# Download ics data from shodan for each country
ics_counts = [get_ics_counts(code) for code in countries['code']]

# Update Data Frame with ics data
countries['ics_counts'] = ics_counts
print(countries)

# Plot Population vs number of ics in a country
figure = countries.plot.scatter(x='population',y='ics_counts')
# figure.axes.set_xscale('log')
plt.savefig(f'output/scatterplot_of_{N_COUNTRIES}_countries.png')

# Explore data with selectors
print(countries[countries['population'] > 500000000])
print(countries[countries['ics_counts'] > 4000])