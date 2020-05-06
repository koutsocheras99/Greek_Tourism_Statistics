import xlrd
import re

def tourists_quarter():

    years = ['2011','2012','2013','2014','2015']
    quarters_num = [2,5,8,11]
    
    for year in years:
        # no need to go to every file. just the Q4 at the last sheet contains the yearly required data
        dataset_path = 'dataset/Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης/'+str(year)+'-Q4.xls'

        # opening the file
        data = xlrd.open_workbook(dataset_path)

        quarter_list = []
        top_quarter = []

        for quarter in quarters_num:
            specific_sheet = data.sheet_by_index(quarter)

            # defining the number of tourists column
            num_tourists = specific_sheet.col_values(3)
            
            for num_tourist in num_tourists:
                cleared = re.sub('[^0-9.]', '', str(num_tourist))

                if cleared:
                    quarter_list.append(cleared)
                
            quarter_list.sort(key=float, reverse=True)

            # print(quarter_list[0])
            top_quarter.append(quarter_list[0])

        # try with a recursive way
        q1 = float(top_quarter[0])
        q2 = float(top_quarter[1]) - q1
        q3 = float(top_quarter[2]) - q2 - q1
        q4 = float(top_quarter[3]) - q3 - q2 - q1

    
        print(year)
        print(f'Q1:{q1} Q2:{q2} Q3:{q3} Q4:{q4}')
        print('')
 
            
if __name__ == '__main__':
    tourists_quarter()