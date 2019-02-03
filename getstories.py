#/usr/bin/env python 3.6

import xml.etree.ElementTree as ET
tree = ET.parse('rss_topstories.xml')
root = tree.getroot()
import sys

for item in root.findall('./channel/item'):
    title = item.find('title').text  
    summary = item.find('description').text  
    news = title + summary
    sys.stdout.write(str(news) + '\n')








