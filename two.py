# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_excel('student_result.xlsx')

print("%10s \t %s" % ("NAME", "SESSIONAL MARKS"))

for i, row in df.iterrows():
    if(row['Sessional_marks'] > 15):
        print("%10s \t %s" % (row['Name'], row['Sessional_marks']))