import csv
import os
import random
import string
import pandas as pd
 
currMonth = 6
currYear = 7
 
def get_months_since(start,years):
                amount = 0
 
                if years == 4:
                        amount = currMonth + (3*12) + (12 - start)
                elif years == 3:
                        amount = currMonth + (2*12) + (12 - start)
                elif years == 2:
                        amount = currMonth + 12 + (12 - start)
                elif years == 1:
                        amount = currMonth + (12 - start)
                elif years == 0:
                        amount = currMonth
                return amount
 
def get_random_string():
                rnstring = ''
                for i in range(0,450):
                        rnstring += random.choice(string.ascii_letters)
                        # print (rnstring)              
                return rnstring
 
get_random_string()
 
def get_file_path(filename):
                currdirpath = os.getcwd()
                file_path = os.path.join(os.getcwd(),filename)
                print (file_path)
                return file_path
 
path = get_file_path('dataset_main.csv')
 
def read_csv(filepath):
        with open(filepath, 'rU') as f:
                with open('output.csv', 'w') as csvoutput:
                        writer = csv.writer(csvoutput, delimiter=',', lineterminator='\n')
                        writer.writerow(('Username', 'Collector','Arrears','Loan_Maturity'))
 
                        reader = csv.DictReader(f)
                        headers = reader.fieldnames
                        headers = set(headers)
                        behindList = []
                        collectors = []
                        usernames = []
                        loanMaturities = []
                        for row in reader:
                                month, date, year = row['loan_start_date'].split("/")
                                totalMonths = get_months_since(int(month),currYear - int(year[3]))
                                shouldHave = totalMonths*(int(row['monthly_loan_payment']) + int(row['monthly_sdl_payment'])
                                                + int(row['monthly_twu_payment']))
                                havePaid =(int(row['total_collected_loan']) + int(row['total_collected_sdl'])
                                                + int(row['total_collected_twuf']))
                                behind = int(shouldHave) - int(havePaid)
                                                               
                                behindList.append(behind)
                                collectors.append(row['Collector'])
                                usernames.append(row['username'])
                                loanMaturities.append(totalMonths)
 
                        rows = zip(usernames,collectors,behindList,loanMaturities)
                        for r in rows :
                        writer.writerow(r)
 
read_csv(path)