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
        print "MAIN MENU"
        print "-" * 40
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
            if int(selection) <= len(list.projects) and int(selection) > 0:
                selection = str(list.projects[int(selection)-1])
                if dictionary.projects[selection]["active"] == "True":
                    projectMenu(selection)

# Project menu
def projectMenu(project):
    while True:
        masthead(True)
        # Selection menu
        print "PROJECT MENU: " + dictionary.projects[project]["name"]
        print "-" * 40
        tasksList(project)
        # Selection menu
        print "[N] New task"
        print "[A] Archive"
        print "[S] Stats"
        print "[B] Back\r"
        selection = raw_input("\n>>> Select an option: ").lower()
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "n":
                newTaskMenu()
            if selection.lower() == "a":
                archiveProject()
            if selection.lower() == "s":
                statsProjectMenu()
            if selection.lower() == "b":
                break
        else:
            # Arreglar esto para que corresponda a las tasks
            if int(selection) <= len(list.projects) and int(selection) > 0:
                selection = str(list.projects[int(selection)-1])
                if dictionary.projects[selection]["active"] == "True":
                    taskMenu(selection)

def newTaskMenu():
    projectMenu()

def archiveProject():
    projectMenu()

def statsProjectMenu():
    projectMenu()

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
            if int(selection) <= len(list.projects) and int(selection) > 0:
                selection = str(list.projects[int(selection)-1])
                if dictionary.projects[selection]["active"] == "False":
                    unarchiveMenu(selection)

# Unarchive menu
def unarchiveMenu(project):
    while True:
        masthead(True)
        # Selection menu
        print "ARCHIVE PROJECT: " + dictionary.projects[project]["name"]
        print "-" * 40
        # Show stats
        print "Stats.............\r"
        # Selection menu
        print "[U] Unarchive"
        print "[B] Back\r"
        selection = raw_input("\n>>> Select an option: ")
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "u":
                dictionary.projects[project]["active"] = "True"
                with open("data/projects.json", "w") as f:
                    json.dump(dictionary.projects, f)
                print "Unarchiving project",
                dotdotdot(5)
                mainMenu()
            if selection.lower() == "b":
                break

# Stats menu
def statsMenu():
    while True:
        masthead(True)
        # Selection menu
        print "STATS MENU"
        print "-" * 40
        # Show stats
        print "Stats.............\r"
        # Selection menu
        print "[B] Back\r"
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
