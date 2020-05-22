import xlrd
import re
from collections import defaultdict
import matplotlib.pyplot as plt


def init_country_dict():
    # no need to go to every file. just the Q4 at the last sheet contains the yearly required data
    dataset_path = 'dataset/Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης/'+'2015'+'-Q4.xls'

    # opening the file
    data = xlrd.open_workbook(dataset_path)

    # determine the last sheet (month = December)
    december_sheet = data.sheet_by_index(11)

    # defining the countries column
    countries = december_sheet.col_values(1)
    
    country_tourist = {}

    # iterating in the countries column
    for country in countries:

        count_space = len(re.findall(' ', country))
        trash = re.findall(':', country)
        
        if len(country)>0 and count_space<2 and not trash:
            # 'append-initialize' each country in the returning dictionary
            country_tourist.update({country: int(0)})

    return country_tourist


def country_most_tourists(numberOfCountries, start_year, end_year):

    country_tourist = init_country_dict()

    # print(country_tourist)

    years = ['2011','2012','2013','2014','2015']

    for year in years[(start_year-2011):(end_year-2011+1)]:
       
        # no need to go to every file. just the Q4 at the last sheet contains the yearly required data
        dataset_path = 'dataset/Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης/'+str(year)+'-Q4.xls'

        # opening the file
        data = xlrd.open_workbook(dataset_path)

        # determine the last sheet (month = December)
        december_sheet = data.sheet_by_index(11)
        
        # iterating in the countries, percentage of tourists columns
        for country, percentage_tourists in zip(december_sheet.col_values(colx=1,start_rowx=71,end_rowx=None), december_sheet.col_values(colx=6,start_rowx=71,end_rowx=None)):
            # removing non irrelevant records (letters) (example -> ΕΤΟΣ) 
            cleared = re.sub('[^0-9.]', '', str(percentage_tourists))
            # check countries.py
            count_space = len(re.findall(' ', country))
            trash = re.findall(':', country)
            
            if cleared and len(country)>0 and count_space<2 and not trash:
                # increment to each country the median percentage of tourists per year
                country_tourist[country] = country_tourist.get(country, 0) + percentage_tourists/len(years)
                

    sorted_numTour_dict = sorted(country_tourist.items(), key=lambda  x: x[1], reverse=True)

    # print(country_tourist.values())

    # matplotlib stuff
    labels = []
    sizes = []
    other_countries_size = 0

    for k in sorted_numTour_dict[1:numberOfCountries+1]:
        labels.append(k[0])
        sizes.append(k[1])
    
    # trying putting the following 5 lines in comments to see the difference in the pie chart
    # me liga logia -> an exw xwra_a, xwra_b me percentages 15% h kathemia sto geniko sunolo, sto chart tha mou bgoun 50% h kathemia pragma poy einai lathos
    for k in sorted_numTour_dict[numberOfCountries+1:]:
        other_countries_size +=  k[1]

    sizes.append(other_countries_size)
    labels.append('Υπόλοιπες Χώρες')
    
    print(sorted_numTour_dict[1:numberOfCountries+1])
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

    # print to see the small fault(~2% ) countries such as Λοιπές Χώρες were excluded.
    # print(other_countries_size)

if __name__ == '__main__':
    country_most_tourists(8, start_year= 2011, end_year= 2015)
