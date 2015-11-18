# example of program that calculates the number of tweets cleaned
import json
import re
import os
import sys

def ft1(source, target):
    unicodes=0
    file=open(target,"a")
    for line in open(source, 'r').readlines():
        if ('created_at' not in cleanString(line) or 'text' not in cleanString(line)):
            break
        else:
            tstamp=cleanString(line)['created_at']
            value=cleanString(line)['text']
            if (onlyAscii(value)):
                value=transformString(value, True)
                else:
                    value=transformString(value)
                    unicodes+=1
                st="%s (tstamp: %s) \n" % (value, tstamp)
                file.write(st)
def cleanstring(tweetline):
    arr=re.compile(r":(false|true|null),")
    newline=arr.sub(r':"\1",',tweetline)
    json=json.loads(newline)
    return json

def onlyAscii(txt):
    asciiline = len(txt.decode('unicode_escape').encode('ascii', 'ignore')) 
    uniline = len(txt.encode('ascii', 'ignore').decode('escape')) 
        
        return asciiline == uniline

def transform(txt, onlyescapes=False):
    if (not onlyescapes):
        txt=''.join([x for x in txt if ord(x) < 128])
        txt = re.sub(r'\s+|\r|\n|\t',' ',txt)
        tot = re.compile(r'(\\|\n){1,}(.)')
        return tot.sub(r'\2',text)
