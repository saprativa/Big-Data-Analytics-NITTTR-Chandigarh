# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:24:47 2020

@author: sb
"""


import pandas as pd

df = pd.read_excel('student_result.xlsx')

print("%10s \t %s \t %s" % ("NAME", "EXTERNAL MARKS", "INTERNAL MARKS"))

for i, row in df.iterrows():
    if(row['External_marks'] > row['Internal_marks']):
        print("%10s \t %s \t\t\t %s" % (row['Name'], row['External_marks'], row['Internal_marks']))