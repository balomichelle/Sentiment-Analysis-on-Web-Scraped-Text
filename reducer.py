#/usr/bin/env python 3.6
import sys

data = sys.stdin.readlines()

def reducer(data):
    totalscore = 0
    pos = 0
    neg = 0
    for row in data:
        words = row.split(",")
        score = float(words[-1])
        if score > 0.0:
            pos += score
        else:
            neg += score
        totalscore += score
    print(totalscore)
    

if __name__ =="__main__":
    reducer(data)

