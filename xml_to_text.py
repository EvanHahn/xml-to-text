#!/usr/bin/env python

from sys import argv
from bs4 import BeautifulSoup

def xml_to_text(file):
    return BeautifulSoup(file).get_text()

if __name__ == "__main__":
    if len(argv) < 2:
        print "What file should I get plain text from?"
        exit(1)
    print xml_to_text(open(argv[1]))
