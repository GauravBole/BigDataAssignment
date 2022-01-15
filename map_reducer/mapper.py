#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
        line = line.strip()
        words = line.split()

        for word in words:
                print("{}       {}".format(word, 1))
