#!/usr/bin python
import sys


#def get_lamda(min, max, headache):
 #   return lambda val: val["age"] >= min and \
  #                     val["age"] <= max and \
   #                    val["headache"] == headache


val = []

for line in sys.stdin:
    
    data=line.strip().split('\t') 
  
    vals = {
      "age":data[0],
     "headache":data[1] 
     }
    val.append(vals)


print "Statistical data of headache for age group of 30"
print "------------------------------------"

if data[0] >= 30:

 print vals
	
else:
    print "Other age groups"


#print val