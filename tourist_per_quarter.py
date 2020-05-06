import xlrd
import re
import matplotlib.pyplot as plt
import numpy as np

def tourists_quarter():

    years = ['2011','2012','2013','2014','2015']
    quarters_num = [2,5,8,11]

    # for plotting
    q1_list = []
    q2_list = []
    q3_list = []
    q4_list = []
        
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

        q1_list.append(q1)
        q2_list.append(q2)
        q3_list.append(q3)
        q4_list.append(q4)
    
        print(year)
        print(f'Q1:{q1} Q2:{q2} Q3:{q3} Q4:{q4}')
        print('')

    X = np.arange(2011,2016)
    
    plt.bar(X - 0.3, q1_list, width = 0.2, label='Q1')
    plt.bar(X - 0.1, q2_list, width = 0.2, label='Q2')
    plt.bar(X + 0.1, q3_list, width = 0.2, label='Q3')
    plt.bar(X + 0.3, q4_list, width = 0.2, label='Q4')
    
    plt.title('Tourists per Quarter')
    plt.xlabel('Years')
    plt.ylabel('Number of Tourists')

    plt.legend(loc='best')
    
    plt.show()
 
            
if __name__ == '__main__':
    tourists_quarter()
