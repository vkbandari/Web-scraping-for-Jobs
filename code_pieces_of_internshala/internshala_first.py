#importing all necessary libraries

from bs4 import BeautifulSoup
import requests
from math import ceil
import time
import csv
import pandas as pd
import os

#=======================================================================================================

def scrape_main(link):
    '''
    a function that request the webpage and store it in response object. then passing lxml parser to parse over the webpage.

    here lxml parser defines the speed to parse the webpage.

    if it throws any errors in using lxml parser. just install it by: " pip intall lxml "
    '''

    response = requests.get(link)
    return (BeautifulSoup(response.text, 'lxml'))



# timestamp as file name by using time library and with prefix as internshala
file_name_1 = 'internshala_first_data_' + time.strftime("%d_%m_%Y_%H_%M_%S") + ".csv"


#============================================================================================================

def get_links():
    # array of internshala links
    links = ['https://internshala.com/internships/work-from-home-jobs', \
             'https://internshala.com/internships/internship-in-bangalore', \
             'https://internshala.com/internships/internship-in-hyderabad', \
             'https://internshala.com/internships/internship-in-odisha']

    # generalied locations based on links and its position

    loc_links = ['work_from_home', 'bangalore', 'hyderabad', 'odisha']

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

    # closing csv file
    file.close()

    # reading csv file
    df = pd.read_csv(file_name_1)

    # df.tail(5)

    # size of jobs collected
    # df.shape

    #### To save it into normal csv file just run below cell
    #storing to csv file
    os.remove(file_name_1)
    df.to_csv(file_name_1)


#===============================================================================================================

