from __future__ import print_function
import os
import time

def anyEnds(fileList, ext):
    for f in fileList:
        if f.endswith(ext):
            return True
    return False

def extFiles(fileList, ext):
    if ext == '':
        return fileList
    temp = []
    for f in fileList:
        if f.endswith(ext):
            temp.append(f)
    return temp

def main():
    global input
    print("Welcome to DeepestFiles! What kind of files are you searching for?")

    # Allows compatibility with Python 2.x and 3.x
    try:
       input = raw_input
    except NameError:
       pass
    
    ext = input("(Leave blank for all types. Otherwise, type the filename extensions with a single space separating each.): ")
    if (ext == ''):
        print("Looking for all files.")
    else:
        print("Looking for files with the following extension(s):", ext)
        ext = tuple(ext.split())

    numresults = input("What is the maximum number of results you would like returned? Enter a number 1-20: ")
    while True: # Only continues if user inputs an integer between 1 and 20
        try:
            numresults = int(numresults)
        except ValueError:
            numresults = input("That was not a number. Please enter a number 1-20: ")
        else:
            if numresults in range(1,21):
                print("Searching...")
                break
            else:
                numresults = input("That was not between 1 and 20. Please enter a number 1-20: ")

    # Starts the clock
    t0 = time.clock()

    # NEXT: Allow user to type what directory to search in
    #rootDir = '.'
    rootDir = "C:\\"
    #rootDir = ".\example"

    deepest = [''] * numresults
    files = [''] * numresults
    for dirPath, subdirList, fileList in os.walk(rootDir, topdown=False):
        if len(fileList) != 0:
            if ext == '' or anyEnds(fileList, ext):
                for i, d in enumerate(deepest):
                    if (dirPath.count("\\") > d.count("\\")):
                        deepest.insert(deepest.index(d), dirPath)
                        files.insert(i, extFiles(fileList, ext))
                        # Keeps only the top numresults examples as specified by the user
                        if len(deepest) > numresults:
                            deepest.pop(numresults)
                            files.pop(numresults)
                        break

    # If number of found results is not as much as user-inputted numresults, empty data is removed
    deepest = list(filter(None, deepest))
    for i, result in enumerate(deepest):
        print("================")
        print(i+1, ')', result)
        print(result.count("\\"), "subfolders from root")
        print("Files in this folder:")
        for f in files[i]:
            print(f)

    print(time.clock() - t0, "seconds elapsed for snooping")

if __name__ == "__main__":
    main()
