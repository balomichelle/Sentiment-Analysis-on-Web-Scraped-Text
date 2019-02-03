#/usr/bin/env python 3.6

# pip install snownlp
# pip install -U textblob
# python -m textblob.download_corpora

import sys
from textblob import TextBlob
import nltk
import numpy as np
import pandas as pd

data = sys.stdin.readlines()
def sentiment(data):
    df= pd.DataFrame(columns=['word','score'])
    for sentence in data:
        words = sentence.split()
        for word in words:
            blob = TextBlob(word)
            if blob.sentiment[0] > 0.0:
                df = df.append(pd.Series([word, 1], index = ['word','score']), ignore_index = True)
            elif blob.sentiment[0] < 0.0:
                df = df.append(pd.Series([word, -1], index = ['word','score']), ignore_index = True)
    df = df.sort_values(by='word') 
    df = df.reset_index(drop=True)
    # change dataframe into array to better calculate
    arrdf = df.values
    return arrdf


# Word Count Function, Reducer of Mapper.file
def do_map(mapper):
    reducer = np.array(['0','0'])
    prev_key = None
    key = None
    current_count = 0
    for line in mapper:
        key = line[0]
        count = line[1]
        count = int(count)
        if key == prev_key:
            current_count += count
        else:
            if prev_key:
                item = np.array([prev_key, current_count])
                reducer = np.vstack((reducer, item))
            current_count = count
            prev_key = key
    # store the last row in the mapper file 
    if key == prev_key:
        item = np.array([prev_key, current_count])
        reducer = np.vstack((reducer, item))
    reducer = np.delete(reducer,0, 0)
    return reducer

# output the aggregated scores for each word in the data
def output(reducer):
    for row in reducer:
        #item = row[0], row[1]
        #sys.stdout.write(str(item) + '\n')
        print( row[0], "," ,row[1])

if __name__ =="__main__":
    arrdf = sentiment(data)
    reducer = do_map(arrdf)
    output(reducer)




