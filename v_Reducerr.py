#!/usr/bin python
import sys


#def get_lamda(medication):
  return lambda val: val["sex"] = 'Female' and \    
                     val["medication"] == medication


val = []

for line in sys.stdin:
    
    data=line.strip().split('\t') 
  
    vals = {
      "age":data[0],
     "headache":data[1] 
     }
    val.append(vals)


print "Statistical data of females taking medications"
print "------------------------------------"

if data[sex] = 'Female':

 print vals
	
else:
    print "Other age groups"


print val