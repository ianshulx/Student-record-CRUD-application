from calendar import calendar
from configparser import SectionProxy
import datetime
from email.policy import default
from random import choice
from re import T
from django.db import models
import os
from datetime import datetime, date

from django.forms import CharField


COURSE_CHOICE = (
 ('B.tech','B.tech'),
 ('M.tech','M.tech'),
 
 ('BCA','BCA'),
 ('BBA','BBA'),
 ('MBA','MBA'),
 ('Diploma','Diploma'),
)

DEPARTMENT_CHOICE = (
 ('MBA department','MBA department'),
 ('Computer Science department',' Computer Science department'),
 ('Electrical department','Electrical department'),
 ('Mechanical Department','Mechanical Department'),
 ('Civil Department','Civil Department'),
 ('Electronic and Engineering Department','Electronic and Engineering Department'),
 
)

GENDER_CHOICES = (
 ('MALE','MALE'),
 ('FEMALE','FEMALE'),
 ('TRANSGENDER','TRANSGENDER'),
 ('OHTER','OTHER'),

)

INCOME_CHOICES = (
 ('Below 1 lac ','Below 1 lac'),
 ('1 lac - 2 lac','1 lac - 2 lac'),
 ('2 lac - 4 lac','2 lac - 4 lac'),
 ('Above 4 lac','Above 4 lac'),
 

)



CATEGORY_CHOICES = (
 ('SC','SC'),
 ('ST','ST'),
 ('OBC','OBC'),
 ('GENERAL','GENERAL'),
 ('MINORITY','MINORITY'),

 ('OHTER','OTHER'),

)

YES_NO = (
 ('NO','NO'),
 ('YES','YES')
 
)

INSTALLMENT=(
 ('1','1'),
 ('2','2'),
 ('3','3'),
 ('4','4'),
 ('5','5')
 
)



LATERAL = (
 ('REGULAR','REGUALR'),
 ('LATERAL ENTRY','LATERAL ENTRY')
 
 
)

SESSION_CHOICE = (
 

 ('2015','2015'),
 ('2016','2016'),
 ('2017','2017'),
 ('2018','2018'),
 ('2019','2019'),
 ('2020','2020'),
 ('2021','2021'),
 ('2022','2022'),
 ('2023','2023'),
 ('2024','2024'),
 ('2025','2025'),
 ('2026','2026'),
 ('2027','2027'),
 ('2028','2028'),
 ('2029','2029'),
 ('2030','2030'),
 ('2031','2031'),
 ('2032','2032'),
 ('2033','2033'),
 ('2034','2034'),
 ('2035','2035'),
)






class Student_data(models.Model):
 first_name = models.CharField(max_length=30)
 middle_name = models.CharField(max_length=30, blank=True)
 last_name = models.CharField(max_length=20, blank=True)

 
 fathers_name = models.CharField(max_length=100)
 fathers_occupation = models.CharField(max_length=30, blank=True, null=True)
 mothers_name = models.CharField(max_length=100)
 mothers_occupation = models.CharField(max_length=30,  blank=True, null=True)


 dob = models.DateField(auto_now=False, auto_now_add=False)
 
 gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
 category = models.CharField(choices=CATEGORY_CHOICES  ,max_length=50)
 address = models.CharField(max_length=180)
 city = models.CharField(max_length=50)
 state=models.CharField( max_length=50)


 
 pin = models.PositiveIntegerField()
 course = models.CharField(choices=COURSE_CHOICE, max_length=100)
 lateral=models.CharField(choices=LATERAL, max_length=50)
 session_start=models.CharField(choices=SESSION_CHOICE ,max_length=50)
 session_end=models.CharField( choices=SESSION_CHOICE,max_length=50)


 mark10_obtained = models.PositiveIntegerField(blank=True, null=True)
 mark10_total = models.PositiveIntegerField( blank=True, null=True)

 mark12_obtained = models.PositiveIntegerField( blank=True, null=True)
 mark12_total = models.PositiveIntegerField(blank=True, null=True)

 mark_diploma_obtain = models.PositiveIntegerField( blank=True, null=True)
 mark_diploma_total = models.PositiveIntegerField(blank=True, null=True)
 
 

 mark_graduation_obtained = models.PositiveIntegerField(blank=True, null=True)
 mark_graduation_total = models.PositiveIntegerField(blank=True, null=True)

 department = models.CharField(choices=DEPARTMENT_CHOICE, max_length=50, blank=True, null=True)

 mobile = models.PositiveIntegerField()
 mobile2 = models.PositiveIntegerField(blank=True, null=True)
 email = models.EmailField(blank=True, null=True)
 


# DOCUMENTS


 photo = models.ImageField(upload_to='d/1', blank=True, null=True)
 sign = models.ImageField(upload_to='d/8', blank=True, null=True)

 Adhaar = models.FileField(upload_to='d/2', blank=True, null=True)
 Adhaar_no = models.CharField(max_length=12, blank=True, null=True)

 pan = models.FileField(upload_to='d/3', blank=True, null=True)
 pan_no = models.CharField(max_length=10,  blank=True, null=True)
 domicile = models.FileField(upload_to='d/9', blank=True, null=True)
 caste = models.FileField(upload_to='d/3', blank=True, null=True)
 
 income = models.FileField(upload_to='d/4', blank=True, null=True)
 total_income=models.CharField( choices=INCOME_CHOICES,max_length=100, blank=True, null=True)

 charactor_certificate = models.FileField(upload_to='d/5', blank=True, null=True)
 mark10 = models.FileField(upload_to='d/6', blank=True, null=True)
 mark12 = models.FileField(upload_to='d/7', blank=True, null=True)
 mark_diploma = models.FileField(upload_to='d/7', blank=True, null=True)
 mark_graduation=models.FileField(upload_to='d/8', blank=True, null=True)
 

 scholar_credit=models.CharField(choices=YES_NO, max_length=50, blank=True, default='NO')

 scholar_credit_ammount=models.PositiveIntegerField(blank=True, null=True)
 
 number_of_installment=models.CharField(choices=INSTALLMENT ,max_length=50, blank=True, null=True)


 installment_1_ammount=models.PositiveIntegerField( blank=True, null=True)
 installment_1_date=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

 installment_2_ammount=models.PositiveIntegerField( blank=True, null=True)
 installment_2_date=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

 installment_3_ammount=models.PositiveIntegerField( blank=True, null=True)
 installment_3_date=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

 installment_4_ammount=models.PositiveIntegerField( blank=True, null=True)
 installment_4_date=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

 installment_5_ammount=models.PositiveIntegerField( blank=True, null=True)
 installment_5_date=models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

 
 

 refrenced_by=models.CharField(max_length=100, blank=True)
 
 



    



 







    




