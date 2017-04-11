import sys


yesTotal = 0
noTotal = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisvalue = data_mapped


    if oldKey and oldKey != thisKey:
       # print "\tAge group of people:", oldKey, "\tNumber of people who have headache as symptom:", yesTotal, "\tNumber of people who do not have headache as symptom:", noTotal
	print oldKey, yesTotal, noTotal
        oldKey = thisKey;
        yesTotal = 0
	noTotal = 0

    oldKey = thisKey
    if thisvalue == 'yes':
   	    yesTotal += 1
    else:
        noTotal += 1

if oldKey != None:
    #print "\tAge group of people:", oldKey, "\tNumber of people who have headache as symptom:", yesTotal, "\tNumber of people who do not have headache as symptom:", noTotal
	print oldKey, yesTotal, noTotal
