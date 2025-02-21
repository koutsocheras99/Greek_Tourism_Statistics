import xlrd
import re
import matplotlib.pyplot as plt

# this could be done in a more simplier way (not using dictionary but lists(check tourist_per_quarter.py)) but it was implemented together with countries_most.py

def most_tourists(start_year, end_year):

    years = ['2011','2012','2013','2014','2015']
    plot_list = []

    for year in years[(start_year-2011):(end_year-2011+1)]:
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
            cleared = re.sub('[^0-9.]', '', str(num_tourist))
            
            if cleared:
                # append to the dictionary with the certain format
                country_tourist.update({country: num_tourist})
                # print(cleared)

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
                country_tourist_top.append(key[1])

        # print every year total tourists number
        # print(country_tourist_top[0])

        plot_list.append(country_tourist_top[:1])

    # remove the circular reference      
    plot_list = sum(plot_list, [])

    plt.bar(years[(start_year-2011):(end_year-2011+1)], plot_list, color='lightskyblue', width=0.35)
    plt.title('Total Tourists per Year')
    plt.xlabel('Years')
    plt.ylabel('Number of Tourists')
    plt.plot(style='plain')
    plt.show()

    print(plot_list)

    return plot_list
    
if __name__ == '__main__':
    most_tourists(2011,2015)