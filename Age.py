# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:51:50 2018

@author: PrasadK
"""

from datetime import datetime, date

print("Enter DOB (dd mm yyyy)")
date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)

print(age)



from datetime import datetime, date
print("Enter DOB")
DOB = datetime.strptime(input())

def find_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))