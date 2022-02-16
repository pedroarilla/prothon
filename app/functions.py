#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules
import os
import sys
import time
import json
from app.classes import *

# Cleans the screen and prints app masthead
def masthead():
    os.system("cls" if os.name == "nt" else "clear")
    prothon = " PROTHON" + colour.grey + app.version + colour.default
    print "========================================"
    print "|            " + prothon  + "           |"
    print "========================================"
    print "\r"

# Prints a simple dot animation (loading)
def dotdotdot(x):
    for dot in range(x):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.3)

# Prints projects list
def projectsList(active):
    # Dumping JSON file into dictionary
    with open("data/projects.json") as f:
        dictionary.projects = json.load(f)
    # Nothing to see here, boy
    a = 1
    archived = 0
    while a <= len(dictionary.projects):
        if dictionary.projects[str(a)]["active"] == "False":
            archived += 1
        a += 1
    if active and len(dictionary.projects) == 0 or not active and archived == 0:
        pass
    # List of projects and times
    else:
        print "{:4}{:7}{:20}".format(" #", "HH:MM", "Project")
        print "-" * 40
        i = 1 # iterative element in dictionary
        j = 1 # index element for the list
        list.projects = [] # reset list
        while i <= len(dictionary.projects):
            s = int(dictionary.projects[str(i)]["time"])
            m, s = divmod(s, 60)
            h, m = divmod(m, 60)
            # Do we want to show active or archived projects?
            if active and dictionary.projects[str(i)]["active"] == "True" or not active and dictionary.projects[str(i)]["active"] == "False":
                print "{:2}{:2}{:02d}:{:02d}{:2}{:20}".format(j, "", h, m, "", dictionary.projects[str(i)]["name"])
                list.projects.append(i)
                j += 1
            i += 1
        # Since there are 1 project or more, showing here the menu option to select a project
        print "\a"
        print "\r[#] Select project nº #"

# Prints tasks list within a project
def tasksList(project, active):
    # Dumping JSON file into dictionary
    with open("data/projects.json") as f:
        dictionary.projects = json.load(f)
    # Loading tasks
    dictionary.tasks = dictionary.projects[project]["tasks"]
    # Nothing to see here, boy
    if len(dictionary.tasks) == 0:
        pass
    # List of tasks and times
    else:
        print "{:4}{:7}{:20}".format(" #", "HH:MM", "Task")
        print "-" * 40
        i = 1
        while i <= len(dictionary.tasks):
            s = int(dictionary.tasks[str(i)]["time"])
            m, s = divmod(s, 60)
            h, m = divmod(m, 60)
            print "{:2}{:2}{:02d}:{:02d}{:2}{:20}".format(i, "", h, m, "", dictionary.tasks[str(i)]["name"])
            i += 1
        # Since there are 1 task or more, showing here the menu option to select a task
        print "-" * 40
        timeS = int(dictionary.projects[project]["time"])
        timeM, timeS = divmod(timeS, 60)
        timeH, timeM = divmod(timeM, 60)
        print "TOTAL TIME: " + str(timeH) + "h " + str(timeM) + "m"
        print "\a"
        if active:
            print "\r[#] Select task nº #"
