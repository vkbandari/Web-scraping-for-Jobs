#importing all necessary libraries

from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd
import os

#==============================================================================================================

def scrape_main(link):
    '''
    a function that request the webpage and store it in response object. then passing lxml parser to parse over the webpage.

    here lxml parser defines the speed to parse the webpage.

    if it throws any errors in using lxml parser. just install it by: " pip intall lxml "
    '''

    response = requests.get(link)
    return (BeautifulSoup(response.text, 'lxml'))


#===============================================================================================================

def get_complete_info():
    # reading first csv file which contains the links
    df = pd.read_csv("first_links.csv")

    # checking 5 job records
    #df.head(5)

    row_heading = ['source', 'location', 'job_link', 'job_title', 'company_name', 'imp_fields', 'description_headings',
                   'description']

    # timestamp as file name by using time library and with prefix as internshala
    file_name_2 = 'internshala_second_raw_data_' + time.strftime("%d_%m_%Y_%H_%M_%S") + ".csv"

    # opening file in write mode and connecting csv writer to file
    file = open(file_name_2, 'w')
    writer = csv.writer(file)

    # initially writing header of csv file
    writer.writerow(row_heading)

    # looping over dataframe link column with index value to give job location and source to new data frame
    for index, link in enumerate(df.job_link):
        # passing  url to scrape on each job link
        soup = scrape_main(link)

        # getting job title by finding unique class name in webpage
        if soup.find('div', {'class': 'heading_4_5 profile'}) == None:
            continue

        job_title = soup.find('div', {'class': 'heading_4_5 profile'}).text.strip()

        # getting company name by unique class name of div tag
        company_name = soup.find('div', {'class': 'heading_6 company_name'}).text.strip()

        '''
        # getting important fields in the job posting as list
        fields are:
        1. start date of joining/mode of vacancy
        2. duration of job
        3. incentives/stipend
        4. last date to apply
        5. types of doing job 
        '''

        imp_fields = []
        for i in soup.find_all('div', {'class': 'item_body'}):
            imp_fields.append(i.get_text().strip())

        # this list is extracting for further process to do in description to get valuable information.
        description_headings = []
        for i in soup.find_all('div', {'class': 'section_heading heading_5_5'}):
            description_headings.append(i.get_text().strip())

        # complete description of job
        description = soup.find('div', {'class': 'internship_details'}).get_text().strip()

        # writing to the server
        writer.writerow([df.source[index], df.location[index], df.job_link[index], job_title, company_name, imp_fields,
                         description_headings, description])

    file.close()

    # loading extracted csv file to the dataframe
    df2 = pd.read_csv(file_name_2)

    #df2.sample(5)

    # getting size of csv file
    #df2.shape

    #### To save it into normal csv file just run below cell
    os.remove(file_name_2)
    df2.to_csv(file_name_2)