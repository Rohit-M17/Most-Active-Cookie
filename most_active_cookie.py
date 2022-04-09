# import csv
# from multiprocessing.sharedctypes import Value
from multiprocessing.sharedctypes import Value
from operator import countOf
from re import search
import sys
from sys import argv
import csv
from datetime import datetime
import time
# import pytz
# import collections
# import re

class my_dictionary(dict):
    def __init__(self):
        self = dict()
    def add(self, key, value):
        if key in self:
            self[key] += 1
        else: 
            self[key] = 1
            
         


# Program asks for most active cookie, I misinterpreted it as a function to find most frequently
# visited cookie which I picked up from rereading the spec
def findMostFreqCookie(cookieFrequencyDict):
    # how to get max values from a dictionary python
    return [key for key, value in cookieFrequencyDict.items() if value == max(cookieFrequencyDict.values())]


def mainCodeProcess(csvFileName, dateToSearch):    
    # Dictionary that will store cookieId as a key and the frequency as a value 
    cookieFrequencyDict = my_dictionary()
    # Open and read CSV File from the arguement vector
    cookieCSV = open(csvFileName, 'r')
    # Comma Separated
    cookiesList = []
    reader = csv.reader(cookieCSV, delimiter=",")
    header = next(reader)
    searchInput = datetime.strptime(dateToSearch, "%Y-%m-%d")
    for column in reader:
        # https://thispointer.com/convert-local-datetime-to-utc-timezone-in-python/
        # https://jeffkemponoracle.com/2021/03/comparing-timestamps-with-time-zone/
        # Link I used to realize how to compare timestamps. I initially didn't realize the importance of checking the timezone when comparing
        # the times. I only remembered last minute because in my internship last summer I had to plan meetings with members on my team from different countries
        # I need to convert the timestamps so that they are in a common timezone (decided to use UTC since this is what the user enters in the terminal)
        cookieId = column[0]
        timeStamp = column[1]
        timeStamp = timeStamp.replace('T', '-')
        timeList = timeStamp.split('+')
        timeList[1] = timeList[1].replace(':', '')
        temp = timeList[0] + '+' + timeList[1]
        temp = datetime.strptime(temp, "%Y-%m-%d-%H:%M:%S%z")
        # I converted the timestamps to UTC so it would make sense for future functions if we wanted to compare times with one another
        # outside the scope of this assessment but I found it interesting to learn how to do this with the pytz library
        # temp = temp.astimezone(pytz.utc)
        if((searchInput.year == temp.year) and (searchInput.month == temp.month) and (searchInput.day == temp.day)):
            cookieFrequencyDict.add(cookieId, 0)

    if len(cookieFrequencyDict) == 0:
        print("Could not find cookies at the specified date")
        exit()
    # Make sure you close the CSV file after you are done using it!!
    cookieCSV.close()
    # Assume UTC time from input
    return ((', ').join(findMostFreqCookie(cookieFrequencyDict)))

# Main that calls the functions
# If the number of arguements that are passed in are greater, end the Program and display message
# 
# Logic for making sure the user is inputting the correct number of inputs to use this function commentted this logic out so it 
# does not interfere with my unittests
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ------------------------------------Comment out this section when Running UNIT TESTS!!!!!!!!!!! (uncomment when using)----------------------------------
numArguements = len(sys.argv)
if numArguements != 4:
    print("Opps!, there is one too many arguements for this command. Please make sure you include the python code file, csv file, -d, and timestamp")
    exit()
dateToSearch = argv[3]
csvFileName = argv[1]
print(mainCodeProcess(csvFileName, dateToSearch))
# -------------------------------------------------------------------------------------------------------------------------------------------------------














# --------------------------------------------------------------------------------------------------------------------
# My first approach was to parse the csv file and then store it in a dictionary but I quickly realized that this 
# function is supposed to work as a commandline program for quick and immediate use, not for storing and doing a query on later which I normally
# had to do in my last internship,so I abandoned this approach and decided to store the latest cookie ID as soon as I read the file. I want to know the most recent 
# cookie on the first read to make sure the runtime of this program is optimized
# --------------------------------------------------------------------------
#------------------ Old Approach (IGNORE)-----------------------------------------
# # Dictionary Class data structure for ordering file
# # Hashmaps are faster as size increases in comparison to arry lists,
# # this will be handy when working with larger Cookie files
# class my_dictionary(dict):
#     def __init__(self):
#         self = dict()
#     # Ran into problem with duplicate key values so I added logic to handle this situation
#     # Important to include duplicates in my data structure incase future coding question asks for me to find the most visited Cookie?
#     def add(self, key, value):
#         if key not in self:
#             self[key] = [value]
#         elif isinstance(self[key], list):
#             self[key].append(value)
#         else:
#             self[key] = [self[key], value]
            
# # # Initialization of my dictionary
# dict_obj = my_dictionary()
# -----------------END OF OLD APPROACH-------------------------------------

# Though process items (irrelavant) 
# -----------------------------------
    # No longer using dictionary approach
# mostrecentId = "Couldn't find the most recent cookie for the specified date"
# temp = " "
# mostrecentTimeStamp1 = '99:99:99+99:99'
# mostrecentTimeStamp2 = '99:99:99+99:99'
# for key in dict_obj:
#     for i in dict_obj[key]:
#         print(key, dict_obj[key])   
#         if(i[0] == "2020-12-08"):
#             mostrecentTimeStamp2 = i[1]
#             mostrecentTimeStamp2 = datetime.strptime(str(mostrecentTimeStamp2),"%H:%M:%S:!+:%f")
#             print(mostrecentTimeStamp2)
#             mostrecentTimeStamp1 =max(mostrecentTimeStamp1, mostrecentTimeStamp2)
# print(mostrecentTimeStamp1)
# for i in range(len(sys.argv)):
#     print(i, ": " , argv[i])
# print(len(sys.argv))
# ----------------------------------- 
