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
        with open(os.path.join("data", "projects.json"), "wb") as temp_file:
            temp_file.write(json_default)

# Prothon's core
def mainMenu():
    while True:
        masthead(True)
        projectsList(True)
        # Selection menu
        print "[N] New project"
        print "[A] Archive"
        print "[S] Stats"
        print "[E] Exit\r"
        selection = raw_input("\n>>> Select an option: ").lower()
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "n":
                newProjectMenu()
            if selection.lower() == "a":
                archiveMenu()
            if selection.lower() == "s":
                statsMenu()
            if selection.lower() == "e":
                break
        else:
            if int(selection) <= len(dictionary.projects) and dictionary.projects[selection]["active"] == "True":
                if int(selection) <= 0:
                    True
                else:
                    projectMenu(selection)

# Project menu
def projectMenu(project):
    while True:
        masthead(True)
        # Selection menu
        print "PROJECT MENU"
        selection = raw_input("\n>>> Select an option: ")
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "b":
                break

# New project menu
def newProjectMenu():
    while True:
        masthead(True)
        print "CREATE NEW PROJECT"
        print "-" * 40
        projectName = raw_input("\nProject name: ")
        # Adding project to file
        createProject(projectName)
        # Showing that the project has been created
        print "Creating project",
        dotdotdot(5)
        break

# Archive menu
def archiveMenu():
    while True:
        masthead(True)
        print "ARCHIVE"
        print "-" * 40
        projectsList(False)
        # Selection menu
        print "[B] Back\r"
        selection = raw_input("\n>>> Select an option: ")
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "b":
                break
        else:
            if int(selection) <= len(dictionary.projects) and dictionary.projects[selection]["active"] == "False":
                if int(selection) <= 0:
                    True
                else:
                    unarchiveMenu(selection)

# Unarchive menu
def unarchiveMenu(project):
    while True:
        masthead(True)
        # Selection menu
        print "PROJECT: " + dictionary.projects[project]["name"]
        print "-" * 40
        # Show stats
        print "stats.............\r"
        # Selection menu
        print "[U] Unarchive"
        print "[B] Back\r"
        selection = raw_input("\n>>> Select an option: ")
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "b":
                break

# Stats menu
def statsMenu():
    while True:
        masthead(True)
        # Selection menu
        print "STATS MENU"
        selection = raw_input("\n>>> Select an option: ")
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "b":
                break

# Closes session
def closeSession():
    print "\nClosing session",
    dotdotdot(3)
    print " Done."
    print "See you later! " + emoji.bye.decode("unicode-escape") + "\n"
