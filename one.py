# -*- coding: utf-8 -*-
marks = [[45,46,30],
         [28,50,12],
         [50,36,48],
         [14,28,43],
         [37,46,24]]

print("Student \tSubject 1\tSubject 2\tSubject 3\tTotal\tPercentage")

i = 0

for student in marks:
    i = i + 1
    total = 0
    print("Student%d\t" % i, end = '')
    for mark in student:
        print("%.2f\t" % (mark), end = '\t')
        total = total + mark 
        
    percentage = total*100/150
    print("%.2f\t%.2f %%" % (total, percentage))
    
