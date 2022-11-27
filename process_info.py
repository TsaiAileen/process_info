#!/usr/bin/python3
import sys

##print(len(sys.argv))
#print(sys.argv[1])
option = ""
if len(sys.argv) >= 2: 
    option = sys.argv[1]
filename = ""
if len(sys.argv) >= 3:
    filename = sys.argv[2]

if option != "-a" and option != "-m" and option != "-t" and option != "-s" and option != "-v":
    print("Wrong option")
    sys.exit(1)

if filename == "":
    print("Missing the filename argument")
    sys.exit(2)

if option == "-a":
    dict = {}
    lf = open(filename,'r')
    rows = 0
    for line in lf.readlines():
        #print(line)
        rows += 1
        word = line.split(' ')
        #print(word)
        if len(word) >= 4 :
            program_name = word[3]
            dict[program_name] = line 
    lf.close()
    
    if rows == 0 :
        print("No processes found")
    else :
        sortedDict = sorted(dict.items())

        if len(sortedDict) > 0 :
            for key,value in sortedDict :
                print(value)

elif option == "-m":
    memorySize = 0 
    memorySize_total = 0
    lf = open(filename,'r')
    rows = 0
    for line in lf.readlines():
        #print(line)
        rows += 1
        word = line.split(' ') #['4','0','6','events']
        #print(word)
        if len(word) >= 2 :
            memorySize = word[1]
            memorySize_total = memorySize_total + int(memorySize)
    lf.close()

    if rows == 0 :
        print("No processes found")
    else :
        print("Total memory size: ", str(memorySize_total) + " KB")

elif option == "-t":
    cpuTime = 0 
    cpuTime_total = 0
    lf = open(filename,'r')
    rows = 0
    for line in lf.readlines():
        #print(line)
        rows += 1
        word = line.split(' ') #['4','0','6','events']
        #print(word)
        if len(word) >= 3 :
            cpuTime = word[2]
            cpuTime_total = cpuTime_total + int(cpuTime)
    lf.close()

    if rows == 0 :
        print("No processes found")
    else :
        print("Total CPU time: ", str(cpuTime_total) + " seconds")

elif option == "-s":
    memorySize = 0 
    threshold = 0

    if len(sys.argv) >= 3: 
        threshold = sys.argv[2]   
    if len(sys.argv) >= 4:
        filename = sys.argv[3] 

    lf = open(filename,'r')
    rows = 0
    rows_threshold = 0
    for line in lf.readlines():
        #print(line)
        rows += 1
        word = line.split(' ') #['4','0','6','events']
        #print(word)
        if len(word) >= 2 :
            memorySize = word[1]
            # print("memorySize: " , memorySize)
            # print("threshold: ", threshold)
            if int(memorySize) >= int(threshold) :
                rows_threshold += 1
                print(line)

    lf.close()

    if rows == 0 :
        print("No processes found with the specified memory size")
    elif rows_threshold == 0 :
        print("No processes found with the specified memory size")

elif option == "-v":
    print("Name: Aileen")
    print("Surname: Tsai")
    print("Student ID: 1234567")
    print("Date of completion: 23 OCT 2022")