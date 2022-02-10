#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules
import os
import sys
import time
import json
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
    # Dumping JSON file into dictionary
    with open("data/projects.json") as f:
        dictionary.projects = json.load(f)
    # Nothing to see here, boy
    if len(dictionary.projects) == 0:
        pass
    # List of projects and times
    else:
        print "{:4}{:7}{:20}".format(" #", "HH:MM", "Project")
        print "-" * 40
        i = 1
        while i <= len(dictionary.projects):
            s = int(dictionary.projects[str(i)]["time"])
            m, s = divmod(s, 60)
            h, m = divmod(m, 60)
            print "{:2}{:2}{:02d}:{:02d}{:2}{:20}".format(i, "", h, m, "", dictionary.projects[str(i)]["name"])
            i += 1
        print "\a"
        # Since there are 1 project or more, showing here the menu option to select a project
        print "\r[#] Select project nº #"

# Creates a new project
def createProject(projectName):
    project = [len(dictionary.projects)+1, projectName, 0, True]
    dictionary.projects[str(project[0])] = {"name": project[1], "time": str(project[2]), "active": str(project[3])}
    with open("data/projects.json", "w") as f:
        json.dump(dictionary.projects, f)
