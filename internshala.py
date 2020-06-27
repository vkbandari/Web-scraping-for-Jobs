#importing all necessary libraries

from bs4 import BeautifulSoup
import requests
from math import ceil
import time
import csv
import pandas as pd
import os

#=======================================================================================================

# array of internshala links
links_list = ['https://internshala.com/internships/work-from-home-jobs', \
            'https://internshala.com/internships/internship-in-bangalore', \
            'https://internshala.com/internships/internship-in-hyderabad', \
            'https://internshala.com/internships/internship-in-odisha']

#=======================================================================================================


def scrape_main(link):
    '''
     a function that request the webpage and store it in response object.

     then passing lxml parser to parse over the webpage.

     here lxml parser defines the speed to parse the webpage.

     if it throws any errors in using lxml parser. just install it by: " pip install lxml "
    '''

    response = requests.get(link)
    return (BeautifulSoup(response.text, 'lxml'))

#=================================================================================================================

# timestamp as file name by using time library and with prefix as internshala
file_name_1 = 'internshala_first_data_' + time.strftime("%d_%m_%Y_%H_%M_%S") + ".csv"


#============================================================================================================

def get_links_internshala(links = links_list):
    '''
        Function to extract unique links of job postings in internshala.
    '''

    # generalied locations based on links and its position
    loc_links = ['work_from_home', 'bangalore', 'hyderabad', 'odisha']

    # writing row heading to understand each column
    row_heading = ['source', 'location', 'job_link']

    # opening file in write mode and connecting csv writer to file
    file = open(file_name_1, 'w')
    writer = csv.writer(file)

    # initially writing header of csv file
    writer.writerow(row_heading)

    # looping over array of links with index value
    for index, url in enumerate(links):
        # passing main page to scape
        soup = scrape_main(url)

        #  to find number of job pages to scrape we need to get count of jobs available which is at heading in webpage.
        # print(soup.find('div',{'class':'heading heading_4_6'}))

        # based on count of jobs - finding the number of pages available at one link in array of links.
        pages = ceil(int(soup.find('div', {'class': 'heading heading_4_6'}).text.split()[0]) / 40)
        for page in range(pages):
            # now we need to scrape over pages under main url
            base_url = url + "/page-" + str(page)
            soup1 = scrape_main(base_url)

            # firstly finding each single job in each page to find job link
            for single_job in soup.find_all("div", {"class": "individual_internship"}):

                if (single_job.find('div', {'class': 'heading_4_5 profile'}) == None):
                    continue

                job_link = "https://internshala.com"
                job_link += single_job.find('div', {'class': 'heading_4_5 profile'}).a.get('href')

                source = 'internshala'

                location = loc_links[index]

                # writing all details to csv
                writer.writerow([source, location, job_link])
                #break
        #break

    # closing csv file
    file.close()

    # reading csv file
    df = pd.read_csv(file_name_1)

    # df.tail(5)

    # size of jobs collected
    # df.shape

    # removing extracted csv file
    os.remove(file_name_1)

    # storing to csv file
    df.to_csv(file_name_1, index=False)

#=================================================================================================================

# timestamp as file name by using time library and with prefix as internshala
file_name_2 = 'internshala_second_data_' + time.strftime("%d_%m_%Y_%H_%M_%S") + ".csv"


#===============================================================================================================

def get_complete_info_internshala(file_name = file_name_1):
    '''
        A function in internshala scraping to extract all the information about each job posting based on link.

    '''
    # reading first csv file which contains the links
    df = pd.read_csv(file_name)

    # checking 5 job records
    #df.head(5)

    # writing row heading to understand each column
    row_heading = ['source', 'location', 'job_link', 'job_title', \
                   'company_name', 'imp_fields', 'description_headings', 'description']


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
        writer.writerow([df.source[index], df.location[index], df.job_link[index], \
                         job_title, company_name, imp_fields, description_headings, description])

    # closing file object
    file.close()

    # loading extracted csv file to the dataframe
    df2 = pd.read_csv(file_name_2)

    #df2.sample(5)

    # getting size of csv file
    #df2.shape

    #removing extracted csv file
    os.remove(file_name_2)

    #### To save it into normal csv file without spaces
    df2.to_csv(file_name_2, index = False)


#=================================================================================================================

def to_database_format_internshala():
    '''
        To save file as pipe '|' as delimiter
    '''
    print("\tHere the csv file stored in pipe as delimiter format " \
            "\n\t file names are given in time format way as: " \
          "\n\t'internshala_first/second_database_ + time.strftime(%d_%m_%Y_%H_%M_%S)'")

    # reading first csv file
    df_1 = pd.read_csv(file_name_1)

    # given time stamp file
    file_db_1 = 'internshala_first_database_' + time.strftime("%d_%m_%Y_%H_%M_%S") + '.csv'

    # saving file as db format
    df_1.to_csv(file_db_1, sep='|', index = False)

    # reading second csv file
    df_2 = pd.read_csv(file_name_2)

    # given time stamp file
    file_db_2 = 'internshala_second_database_' + time.strftime("%d_%m_%Y_%H_%M_%S") + '.csv'

    # saving file as db format
    df_2.to_csv(file_db_2, sep='|', index = False)



#=============================================================================================================