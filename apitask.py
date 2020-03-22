import pandas as pd
from pandas.io.json import json_normalize
import calendar
from datetime import date
from datetime import timedelta
from datetime import datetime
import os, sys
import requests
import json
import csv
import codecs
import sys


FILE_LOC = 'C:\\Temp\\data.csv' #The location in which the dynamic data file will be saved
FILE_LOC1 = 'C:\\Temp\\3channel_data.csv' #The location in which the static data file will be saved
GET_CHANNELS_API = 'https://fvau-api-prod.switch.tv/content/v1/channels' #To get the list of Channels from the given link
GET_PROGRAMS_API = 'https://fvau-api-prod.switch.tv/content/v1/epgs/' #To get the list of programs in the given channel
todays_date = date.today() #To get current system date
next_six_days = date.today() + timedelta(days=5) #To check the system date for next six days
is_three_channel_data = 'false'


#To Remove the data file if its alrady available in the location
def rem_files():
    """Remove the existing file when the program begins
    """
    file_exists = os.path.isfile(FILE_LOC)
    if file_exists:
        os.remove(FILE_LOC)

    file_exists = os.path.isfile(FILE_LOC1)
    if file_exists:
        os.remove(FILE_LOC1) 

#To get the list of channel and display the channel name and its corresponding dvb_triplet
def get_channelsdata():    
    
    requestdata = requests.get(GET_CHANNELS_API) #To send the request
    response = requestdata.json() #To get the response
    df=json_normalize(response['data']) #To store the response data
    
    print("List of channels with dvb_triplet")
    print(df['channel_name']+' '+df['dvb_triplet'])
    
#To get the list of Programs for the corresponding dvb_triplet
def get_epgdata():
        
    epg = input("Enter a dvb_triplet to display list of shows for the next 6 days: ")
    print("File saved to C:\Temp\data.csv location")
    return epg

#To get list of programs for the selected dvb_triplet from the current system date to next seven days    
def get_programsdata(epg,todays_date,next_six_days,is_three_channel_data):
    
    build_get_programs_api = GET_PROGRAMS_API+str(epg)+'/?start='+str(todays_date)+'&end='+str(todays_date)+'&limit=100&sort=start'
    requestdata = requests.get(build_get_programs_api)
    response = requestdata.json()    
    df=json_normalize(response['data'])
     
    if is_three_channel_data == 'false': 
        df.to_csv(FILE_LOC,header=False, index=False, mode='a')
    else: 
        df.to_csv(FILE_LOC1,header=False, index=False, mode='a')
#To check the program list for the six days from the current system date                
    if todays_date<=next_six_days:        
        todays_date=todays_date+ timedelta(days=1)        
        get_programsdata(epg,todays_date,next_six_days,is_three_channel_data)
    
    
#Statically save the dvb_triplet data for the given epg records below, this epg values can be changed     
def get_3channeldata(epg,todays_date,next_six_days):

    print("Fetching 3 channels data")
    
    is_three_channel_data = 'true'    #I want to save this data in a new file
    #9Gem - This can be changed manually here
    epg='1012:0400:040A'   
        
    get_programsdata(epg,todays_date,next_six_days,is_three_channel_data)
    
    
    #9Go! - This can be changed manually here
    epg='1012:0400:040B'   
       
    get_programsdata(epg,todays_date,next_six_days,is_three_channel_data)

    
    #ABC - This can be changed manually here
    epg='1010:0211:0211'   
        
    get_programsdata(epg,todays_date,next_six_days,is_three_channel_data)
    
    print("File saved to C:\Temp\\3channel_data.csv location")
    

def main():
    remfile = rem_files()
    channels = get_channelsdata()
    epg = get_epgdata()
    programs = get_programsdata(epg,todays_date,next_six_days,is_three_channel_data)
    threechanneldata = get_3channeldata(epg,todays_date,next_six_days)
    

if __name__ == '__main__':
    main()
