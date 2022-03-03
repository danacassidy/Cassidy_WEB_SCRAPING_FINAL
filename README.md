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
First, I collected all the partial URLs from each hyperlinked DC Number on the main page. This was fairly easy, as I initially found every table row on the main URL and then did a for loop to find the "href" tag within each. 

Because I had to find all of the desired table rows, there were some rows that didn't consist of the data that I wanted, so I added a "try" and "except" to only collect the correct href links. If a row did not have the data I wanted, it would pass through the "except" and continue in our for loop. 

We then run this with our URL listed at the top of the readme.md file.

Next, I wanted to make a function to collect information about the inmates themselves. I would use each partial link in combination with the main link to the FDOC website to collect individual TD from an inmate's page. This information is then appended to a list called "inmate". 

This was done in a "try" and "except" manner until every cell is collected. To make this function run, you have to open up the csv file, "inmateinfo_dana_webscrapingproject_output.csv", and create a csv.writer object, write the column headings rows, and then use a for loop to run through the collected hrefs for every partial link in the inmate_link list.

After this, I essentially repeated the same steps (opening and writing the file to loop the output of a function for each inmate page through inmate_links) except this time I collected all the information of the offenses inmates committed into a seperate csv called "offenseinfo_dana_webscrapingproject_output.csv."

This new function for offenses is called "offense_scrape", and takes a person's DC number and appends it to a list to then write into a csv row alongside their offense data. This ensures that each offense and the offense details can be linked to a proper inmate. Once all of the table data is found, it is cleaned and appened to a list and written into the csv.

## Unexpected problems:

The biggest frustration was figuring out how to properly collect all of the offenses for each inmate when each of them have a varied number of charges. It was eventually decided that the best course of action is to have two seperate CSVs and have the offenses identified by an inmate's DC number. This DC number exists in the inmate's info CSV and can be joined with the offenses info csv if someone desires to combine them. I also had trouble collecting the proper TD at first, as a dictionary method did not work on individual pages.

I also realized at a certain point that my CSVs were not being written correctly because I inititally did not collect my partial links correctly. Once I fixed this, everything was perfect.

I also want to point out that GitHub does not like the comma in the "Name" column strings I have, hence why it says it needs more column names. It works perfectly in a traditional CSV format.

