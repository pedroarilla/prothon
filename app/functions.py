#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules
import os
import sys
import time
from app.classes import *

# Cleans the screen and prints app masthead
def masthead(escape):
    os.system("cls" if os.name == "nt" else "clear")
    pomothon = " POMOTHON" + colour.grey + app.version + colour.default
    print "========================================"
    print "|           " + pomothon + "           |"
    print "========================================"
    if escape:
        print "\r"
    else:
        print "\a"

# Prints a simple dot animation (loading)
def dotdotdot(x):
    for dot in range(x):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.3)

# Prints projects list
def projectsList():
    print project.message
    print "{:3}{:7}{:20}".format("#", "HH:MM", "Project")
    print "-" * 40
    i = 1
    while i <= len(project.dict):
        s = int(project.dict[str(x)]["time"])
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        print "{:1}{:2}{:02d}:{:02d}{:2}{:20}".format(x, "", h, m, "", project.dict[str(x)]["name"])
        i += 1
    print "\a"
