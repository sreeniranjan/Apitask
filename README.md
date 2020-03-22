# API AUTOMATION TASK

API automation task is a test project build with the python basics to check the API request and response for the server details mentioned below. The python code is run in Command prompt or Windows PowerShell to view the list of TV guide for selected channel in *.csv format.

Initially Postman tool was used to get the Request and Response JSON.

Pandas Library was used in python as it helpful in data manipulation and analysis. Below code is used to install the pandas library.

```bash
pip install pandas
```

## User Story

As a Freeview Web user, I want to be able to view the TV Guide for all available channels, so that I can have an overview of what is scheduled for the following week and plan which
shows to watch

## Basic Test cases that can be verified
1.	To verify the sorting order of dvb_triplet based on the system date,
2.	To verify list of programs for the given dvb_triplet in the data.csv file,
3.	To verify list of programs for the given dvb_triplet from current system date to next six days in the data.csv file.
4.	To verify the list of program for the static data given inside the source code namely [9Gem- epg’1012:0400:040A’, 9Go! – epg’1012:0400:040B’, ABC- epg‘1010:0211:0211’] in 3channel_data.csv file.
5.	To verify the list of programs for the static data given inside the source code from current system date for next six days in 3channel_data.csv file.
6.	To verify deletion of the old of old data.csv and 3channel_data.csv file when a new dvb_triplet is queried in the Command prompt or Windows PowerShell.

[Server Detail](https://fvau-api-prod.switch.tv/)


## URL for GET Request

[To get the EPG Data](https://fvau-api-prod.switch.tv/content/v1/epgs/) 
 
[To get the list of channels](https://fvau-api-prod.switch.tv/content/v1/channels/?limit=3)

[To get the list of program for a channel from current system date to next date](https://fvau-api-prod.switch.tv/content/v1/epgs/3202:0300:0301/?start=2020-03-23&end=2020-03-24&limit=100&offset=0&more=true&sort=start)   

