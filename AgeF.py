# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:03:26 2018

@author: prasadk
"""

from datetime import datetime, date


print("Enter DOB (dd mm yyyy)")
date_birth = datetime.strptime(input("--->"), "%Y %m %d")
date_today =  date.today

years_diff = date_today.year - date_birth.year
months_diff = date_today.month - date_birth.month
days_diff = date_today.day - date_birth.day
age_in_days = (date_today - date_birth).days

age = years_diff
age_string = str(age) + " years"




#def get_person_age(date_birth, date_today):
if years_diff == 1:
    if months_diff < 0:
        age = months_diff + 12
        age_string = str(age) + " months" 
        if age == 1:
            if days_diff < 0:
                age = age_in_days
                age_string = str(age) + " days" 
            elif days_diff < 0:
                age = age-1
                age_string = str(age) + " months"
            elif months_diff == 0:
                if days_diff < 0:
                    age = 11
                    age_string = str(age) + " months"
            else:
                age = 1
                age_string = str(age) + " years"
        else:
            age = 1
            age_string = str(age) + " years"
        
#get_person_age(DOB,Date)