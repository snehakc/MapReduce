import sys


medicationTotal = 0
nomedicationTotal = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisvalue = data_mapped


    if oldKey and oldKey != thisKey:
       # print "\tsex of the people:", oldKey, "\tNumber of people who take medication:", medicationTotal, "\tNumber of people who do not have headache as symptom:", noMedicationTotal
	print oldKey, medicationTotal, noamedicationTotal
        oldKey = thisKey;
        medicationTotal = 0
	noMedicationTotal = 0

    oldKey = thisKey
    if thisvalue == 'none':
   	    nomedicationTotal += 1
    else:
        medicationTotal += 1

if oldKey != None:
    #print "\tSex of the people:", oldKey, "\tNumber of people who are taking medication:", medicationTotal, "\tNumber of people who do not have headache as symptom:", noMedicationTotal
print oldKey, MedicationTotal, noMedicationTotal
