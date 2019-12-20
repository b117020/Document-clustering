# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:14:43 2019

@author: Devdarshan
"""

#import modules
import csv
import pandas as pd
from nltk import tokenize

#read data
df = pd.read_csv('mueller_report.csv')
df = df['text']
df = df.tolist()

#converting into text file
with open('text.txt', 'w',encoding="utf-8") as f:
    for item in df:
        f.write("%s " % item)
        
#removing special characters        
s = open('text.txt','r').read()
s = ' '.join(s.split())
chars = ('$','%','^','*','"','@',':','/','>','<','~','#','&','^','-','_','(',',',')','`') # etc
for c in chars:
  s = ' '.join( s.split(c) )
out_file = open('cleaned.txt','w')
out_file.write(s)
out_file.close() 

#extracting sentences and saving into csv file       
fp = open("cleaned.txt")
data = fp.read()
txt = tokenize.sent_tokenize(data)
dfr = pd.DataFrame(txt)
dfr.to_csv('sentences.csv', index=False)

#removing non-ascii characters
file = pd.read_csv('sentences.csv')
def replace_trash(unicode_string):
     for i in range(0, len(unicode_string)):
         try:
             unicode_string[i].encode("ascii")
         except:
              #means it's non-ASCII
              unicode_string=unicode_string.replace(unicode_string[i]," ") #replacing it with a single space
     return unicode_string
file['data'] = file['data'].apply(replace_trash)
file.to_csv('preprocessed.csv', index=False)

#removing periods and extra spaces
with open("preprocessed.csv", "r") as infile, open("final.csv", "w") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    conversion = set('_"/;.$')
    for row in reader:
        newrow = [''.join('' if c in conversion else c for c in entry) for entry in row]
        writer.writerow(newrow)
af = pd.read_csv('final.csv')
modifiedDF = af.dropna() 
modifiedDF.to_csv('final.csv',index=False)

#converting data to lower case and saving 
data = pd.read_csv("final.csv") 
data["data"]= data["data"].str.lower() 
data.to_csv('final1.csv', index=False)