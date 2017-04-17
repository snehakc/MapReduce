#!/usr/bin/ python
import sys
import csv

vals = []

for line in sys.stdin:

                l = list(csv.reader([line])) [0]
                if  not l[5].isdigit():
                                pass
                else:
                                
                                val={
                                "num" : l[0],
                                "id": l[1] ,
                                "time" : l[2],
                                "dos": l[3],
                                "hatype" : l[4],
                                "age" : int(l[5].strip()) if l[5].isdigit() else 0,
                                "airq" : l[6],
                                "medication" : l[7],
                                "headache" : l[8],
                                "sex" : l[9].strip()
                                }
                                print '{0}\t{1}'.format(l[9],l[7])
