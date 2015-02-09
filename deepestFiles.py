import os
import time

NUMRESULTS = 5
t0 = time.clock()
print "Searching..."

#rootDir = '.'
rootDir = '.\example'

deepest = [''] * NUMRESULTS
files = [''] * NUMRESULTS
for dirPath, subdirList, fileList in os.walk(rootDir, topdown=False):
    if len(fileList) != 0:
        for i, d in enumerate(deepest):
            if (dirPath.count('\\') > d.count('\\')):
                deepest.insert(deepest.index(d), dirPath)
                files.insert(i, fileList)
                if len(deepest) > NUMRESULTS:
                    deepest.pop(NUMRESULTS)
                    files.pop(NUMRESULTS)
                break

for i, result in enumerate(deepest):
    print "================"
    print i, ")", result
    print result.count('\\'), "subfolders from root"
    print "Files in this folder:"
    for f in files[i]:
        print f

#print deepest
#print files

print time.clock() - t0, "seconds elapsed for snooping"
