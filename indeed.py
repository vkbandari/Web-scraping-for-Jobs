#importing all necessary libraries

import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests
import time
import os


#========================================================================================================

# array of indeed links
links_list = ['https://www.indeed.co.in/jobs?q=&l=Telangana&radius=100&sort=date&start=', \
              'https://www.indeed.co.in/jobs?q=&l=Karnataka&radius=100&sort=date&start=', \
              'https://www.indeed.co.in/jobs?q=&l=Orissa&radius=100&sort=date&start=']


#=================================================================================================================

def url_soup(url):
    '''
      A function that request the webpage and store it in response object.

      Then passing lxml parser to parse over the webpage.

      Here lxml parser defines the speed to parse the webpage.

      If it throws any errors in using lxml parser. just install it by: " pip install lxml "
    '''
    response = requests.get(url)
    return (BeautifulSoup(response.text, 'lxml'))


#=================================================================================================================

# timestamp as file name by using time library and with prefix as indeed
file_name = "indeed_" + time.strftime("%d_%m_%Y_%H_%M_%S") + ".csv"


#=================================================================================================================

def scrape_indeed(list = links_list):
    '''
        A function in indeed to extract jobs in indeed using the array of links_list,

        where all job links are given based on location wise.
    '''

    # writing row heading to understand each column
    row_heading = ['source', 'job_title', 'company_name', 'salary', 'location', 'short_summary', 'link']

    # opening file in write mode and connecting csv writer to file
    file = open(file_name, 'w')
    writer = csv.writer(file)

    # initially writing header of csv file
    writer.writerow(row_heading)

    # count variable to count the jobs
    count = 0

    #limit value - static value
    limit  = 100

    # looping over array of links with index value
    for i in list:
        sp = url_soup(i)
        cont = sp.find("div", {"id": "searchCountPages"})
        jobs = cont.string.split()[3]
        jobs = jobs.replace(',', '')
        for page in range(0, 100, 10):
            container = sp.findAll("div", {"class": "jobsearch-SerpJobCard"})
            # print(len(container))

            for each_job in range(len(container)):
                source = "indeed"

                # getting single job posting work title
                job_title = container[each_job].find('a', {'class': 'jobtitle'}).string.strip()

                # getting single job company name
                comp_na = container[each_job].find('span', {'class': 'company'}).string
                if comp_na != None:
                    comp_name = comp_na.strip()
                else:
                    comp_name = None

                # getting single job salary
                sal = container[each_job].find('span', {'class': 'salaryText'})
                if sal != None:
                    salary = sal.string.strip()
                else:
                    salary = None

                # getting single job location
                job_lo = container[each_job].find('div', {'class': 'location'})
                if job_lo != None:
                    job_loc = job_lo.string.strip()
                else:
                    job_loc = None

                # getting single job summary
                job_short_summa = container[each_job].find('div', {'class': 'summary'}).li
                if job_short_summa != None:
                    job_short_summary = job_short_summa.string.strip()
                else:
                    job_short_summary = None

                # to get complete info
                # getting single job posting link
                link = 'https://www.indeed.co.in'
                link += container[each_job].a.get('href')
                job_link = link
                lis = [source, job_title, comp_name, salary, job_loc, job_short_summary, job_link]
                # for i in lis:
                # print(i)

                # writing all details to csv
                writer.writerow(lis)

                # on each record writing count is increasing
                count += 1
                if count == limit:
                    break
            if count == limit:
                break

    # closing csv file
    file.close()

    # reading csv file
    df = pd.read_csv(file_name)

    # df.tail(5)

    # size of jobs collected
    # df.shape

    # removing extracted csv file
    os.remove(file_name)

    # storing to csv file
    df.to_csv(file_name, index=False)


#=================================================================================================================

def to_database_format_indeed():
    '''
        To save file as pipe '|' as delimiter
    '''
    print("\tHere the csv file stored in pipe as delimiter format " \
            "\n\t file name is given in time format way as: " \
          "\n\t'indeed_database_ + time.strftime(%d_%m_%Y_%H_%M_%S)'")

    # reading first csv file
    df_1 = pd.read_csv(file_name)

    # given time stamp file
    file_db_1 = 'indeed_database_' + time.strftime("%d_%m_%Y_%H_%M_%S") + '.csv'

    # saving file as db format
    df_1.to_csv(file_db_1, sep='|', index = False)


# =================================================================================================================

