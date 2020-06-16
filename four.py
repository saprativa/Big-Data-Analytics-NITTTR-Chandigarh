# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:35:47 2020

@author: sb
"""


import pandas as pd

data = {'Name':['Saprativa', 'Sanjay', 'Rajesh', 'Srinath'],
        'Designation':['Lecturer', 'Lecturer', 'Lecturer', 'Lecturer'],
        'Email-id':['saprativa@gmail.com', 'sanjay@gmail.com', 'rajesh@gmail.com', 'srinath@gmail.com'],
        'Contact Number':[9876543211, 9876543212, 9876543213, 9876543214],
        'Salary':[50000, 50000, 50000, 50000]}

df = pd.DataFrame(data)

print(df)