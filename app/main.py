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
    selection = ""
    while True:
        masthead()
        print "MAIN MENU"
        print "-" * 40
        projectsList(True)
        # Selection menu
        print "[N] New project"
        print "[A] Archive"
        print "[E] Exit\r"
        selection = raw_input("\n>>> Select an option: ").lower()
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "n":
                newProject()
            if selection.lower() == "a":
                archiveMenu()
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
        masthead()
        print "PROJECT MENU: " + dictionary.projects[project]["name"]
        print "-" * 40
        tasksList(project, True)
        # Selection menu
        print "[N] New task"
        print "[A] Archive"
        print "[B] Back\r"
        selection = raw_input("\n>>> Select an option: ").lower()
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "n":
                newTask(project)
            if selection.lower() == "a":
                archiveProject(project)
            if selection.lower() == "b":
                break
        else:
            if int(selection) <= len(dictionary.tasks) and int(selection) > 0:
                startTask(project, selection)

# New project
def newProject():
    while True:
        masthead()
        print "CREATE NEW PROJECT"
        print "-" * 40
        projectName = raw_input("\nProject name: ")
        # Adding project to file
        project = [len(dictionary.projects)+1, projectName, 0, True, {}]
        dictionary.projects[str(project[0])] = {"name": project[1], "time": str(project[2]), "active": str(project[3]), "tasks": project[4]}
        # Dumping dictionary into JSON file
        with open("data/projects.json", "w") as f:
            json.dump(dictionary.projects, f)
        # Showing that the project has been created
        print "Creating project",
        dotdotdot(5)
        break

# Start task
def startTask(project, task):
    while True:
        masthead()
        print "WORKING ON TASK:" + dictionary.tasks[task]["name"]
        print "Project: " + dictionary.projects[project]["name"]
        print "-" * 40
        # Selection menu
        print "[S] Start timer"
        print "[M] Manual record"
        print "[B] Back\r"
        selection = raw_input("\n>>> Select an option: ").lower()
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "s":
                break
            if selection.lower() == "m":
                manualRecord(project, task)
            if selection.lower() == "b":
                break

# Introduce manual record
def manualRecord(project, task):
    masthead()
    print "ADD MANUAL RECORD TO: " + dictionary.tasks[task]["name"]
    print "Project:" + dictionary.projects[project]["name"]
    print "-" * 40
    # Getting time value
    while True:
        time = raw_input("\nTime to add (in minutes): ")
        try:
            int(time)
        except ValueError:
            True
        else:
            if int(time) <= 0:
                True
            else:
                break
    # Adding task to file
    time = int(time) * 60
    oldTime = int(dictionary.tasks[task]["time"])
    newTime = oldTime + time
    dictionary.tasks[task]["time"] = str(newTime)
    # Updating project
    oldTime = int(dictionary.projects[project]["time"])
    newTime = oldTime + time
    dictionary.projects[project]["time"] = str(newTime)
    # Dumping dictionary into JSON file
    with open("data/projects.json", "w") as f:
        json.dump(dictionary.projects, f)
    # Showing that the task has been created
    print "Updating task",
    dotdotdot(5)
    projectMenu(project)

# New task menu
def newTask(project):
    while True:
        masthead()
        print "CREATE NEW TASK FOR: " + dictionary.projects[project]["name"]
        print "-" * 40
        taskName = raw_input("\nTask name: ")
        # Adding task to file
        task = [len(dictionary.tasks)+1, taskName, 0]
        dictionary.tasks[str(task[0])] = {"name": task[1], "time": str(task[2])}
        dictionary.projects[str(project)]["tasks"] = dictionary.tasks
        # Dumping dictionary into JSON file
        with open("data/projects.json", "w") as f:
            json.dump(dictionary.projects, f)
        # Showing that the task has been created
        print "Creating task",
        dotdotdot(5)
        break

# Archive menu
def archiveMenu():
    while True:
        masthead()
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
                    unarchiveProject(selection)

# Archive project
def archiveProject(project):
    while True:
        masthead()
        print "ARCHIVE PROJECT?: " + dictionary.projects[project]["name"]
        print "-" * 40
        # Selection menu
        print "[Y] Yes"
        print "[B] Back\r"
        selection = raw_input("\n>>> Select an option: ")
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "y":
                dictionary.projects[project]["active"] = "False"
                # Dumping dictionary into JSON file
                with open("data/projects.json", "w") as f:
                    json.dump(dictionary.projects, f)
                print "Archiving project",
                dotdotdot(5)
                mainMenu()
            if selection.lower() == "b":
                break

# Unarchive project
def unarchiveProject(project):
    while True:
        masthead()
        print "ARCHIVED PROJECT: " + dictionary.projects[project]["name"]
        print "-" * 40
        # Show stats
        tasksList(project, False)
        # Selection menu
        print "[U] Unarchive"
        print "[B] Back\r"
        selection = raw_input("\n>>> Select an option: ")
        try:
            int(selection)
        except ValueError:
            if selection.lower() == "u":
                dictionary.projects[project]["active"] = "True"
                # Dumping dictionary into JSON file
                with open("data/projects.json", "w") as f:
                    json.dump(dictionary.projects, f)
                print "Unarchiving project",
                dotdotdot(5)
                mainMenu()
            if selection.lower() == "b":
                break

# Closes session
def closeSession():
    print "\nClosing session",
    dotdotdot(3)
    print " Done."
    print "See you later! " + emoji.bye.decode("unicode-escape") + "\n"
