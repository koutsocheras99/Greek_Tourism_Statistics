import xlrd
import re
import matplotlib.pyplot as plt

def transport(start_year, end_year):

    years = ['2011','2012','2013','2014','2015']

    # lists for plotting
    air_list = []
    rail_list = []
    sea_list = []
    road_list = []

    for year in years[(start_year-2011):(end_year-2011+1)]:

        dataset_path = 'dataset/Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης και μέσο μεταφοράς/'+str(year)+'-Q4.xls'

        data = xlrd.open_workbook(dataset_path)

        december_sheet = data.sheet_by_index(11)

        airplane = december_sheet.col_values(2)
        air = []

        railway = december_sheet.col_values(3)
        rail = []

        by_sea = december_sheet.col_values(4)
        sea = []

        by_road = december_sheet.col_values(5)
        road = []
        
        for element1,element2,element3,element4 in zip(airplane, railway, by_sea, by_road):
            
            # leave only numbers and dots 
            element1 = re.sub('[^0-9.]', '', str(element1))
            element2 = re.sub('[^0-9.]', '', str(element2))
            element3 = re.sub('[^0-9.]', '', str(element3))
            element4 = re.sub('[^0-9.]', '', str(element4))

            # dont let empty elements get appenened in the list for the sort function
            if len(element1)>0 and len(element2)>0 and len(element3)>0 and len(element4)>0:
                air.append(element1)
                rail.append(element2)
                sea.append(element3)
                road.append(element4)

        # sort based on the numerical(float) value not the string!
        air.sort(reverse=True, key=float)
        rail.sort(reverse=True, key=float)
        sea.sort(reverse=True, key=float)
        road.sort(reverse=True, key=float)

        
        print(f'Using airplane: {air[0]}')
        print(f'Using railway: {rail[0]}')
        print(f'By sea: {sea[0]}')
        print(f'By road: {road[0]}')
        print('')

        air_list.append(float(air[0]))
        rail_list.append(float(rail[0]))
        sea_list.append(float(sea[0]))
        road_list.append(float(road[0]))
       
    plt.plot(years[(start_year-2011):(end_year-2011+1)], air_list, label='Airplane')
    plt.plot(years[(start_year-2011):(end_year-2011+1)], rail_list, label='Railway')
    plt.plot(years[(start_year-2011):(end_year-2011+1)], sea_list, label='Sea')
    plt.plot(years[(start_year-2011):(end_year-2011+1)], road_list,label='Road')

    plt.title('Transport Type and Number of Tourists')
    plt.xlabel('Years')
    plt.ylabel('Number of Tourists')

    plt.legend(loc='upper left')
    
    plt.show()
    
    
if __name__ == '__main__':
    transport(start_year=2011, end_year=2015)
