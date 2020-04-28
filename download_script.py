from bs4 import BeautifulSoup
import requests
import re
import os 

dataset_path = 'dataset/'

# check if dataset folder already exists
if not os.path.exists(dataset_path):
    try:
        # creating dataset folder
        os.mkdir(dataset_path)
    except OSError:
        print('Error creating dataset directory!')

# list for future operation/identification
file_identification = ['Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης',
                       'Αφίξεις μη κατοίκων από το εξωτερικό ανά χώρα προέλευσης και μέσο μεταφοράς',
                       'Αφίξεις μη κατοίκων από το εξωτερικό ανά μέσο μεταφοράς και σταθμό εισόδου']

# creating sub folders
for folder_name in file_identification:
    # check if sub folder exists
    if not os.path.exists(dataset_path+folder_name):
        os.mkdir(dataset_path+folder_name)

# lists containing the requested timeframes
years = ['2011','2012','2013','2014','2015']
quarters = ['Q1','Q2','Q3','Q4']

# iterating for all years and quarters
for year in years:
    for quarter in quarters:
        # for the url identification
        year_quarter = (year+'-'+quarter)
        
        # defining the correct url for every loop
        url = 'https://www.statistics.gr/el/statistics/-/publication/STO04/'+year_quarter
        
        # requesting the page
        page = requests.get(url).text

        # using the beatiful soup module and html parser to scrape the page
        soup = BeautifulSoup(page, 'html.parser')

        # scraping the site searching for the specific data
        general_links = soup.find_all('td',class_='titleCol')

        # the first 3 are not relative to the objectives
        for general_link in general_links[3:]:
            # get the link text that will be downloaded afterwards
            link_text = general_link.a['href'] 
            
            # print(general_link.text) # let it run until it FINISHS and see the usage of cleared_text!

            # substitute numbers and dots for future matching using regural expressions module + strip to remove whitespace
            cleared_text = re.sub('[.\d]', '', general_link.text).strip()
            
            # the reason for this identification is the difference in the site ordering for year 2015 in comparison to the others
            for id_text in file_identification:
                if id_text == cleared_text:
                    # check it with the print function below
                    # print(id_text + ' ' + year_quarter)
            
                    # download the link
                    request_info = requests.get(link_text)
                    # create file in binary mode
                    file_writer = open(dataset_path+id_text+'/'+year_quarter+'.xls', 'wb+')
                    # write the content to the file
                    file_writer.write(request_info.content)
