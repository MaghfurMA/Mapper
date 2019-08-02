#!/usr/bin/env python


import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    if len(line) > 1:
        for word in words:
            print ('%s\t%d' % (word, 1))
            
            
for line in sys.stdin:
    words = line.split()
        for word in words:
            word = "".join(i for i in word if ord(i)==32 or 47<ord(i)<58 or 64<ord(i)<91 or 96<ord(i)<123)
          
          
for line in sys.stdin:
    words = line.split()
        for word in words:
            word = word.lower()
