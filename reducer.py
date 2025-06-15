#!/usr/bin/env python  
import sys  
gender_age = {}  
for line in sys.stdin:  
    gender, age = line.strip().split('\t')  
    gender_age.setdefault(gender, []).append(int(age))  

for gender in gender_age:  
    ave_age = sum(gender_age[gender]) * 1.0 / len(gender_age[gender])  
    print '%s\t%s' % (gender, ave_age)
