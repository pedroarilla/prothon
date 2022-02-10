#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules
import os
import json
from app.functions import *
from app.classes import *

# Checks files structure
def checkFiles():
    if not os.path.exists("data"):
        os.makedirs("data")
        json_default = "{}"
        with open(os.path.join("data", "archive.json"), "wb") as temp_file:
            temp_file.write(json_default)
        with open(os.path.join("data", "projects.json"), "wb") as temp_file:
            temp_file.write(json_default)
        with open(os.path.join("data", "stats.json"), "wb") as temp_file:
            temp_file.write(json_default)

# Pomothon's core
def mainMenu():
    while True:
        masthead(True)
        # Selection menu
        print "[P] Personal project"
        print "[W] Work project"
        print "[E] Exit\r"
        project.nature = raw_input("\n>>> Select an option: ").lower()
        if project.nature == "p":
            project.file = "data/personal.json"
            project.message = "> PERSONAL FILE\n"
        elif project.nature == "w":
            project.file = "data/work.json"
            project.message = "> WORK FILE\n"
        elif project.nature == "e":
            break
        else:
            continue
        # Dumping JSON file into dictioanry
        with open(project.file) as f:
            project.dict = json.load(f)
        projectsMenu()

# Projects menu
def projectsMenu():
    while True:
        masthead(True)
        projectsList()
        # Selection menu
        print "[#] Work on # (project)"
        print "[M] Manage projects"
        print "[B] Back\r"
        project.select = raw_input("\n>>> Select an option: ")
        try:
            int(project.select)
        except ValueError:
            if project.select.lower() == "m":
                manageMenu()
            if project.select.lower() == "b":
                break
        else:
            if int(project.select) <= len(project.dict):
                if int(project.select) <= 0:
                    True
                else:
                    timerMenu()

# Timer menu
def timerMenu():
    while True:
        masthead(True)
        print "> PROJECT NAME\n" # To-do: print real name
        # Selection menu
        print "[T] Timer"
        print "[P] Pomodoro"
        print "[M] Manual record"
        print "[B] Back\r"
        project.timer = raw_input("\n>>> Select an option: ").lower()
        if project.timer == "t":
            print "\nTiming",
            dotdotdot(3)
            print " Done."
        elif project.timer == "p":
            print "\nPomodoring",
            dotdotdot(3)
            print " Done."
        elif project.timer == "m":
            print "\nRecording",
            dotdotdot(3)
            print " Done."
        elif project.timer == "b":
            break
        else:
            continue

# Manage menu
def manageMenu():
    while True:
        masthead(True)
        # Selection menu
        print "[C] Create project"
        print "[R] Rename project"
        print "[A] Archive project"
        print "[U] Unarchive project"
        print "[B] Back\r"
        project.manage = raw_input("\n>>> Select an option: ").lower()
        if project.manage == "c":
            print "\nCreating",
            dotdotdot(3)
            print " Done."
        elif project.manage == "r":
            print "\nRenaming",
            dotdotdot(3)
            print " Done."
        elif project.manage == "a":
            print "\nArchiving",
            dotdotdot(3)
            print " Done."
        elif project.manage == "u":
            print "\nUnarchiving",
            dotdotdot(3)
            print " Done."
        elif project.manage == "b":
            break
        else:
            continue

# Closes session
def closeSession():
    print "\nClosing session",
    dotdotdot(3)
    print " Done."
    print "See you later! " + emoji.bye.decode("unicode-escape") + "\n"
