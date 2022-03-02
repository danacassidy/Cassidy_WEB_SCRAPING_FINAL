
# # Scraping Deathrow Inmates - Florida Department of Corrections
# ### By: Dana Cassidy

from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup
import re
import time
import csv
import requests



my_url = 'http://www.dc.state.fl.us/OffenderSearch/deathrowroster.aspx'

def scrape_links(my_url):
    res = requests.get(my_url)
    soup= bs4.BeautifulSoup(res.text,"html.parser")

        # collect every row in our soup
    inmate_rows = soup.find_all("tr")

        # make a blank list that we will append our information to
    inmate_links = []

        # for every row in our list inmate_rows, we are going to take all of the table data we need in a try and except. 
        #This try and except exists because some rows don't have the proper data we are looking for and will throw errors unless we stop them ahead of time.
    for row in inmate_rows:

        try:
                   # getting our table data
                a_inmate = row.find("a")
                href_inmate = a_inmate.get("href")
                    #let's make a dictionary. We can assign keys and attributes to ensure that we're inputting the right info into our CSV
                    # we're also going to strip our text because it's really ugly if we don't.
                inmate_links.append(href_inmate)
        except:
                continue

    return inmate_links 



## setting everything up for our inmates' information

filename = 'inmateinfo_dana_webscrapingproject_output.csv' 

column_headings = ['DC Number', 'Name', 'Race', "Sex", "Birth Date", "Inititial Receipt Date", "Current Facility",
                      "Current Custody", "Current Release Date", "Custody Status","Visiting Request Form - Part 1", 
                   "Visiting Request Form - Part 2", "How to Apply for Visitation", "Detainer Information"]

csvfile = open(filename, 'w', newline='', encoding='utf-8')

c = csv.writer(csvfile)
c.writerow(column_headings)




## function to scrape each inmates' information

def scrape_info(my_url):
    inmate = []
    combo_url = ("http://www.dc.state.fl.us/" + str(my_url))
    page =requests.get(combo_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find("table", class_="offenderDetails")
    data = table.find_all("td")
    
    for cell in data:
        if cell.find("a") in cell:
            a_tag = cell.find("a")
            href_link = a_tag.get('href')
            inmate.append(href_link)
            
        elif cell.find("a") not in cell:    
            cleaned_inmate = cell.get_text().strip()
            inmate.append(cleaned_inmate)
        else:
            inmate.append("n/a")
    
    c.writerow(inmate)



## looping through our list return output of links to scrape each inmate's information

for link in inmate_links:
    scrape_info(link)



## repeating the same process in the steps above except with the collection of offenses in mind.

offense_column_headings = ["DC Number","Offense Date", "Offense", "Sentence Date", "County",
                      "Case No.", "Prison Sentence Length"]


filename = 'offenseinfo_dana_webscrapingproject_output.csv' 


csvfile = open(filename, 'w', newline='', encoding='utf-8')

c = csv.writer(csvfile)
c.writerow(offense_column_headings)



## scraping every offense listed for inmates. Each offense is paired with a DC Number that matches the correct inmate.
def offense_scrape(my_url):
    combo_url = ("http://www.dc.state.fl.us/" + str(my_url))
    page =requests.get(combo_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    big_table = soup.find("table", class_ = "dcCSStableAlias")
    table = big_table.find_all("tr")
    
    for row in table:
        offense_row = []
        if row.find("td") in row:
            data = row.find_all("td")
            
            #appending the DC number to our row in order to indentify who committed what offense
            DC_number= soup.find("td")
            offense_row.append(DC_number.text)
            
            for d in data:
                cleaned_offense_row = d.get_text().strip()
                offense_row.append(cleaned_offense_row)
            c.writerow(offense_row)
            
        else:
            continue



## looping through our partial links to scrape the offenses information
for link in inmate_links:
    offense_scrape(link)




