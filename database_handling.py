import sqlite3
import csv
from country_v2 import country_most_tourists
from tourist_per_year import most_tourists
from transport_type import transport
from tourist_per_quarter import tourists_quarter

connection = sqlite3.connect('database.sqlite')

c = connection.cursor()

# creating tables

"""

c.execute('''
            CREATE TABLE IF NOT EXISTS TOURISTS_PER_YEAR (
            Year INT,
            NumbofTourists FLOAT );
          ''')

# country_v2.py
c.execute('''
            CREATE TABLE IF NOT EXISTS COUNTRIES_MOST_TOURISTS (
            Year INT,
            Country TEXT,
            NumbofTourists FLOAT );
          ''')

c.execute('''
            CREATE TABLE IF NOT EXISTS TRANSPORT_TYPE (
            Year INT,
            Airplane FLOAT,
            Railway FLOAT,
            Sea FLOAT,
            Road FLOAT);
           ''')

c.execute('''
            CREATE TABLE IF NOT EXISTS QUARTER (
            Year INT,
            Q1 FLOAT,
            Q2 FLOAT,
            Q3 FLOAT,
            Q4 FLOAT);
          ''')

connection.commit()

"""

years = ['2011','2012','2013','2014','2015']

# FIRST INSERTION

# tourists_per_year = most_tourists(2011,2015)

# insertion into table for total tourists per year
'''
for tour_num, year in zip(tourists_per_year, years):
  c.execute('INSERT INTO TOURISTS_PER_YEAR VALUES(?, ?)', (year, tour_num))

connection.commit()
'''

# SECOND INSERTION

# countries, num_tourists = country_most_tourists(1)

# insertion into table for countries with most tourists per year
'''
for year, country, num_tourist in zip(years, countries, num_tourists):
  c.execute('INSERT INTO COUNTRIES_MOST_TOURISTS VALUES(?, ?, ?)', (year, country, num_tourist))

connection.commit()
'''

# THIRD INSERTION

# air_list, rail_list, sea_list, road_list = transport(start_year=2011, end_year=2015)

# insertion into table for types of transport
'''
for year, air, rail, sea, road in zip(years, air_list, rail_list, sea_list, road_list):
  c.execute('INSERT INTO TRANSPORT_TYPE VALUES(?, ?, ?, ?, ?)', (year, air, rail, sea, road))

connection.commit()
'''

# FOURTH INSERTION

# q1_list, q2_list, q3_list, q4_list = tourists_quarter(start_year=2011, end_year=2015)

# insertion into table for tourists per quarter
'''
for year, q1, q2, q3, q4 in zip(years, q1_list, q2_list, q3_list, q4_list):
  c.execute('INSERT INTO QUARTER VALUES(?, ?, ?, ?, ?)', (year, q1, q2, q3, q4))

connection.commit()
'''

# c.execute('SELECT * FROM TOURISTS_PER_YEAR')
# c.execute('SELECT * FROM COUNTRIES_MOST_TOURISTS')
# c.execute('SELECT * FROM TRANSPORT_TYPE')
c.execute('SELECT * FROM QUARTER')

print("Database Content:")
print(c.fetchall())


# CREATING THE DEMANDED CSV FILES (need to uncomment some lines above. For example, for the first one || line 56 )

''' PER YEAR CSV 
with open('tourists_per_year.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Year", "Number of Tourists"])
  for year, element in zip(years, tourists_per_year):
    writer.writerow([year, element])
'''

''' COUNTRIES CSV
# enconding 'utf-8' for greek language issues 
with open('countries_most_tourists.csv', 'w', newline='', encoding='UTF-8') as file:
  writer = csv.writer(file)
  writer.writerow(["Year", "Country", "Number of Tourists"])
  for year, country, tourists_num in zip(years, countries, num_tourists):
    writer.writerow([year, country, tourists_num])
'''

''' TRANSPORT TYPE CSV
with open('transport_type.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Year", "Aiplane", "Railway", "Sea", "Road"])
  for year, air, rail, sea, road in zip(years, air_list, rail_list, sea_list, road_list):
    writer.writerow([year, air, rail, sea, road])
'''

''' QUARTER CSV
with open('tourist_per_quarter.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Year", "Q1", "Q2", "Q3", "Q4"])
  for year, q1, q2, q3, q4 in zip(years, q1_list, q2_list, q3_list, q4_list):
    writer.writerow([year, q1, q2, q3, q4])
'''