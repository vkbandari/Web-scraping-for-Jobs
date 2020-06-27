#importing all necessary libraries

from facebook_scraper_lib import get_posts
import csv
import time
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
import os


#=================================================================================================================

def url_rq(link):
    '''
      A function that request the webpage and store it in response object.

      Then passing lxml parser to parse over the webpage.

      Here lxml parser defines the speed to parse the webpage.

      If it throws any errors in using lxml parser. just install it by: " pip install lxml "
    '''
    response = requests.get(link)
    sp = soup(response.text, 'lxml')
    return(sp.find('div',{'dir':'ltr'}))


#=================================================================================================================


# timestamp as file name by using time library and with prefix as facebook
file_name = "facebook_" + time.strftime("%d_%m_%Y_%H_%M_%S") + ".csv"

#=================================================================================================================

def scrape_facebook():
    '''
        A function to get the posts in facebook and based on links in facebook it going to rescrape on that link.

        here it works only on links of id : 380555718642309.

        since the id values of other websites of other id might be different so need to cross check.
    '''

    # writing row heading to understand each column
    row_heading = ['post_id', 'text', 'post_text', 'shared_text', 'time', \
                   'likes', 'comments', 'shares', 'link', 'jobs_info']

    # opening file in write mode and connecting csv writer to file
    with open(file_name, 'w') as file:
        writer = csv.writer(file)

        # initially writing header of csv file
        writer.writerow(row_heading)

        # extracting posts from facebook  by using facebook_scraper_lib
        for post in get_posts('380555718642309', pages=15):

            # for jobs_info the actual scraping is done to extract xml data of multiple jobs.
            jobs_info = url_rq(post['link'])

            # writing all details to csv
            writer.writerow([post['post_id'], post['text'], post['post_text'],\
                             post['shared_text'], post['time'], post['likes'], post['comments'],\
                             post['shares'], post['link'], jobs_info])


    df = pd.read_csv(file_name)
    # df.tail(5)

    # size of jobs collected
    # df.shape

    # removing extracted csv file
    os.remove(file_name)

    # storing to csv file
    df.to_csv(file_name, index=False)



#=================================================================================================================

def to_database_format_facebook():
    '''
        To save file as pipe '|' as delimiter
    '''
    print("\tHere the csv file stored in pipe as delimiter format " \
            "\n\t file name is given in time format way as: " \
          "\n\t'facebook_database_ + time.strftime(%d_%m_%Y_%H_%M_%S)'")

    # reading first csv file
    df_1 = pd.read_csv(file_name)

    # given time stamp file
    file_db_1 = 'facebook_database_' + time.strftime("%d_%m_%Y_%H_%M_%S") + '.csv'

    # saving file as db format
    df_1.to_csv(file_db_1, sep='|', index = False)


# =================================================================================================================


