# example of program that calculates the average degree of hashtags
import os
import re
import sys
import time
import itertools
from igraph import *
from datetime import datetime


def ft2(source,target):
    f = open(target, "a")                   
    mast = []                                 
    last = []                                 
    for line in open(source,'r').readlines(): 
        edg = []                              
        tw = cleanData(line)                 
        if(tw):                              
            last.append(tw)                     
            while ((last[-1]['timestamp'] - last[0]['timestamp'] > 60) and (last[-1]['timestamp'] > last[0]['timestamp'])):
                del last[0]                    
            add = uniqueTags(mast, tw['tags'])   
            mast.extend(add)                     
            edg = list(set(itertools.chain.from_iterable([i['edges'] for i in last])))
            average_degree = createGraph(edg, mast)
            f.write(str(average_degree)+'\n')   
def clean(time):
    
    
    date_format= '%a %b %d %H:%M:%S %Y'                   
    stripping = re.sub(r"[+-]([0-9])+", "", time)  
    
    t = datetime.strptime(stripping, date_format)        
    
    return int(time.mktime(t.timetuple()))                  

def clean(line):
    hashtags_p = re.compile(r'(#\w{1,})')               
    timestamp_p= re.compile(r'\(timestamp: (.*)\)') 
    
    hashes = set([x.lower() for x in hashtags_p.findall(line)]) 
    tstamp = timestamp_p.findall(line)      
    
    has = list(hashes)                      
    
    try:    
        tim = Timestamp(match_tstamp[0]
    except Exception:
        tim = '0000000000'
        
    im = list(itertools.combinations(hashes,2))         
    
    if len(hashesh) > 1:                                 
        return {"tags": h, "timestamp": t, "edges": e}  

def unique(tw1, tw2):
    
    
    int = [val for val in tw2 if val in tw1]             
    diff = [val for val in tw2 if val not in intersection] 
    
    return diff

def createGraph(im,mast):
    gr = Graph()                             
    
    for i in mast: gr.add_vertex(i)         
    for i in im: gr.add_edge(i[0],i[1])      
    
    try:
        return round(sum(gr.degree())/float(len(gr.degree())),2) 
    except Exception:
        return 0


