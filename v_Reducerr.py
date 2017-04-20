#!/usr/bin/python
import sys


medicationTotal = 0
noMedicationTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisvalue = data_mapped

# checks if the key is same as the old key and then prints the data if the key is same
    if oldKey and oldKey != thisKey:
       # print "\tSex of the person:", oldKey, "\ttaking medication:", medicationTotal, "\tNot taking Medication:", noMedicationTotal 
        oldKey = thisKey;
	#print oldKey
	#print thisKey
	

    oldKey = thisKey
    if thisKey == 'female':
	if thisvalue == 'none':
   	    noMedicationTotal += 1
	
	else:
	    medicationTotal += 1
	   # print thisKey
	    #print thisvalue
print "\t Number of females taking medication:", medicationTotal, "\t Number of females Not taking Medication:", noMedicationTotal
