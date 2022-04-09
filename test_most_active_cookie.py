import unittest
import sys 
from sys import argv
import most_active_cookie
from most_active_cookie import mainCodeProcess, my_dictionary
import csv


# I learned that to test command line programs I should use argv.pop so 
# my unittest's parameters don't mess with my regular program's
class TestMost_active_cookie(unittest.TestCase):
    # def test_checkingTest1():
    def test_mainCodeProcess1(self):
        csvFileName = "cookie_log.csv"
        dateToSearch = "2018-12-09"
        # print(most_active_cookie.mainCodeProcess(csvFileName, dateToSearch))
        assert most_active_cookie.mainCodeProcess(csvFileName, dateToSearch) == "AtY0laUfhglK3lC7"

    def test_mainCodeProcess2(self):
        csvFileName = "cookie_log.csv"
        dateToSearch = "2018-12-08"
        # print(most_active_cookie.mainCodeProcess(csvFileName, dateToSearch))
        assert most_active_cookie.mainCodeProcess(csvFileName, dateToSearch) == "SAZuXPGUrfbcn5UA, 4sMM2LxV07bPJzwf, fbcn5UAVanZf6UtG"
    
    def test_mainCodeProcess3(self):
        csvFileName = "cookie_log.csv"
        dateToSearch = "2006-03-08"
        # print(most_active_cookie.mainCodeProcess(csvFileName, dateToSearch))
        assert most_active_cookie.mainCodeProcess(csvFileName, dateToSearch) == "XXXXXXXXXXXXXXXX"
if __name__ == " __main__":
    unittest.main()
    print("Everything passed!")
