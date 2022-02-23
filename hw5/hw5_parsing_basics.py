#! /usr/bin/env python
import requests
import csv
import sys
import string
import os
from bs4 import BeautifulSoup as bs
filename = './ITNserver.csv'
fn = open(filename, 'w+', errors ='ignore', newline = '')
csv_writer = csv.writer(fn)
url_ = 'https://www.ltn.com.tw/'
res_ = requests.get(url_)
soup_ = bs(res_.text,'html.parser')
tag_name_ = 'div.news12.boxTitle p'
articles_ = soup_.select(tag_name_)
for index in articles_:
    new = [index.text]
    csv_writer.writerow(new)
fn.close()
