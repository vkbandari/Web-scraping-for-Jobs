#importing all python wrapper files

import facebook
import indeed
import internshala

#===============================================================================================================


if __name__ == '__main__':
    print("Started Main Function To Call Wrappers")
    print('\n',"*"*20)

    #started internshala
    print("Internshala scraping started:")

    #first links
    print("\t calling function of link extraction: ......")
    internshala.get_links_internshala()
    print('\t\tSuccessfully completed links extraction')

    #complete info
    print("\t calling function of total extraction: ......")
    internshala.get_complete_info_internshala()
    print('\t\tSuccessfully completed links extraction')
    print('successfully done internshala')

    # to convert it into database format - uncomment below line:
    internshala.to_database_format_internshala()

    print('\n',"*"*20)


    #indeed scrape
    print("Indeed scraping started:")

    print("\t calling function of scraping")
    indeed.scrape_indeed()
    print('\tSuccessfully completed extraction')

    # to convert it into database format - uncomment below line:
    indeed.to_database_format_indeed()

    print('\n',"*"*20)


    #facebook scrape
    print("facebook scraping started:")

    print("\t calling function of scraping")
    facebook.scrape_facebook()
    print('\tSuccessfully completed extraction')

    # to convert it into database format - uncomment below line:
    facebook.to_database_format_facebook()

    print('\n\n"***All Scraping Works Done***"')

#=================================================================================================================


