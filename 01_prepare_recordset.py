#create a sample file

#import header
import csv
from random import randint
import configparser
import os
#open a file 
file = open(os.path.join('Dataset','customermaster.dat'),'a')
fwriter = csv.writer(file,delimiter=',')

#read from config file
cfg = configparser.RawConfigParser()
cfg.read(os.path.join('config','configurationfile.ini'))

minsalarya = cfg.getint('mastercustomerdescription','minsalary')
maxsalarya = cfg.getint('mastercustomerdescription','maxsalary')

for i in range(1,100,):
	customername = 'a'
	customersalary = randint(minsalarya,maxsalarya)
	customerid = i
	customerrecord = customername  + ' ' + str(customersalary) +  ' '+str(customerid)
	fwriter.writerow(customerrecord.split())

file.close()