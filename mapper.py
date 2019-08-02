import sys
import re

for line in sys.stdin:
    line = " ".join(re.findall("[a-zA-Z]+", line))
    line=line.lower()
    line = line.strip()
    words = line.split()
    if len(line) > 1:
        for word in words:
            print ('%s\t%d' % (word, 1))
