#create a sample file

#import header
import csv
from random import randint
import configparser
import os

#create customer master data file
#open a file 
file = open(os.path.join('Dataset','customermaster.dat'),'a')
fwriter = csv.writer(file,delimiter=',')

#read from config file
cfg = configparser.RawConfigParser()
cfg.read(os.path.join('config','configurationfile.ini'))

minsalarya = cfg.getint('mastercustomerdescription','minsalary')
maxsalarya = cfg.getint('mastercustomerdescription','maxsalary')
custidmin = cfg.getint('transactiondata','customeridmin')
custidmax = cfg.getint('transactiondata','customeridmax')

for i in range(custidmin,custidmax):
	customername = 'a'
	customersalary = randint(minsalarya,maxsalarya)
	customerid = i
	customerrecord = customername  + ' ' + str(customersalary) +  ' '+str(customerid)
	fwriter.writerow(customerrecord.split())

file.close()

#create transaction file
file=open(os.path.join('Dataset','transactiondata'),'a')
