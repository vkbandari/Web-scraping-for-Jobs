import pymysql
import csv

#======================================================================================================================


db = pymysql.connect(host='localhost', user='root', password='password', db='mindaddadb1')
cursor = db.cursor()

'''
#======================================================================================================================
#internshala data insertion

with open('internshala_second_database_27_06_2020_10_41_11.csv') as file:
    spamreader = csv.DictReader(file, delimiter='|')
    for row in spamreader:
        sql = """INSERT INTO raw_internshala_scrape ( source, location, job_link, job_title, company_name, imp_fields, description_headings, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (row['source'], row['location'], row['job_link'], row['job_title'], row['company_name'], row['imp_fields'], row['description_headings'], row['description'])
        cursor.execute(sql, val)
        db.commit()
        #print(count, row['source'],'*******\n\n', row['location'],'*********\n\n', str(row['job_link']),'******\n\n', str(row['job_title']),'***********\n\n', row['company_name'],'************\n\n', row['imp_fields'],'***********\n\n', row['description_headings'],'************\n\n', row['description'])

#======================================================================================================================


cursor.execute("select * from raw_internshala_scrape")
myresult = cursor.fetchall()
for i in myresult:
    print(i)

#======================================================================================================================
'''
#indeed data Insertion

with open('indeed_database_27_06_2020_10_41_19.csv') as file:
    spamreader = csv.DictReader(file, delimiter='|')
    for row in spamreader:
        sql = """INSERT INTO raw_indeed_scrape ( source, job_title, company_name, salary, location, short_summary, link) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val = (row['source'], row['job_title'], row['company_name'], row['salary'], row['location'], row['short_summary'], row['link'] )
        cursor.execute(sql, val)
        db.commit()
        #print(row['source'], row['job_title'], row['company_name'], row['salary'], row['location'], row['short_summary'], row['link'])


#======================================================================================================================

cursor.execute("select * from raw_indeed_scrape")
myresult = cursor.fetchall()
for i in myresult:
    print(i)


#======================================================================================================================

'''
#facebook Data insertion

with open('facebook_database_27_06_2020_10_41_27.csv') as file:
    spamreader = csv.DictReader(file, delimiter='|')
    for row in spamreader:
        sql = """INSERT INTO raw_fb_scrape ( post_id, text, post_text, shared_text, time, likes, comments, shares, link, jobs_info ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (row['post_id'], row['text'], row['post_text'], row['shared_text'], row['time'], row['likes'], row['comments'], row['shares'], row['link'], row['jobs_info'] )
        cursor.execute(sql, val)
        db.commit()
        #print(row['post_id'], row['text'], row['post_text'], row['shared_text'], row['time'], row['likes'], row['comments'], row['shares'], row['link'], row['jobs_info'] )



cursor.execute("select * from raw_indeed_scrape")
myresult = cursor.fetchall()
for i in myresult:
    print(i)

'''




