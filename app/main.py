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

# Prothon's core
def mainMenu():
    while True:
        masthead(True)
        projectsList()
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
            if int(selection) <= len(dictionary.projects):
                if int(selection) <= 0:
                    True
                else:
                    projectMenu()

# Project menu
def projectMenu():
    while True:
        masthead(True)
        # Selection menu
        print "PROJECT MENU"
        project.select = raw_input("\n>>> Select an option: ")
        try:
            int(project.select)
        except ValueError:
            if project.select.lower() == "b":
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
        # Selection menu
        print "ARCHIVE MENU"
        project.select = raw_input("\n>>> Select an option: ")
        try:
            int(project.select)
        except ValueError:
            if project.select.lower() == "b":
                break

# Stats menu
def statsMenu():
    while True:
        masthead(True)
        # Selection menu
        print "PROJECT MENU"
        project.select = raw_input("\n>>> Select an option: ")
        try:
            int(project.select)
        except ValueError:
            if project.select.lower() == "b":
                break

# Closes session
def closeSession():
    print "\nClosing session",
    dotdotdot(3)
    print " Done."
    print "See you later! " + emoji.bye.decode("unicode-escape") + "\n"
