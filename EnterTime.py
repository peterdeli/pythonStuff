#!/bin/env python
'''
Created on Apr 9, 2017

@author: peter d
'''

# Key "Activity" ->      Hash { WBS % } 


import inspect
import sys
global WORK_CODE_FILE
def banner(me, parent):
    print """--------------------------
%s : %s""" % ( parent, me )

def whoami():
    return inspect.stack()[1][3]
def whosdaddy():
    return inspect.stack()[2][3]
def loadConfig(WORK_CODE_FILE):
    banner( whoami(), whosdaddy())
    
    WorkCodeDict = {}
    choice = raw_input( "Enter the path to the datafile\n( Press return for Default:  " + WORK_CODE_FILE + "): " )
    choice=choice.strip()
    if choice != '':
        WORK_CODE_FILE = choice
        
    mode='r'
    try:
        with open ( WORK_CODE_FILE, mode ) as workCodeFile:
            for line in workCodeFile.readlines():
                    [descr,code,pct] = line.strip().split(':')
                    # add successive descr items to dict
                    if descr in WorkCodeDict.keys():
                        codePctHash = WorkCodeDict[descr]
                        codePctHash[code] = pct
                    else:
                        WorkCodeDict[descr] = {code:pct}
    except IOError:
        print "Error opening {} for reading: {}".format( WORK_CODE_FILE, "IO error")

    return WorkCodeDict


def init():
    global WORK_CODE_FILE
    banner( whoami(), whosdaddy())
    WORK_CODE_FILE="workCodeFile.dat"
    
def mainMenu(WorkCodeDict):
    banner( whoami(), whosdaddy())
 
    menu_idx = 1
    list_idx = 0
    descr_list = WorkCodeDict.keys()
    
    for descr in descr_list:
        menuItem = "{}) {}".format(menu_idx,descr)
        print menuItem
        menu_idx += 1
    return ( menu_idx - 1 )
        
def selectWorkItem(menu_idx):
    banner( whoami(), whosdaddy())
    while True:
        print "Enter a selection number: "
        inputPrompt = "Choice: (1 - {max_choice}), 'q' to quit: ".format(max_choice=menu_idx)
        choice = raw_input(inputPrompt)
        choice=choice.strip()
        if choice == 'q':
            sys.exit(0)
        try:
            list_idx = int(choice) - 1
            if int(choice) > menu_idx  or int(choice) < 1:
                print "Selection {value} is not a valid choice".format(value=choice)
                continue
            else:
                break
        except ValueError as e:
            print("\"{choice}\" is not a valid input".format(choice=choice))
            continue
    return list_idx

def enterHoursForChoice(workDescr):
    banner( whoami(), whosdaddy())
    while True:
        inputPrompt = "Enter the number of hours for " + workDescr
        hours = raw_input( inputPrompt + " ('q' to quit): " )
        hours=hours.strip()
        try:
            testNum = float(hours) + 0.0
        except ValueError as e:
            print("\"{choice}\" is not a valid input".format(choice=hours))
            continue
        else:
            return float(hours)
    

def displayData(WorkCodeDict, workDescr, hours):
    banner( whoami(), whosdaddy())
    print "For " + workDescr + ", SAP code and hours: "
    for code in WorkCodeDict[workDescr].keys():
        pct = WorkCodeDict[workDescr][code]
        print "Code: {:>25}, {:>5}%, Hours: {:>5.2f}".format(code,float(pct),float(float(hours) * (float(pct)/100)))
    print "{:>48}{:>5.2f}".format("Total hours: ", float(hours))
def main():
    if __name__ == '__main__':
        pass
    #WORK_CODE_FILE="C:\workCodeFile.dat"
    banner( whoami(), whosdaddy())
    global WORK_CODE_FILE
    
    init()
    
    WorkCodeDict=loadConfig(WORK_CODE_FILE)
    descr_list = WorkCodeDict.keys()
    while True:
        menu_idx = mainMenu(WorkCodeDict)
        list_idx=selectWorkItem(menu_idx)
        hours=enterHoursForChoice(descr_list[list_idx])
        displayData(WorkCodeDict, descr_list[list_idx], hours)
        
        inputPrompt="Press return for next item, 'q' to quit: "
        choice=raw_input(inputPrompt)
        choice=choice.strip()
        if choice =='q':
            sys.exit(0)
        
        
    
main()
