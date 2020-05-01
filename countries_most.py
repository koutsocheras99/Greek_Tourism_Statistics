import xlrd
import re

def country_most_tourists(number_top):

    years = ['2011','2012','2013','2014','2015']

    for year in years:
        
        # no need to go to every file. just the Q4 at the last sheet contains the yearly required data
        dataset_path = 'dataset/Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης/'+str(year)+'-Q4.xls'

        # opening the file
        data = xlrd.open_workbook(dataset_path)

        # determine the last sheet (month = December)
        december_sheet = data.sheet_by_index(11)

        # defining the countries column
        countries = december_sheet.col_values(1)

        # defining the number of tourists column
        num_tourists = december_sheet.col_values(3)

        country_tourist = {}

        country_tourist_top = []

        # iterating in the countries, number of tourist columns
        for country, num_tourist in zip(countries, num_tourists):
            # removing non irrelevant records (ΕΤΟΣ)
            cleared = re.sub('\d', '', str(num_tourist))
            
            if cleared:
                # append to the dictionary with the certain format
                country_tourist.update({country: num_tourist})

        #print(country_tourist)

        # sorting the initial dictionary based on the number of tourists (x[1])
        sorted_numTour_dict = sorted(country_tourist.items(), key=lambda  x: x[1], reverse=True)

        # print(sorted_numTour_dict)

        for key in sorted_numTour_dict:
            # count space on the sorted dictionary keys for future operations
            count_space = len(re.findall(' ', key[0]))

            # for excluding empty key values and keys such as Λοιπά Κράτη Ευρώπης, Λοιπά κράτη Ασίας, etc (issue at Λίβανος - Συρία! that has 2 spaces) 
            if len(key[0])>0 and count_space<2:
                # append to the top list 
                country_tourist_top.append(key)

        print(country_tourist_top[1:number_top+1])



if __name__ == '__main__':
    country_most_tourists(5)