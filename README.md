# Scraping the Florida Department of Corrections 
### Link to the main URL in this project: http://www.dc.state.fl.us/OffenderSearch/deathrowroster.aspx

## Why scrape this page?

##### The goal of scraping this page is to collect information about the 300+ death row inmates for the Florida Department of Corrections. 

In the first CSV, this information includes an inmate's name DC#, race, gender, date recieved, crime(s), date of offense, date of sentence, date of birth, count, and links for visitiation access. In the second CSV, there is information about offenses, offense date, custody status, etc. These categorires allow those analyzing this information to better look at the makeup of those on death row. 

#### Some questions to think about while exploring the scraped data:
###### 1) What is the most common county in the dataset?
###### 2) What is the average age (based on the date of birth) of those on the roster?
###### 3) What is the most common crime committed? 
###### 4) What does the average death row inmate in Florida look like ? (Race, gender, age range, location, etc.)


## How it was done:
First, I collected all the partial URLs from each hyperlinked DC Number on the main page. This was fairly easy, as I initially found every table row on the main URL and then did a for loop to parse through the "a" tag and then the "href" tag within each. I did this all within a function.

I then appended the partial URL to a list. Because I had to find all of the desired table rows, there were some table rows that didn't consist of the data that I wanted, so I added a "try" and "except" to only collect the correct href links. If a row did not have the data I wanted, it would pass through the "except" and continue in our for loop. This is done in the "scrape_links" function. Having a function instead of just the code allows for different URLs to be put into the function.

We then run this function with our URL listed at the top of the readme.md file.

Next, I wanted to make a function to collect information about the inmates themselves. I would use each partial link to combine it with the static main link of the FDOC website to collect individual TD from an inamte's page. This information would be appended into a list. If a TD contained an "a" tag, then I would append the internal href link into that ongoing list, as these links are more useful than the actual text displayed for these cells about how to apply for visitation.

This was done in a "try" and "except" manner until every cell desired is collected. To make this function run, you have to open up the csv file, "inmateinfo_dana_webscrapingproject_output.csv", and create a csv.writer object, write the column headings rows, and then create a for loop to execute the "scrape_info" function for every partial link in inmate_link, which is the return output of the "scrape_links" function.

After I did this I essentially repeated the same steps (opening, writing the file and looping it through "scrape_links" returned list output) except this time I collected all the information on the offenses into a seperate csv called "offenseinfo_dana_webscrapingproject_output.csv."

This new function for offenses is called "offense_scrape", and takes a person's DC number and puts it in a list to then insert into a csv row with their offense data. I did this by searching for the "td" tag in a seperate category of the individual inmate pages. Once all the "TD" is found, it is cleaned and appened to a list. Once all information is found, cleaned, and appended, it is written into the csv.

## Unexpected problems:

The biggest frustration was figuring out how to properly collect all of the offenses for each inmate when each of them have a varied number of charges. It was eventually decided that the best course of action is to have two seperate CSVs and have the offenses identified by an inmate's DC number. This DC number exists in the inmate's info CSV and can be joined with the offenses info csv if someone desires to combine them.

I also had trouble collecting the proper TD, as a dictionary method did not work on individual pages.
