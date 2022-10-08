from cProfile import label
from dataclasses import field, fields
from datetime import date
from logging import PlaceHolder
from django import forms
from .models import LATERAL, Student_data
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Fieldset, ButtonHolder, Div
from crispy_forms.bootstrap import InlineRadios, InlineField, InlineCheckboxes, PrependedText, FieldWithButtons


# GENDER_CHOICES = [
#  ('Male', 'Male'),
#  ('Female', 'Female')
# ]

# CATEGORY = [
#  ('SC', 'SC'),
#  ('ST', 'ST'),
#  ('OBC', 'OBC'),
#  ('GENERAL', 'GENERAL'),
#  ('OTHERS', 'OTHERS'),

# ]

YES_NO = (
 ('NO','NO'),
 ('YES','YES')
 
)

LATERAL = (
 ('REGULAR','REGUALR'),
 ('LATERAL ENTRY','LATERAL ENTRY')
)

INSTALLMENT=(
 ('1','1'),
 ('2','2'),
 ('3','3'),
 ('4','4'),
 ('5','5')
 
)

class Student_data_form(forms.ModelForm):
 
 lateral = forms.ChoiceField(choices=LATERAL, widget=forms.RadioSelect, label='Admission type')
#  category = forms.ChoiceField(label='Category', choices=CATEGORY, widget=forms.RadioSelect)
#  dob = forms.ChoiceField(widget=forms.DateField, label='date of birth')
 dob = forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'}
    ),
    label='date of birth'
) 

 installment_1_date= forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'}
    ),
    label='Installment 1 date',
    required=False
)

 installment_2_date= forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'}
    ),
    label='Installment 1 date',
    required=False
)

 installment_3_date= forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'}
    ),
    label='Installment 1 date',
    required=False
)

 installment_4_date= forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'}
    ),
    label='Installment 1 date',
    required=False
)

 installment_5_date= forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'}
    ),
    label='Installment 1 date',
    required=False
)







 class Meta:
  model = Student_data
  fields = ['refrenced_by', 'first_name','middle_name', 'last_name', 'fathers_name', 'fathers_occupation', 'mothers_name','mothers_occupation', 'dob', 'gender', 'category','address', 'city', 'pin','mobile', 'mobile2', 'email',  'course', 'department', 'session_start', 'session_end', 'lateral',   'mark10', 'mark10_obtained' , 'mark10_total', 'mark12',  'mark12_obtained' , 'mark12_total', 'mark_graduation', 'mark_graduation_obtained' , 'mark_graduation_total' , 'photo', 'sign', 'Adhaar', 'Adhaar_no' ,'pan', 'pan_no', 'caste', 'income', 'scholar_credit', 'charactor_certificate', 'state', 'mark_diploma', 'mark_diploma_obtain', 'mark_diploma_total', 'domicile', 'total_income','number_of_installment', 'installment_1_ammount','installment_1_date', 'installment_2_ammount','installment_2_date', 'installment_3_ammount','installment_3_date','installment_4_ammount','installment_4_date','installment_5_ammount','installment_5_date']
  labels = {'first_name':'First Name', 'middle_name':'Middle Name', 'last_name':'Last Name' ,'fathers_name': 'Fathers Name' ,'fathers_occupation': 'Fathers occupation' , 'mothers_occupation': 'Mothers occupation' , 'dob': 'Date of Birth', 'pin':'Pin Code', 'mobile':'Mobile No.', 'mobile2':'Fathers mobile no.', 'email':'Email ID', 'lateral':'Admission type', 'photo':'Students Image', 'Adhaar':'Adhaar Card', 'pan':'Pan Card', 'caste':'Caste Certificate', 'income':'Income Certificate', 'charactor_certificate': 'Character Certificate', 'state':'State','scholar_credit':'Scholarship Credit', 'mark10': '10th Marksheet', 'session_start':'Session','session_end':'','mark_diploma':'Diploma Marsksheet', 'mark_diploma_obtain':'(for Lateral only) Marks obtained in diploma', 'mark_diploma_total':'Total marks in diploma',  'mark12': '12th Marksheet', 'mark10_obtained':'Obtained marks in 10th', 'mark10_total':'Total marks in 10th','mark12_obtained':'Obtained marks in 12th' , 'mark12_total':'Total marks in 12th', 'mark_graduation_obtained':'( MBA only ) Obtained marks in degree' , 'mark_graduation_total':'Total marks in degree', 'mark_graduation':'Graduation degree', 'domicile':'Domicile Certificate', 'total_income':'Annual family income'}
  
 


 def __init__(self, *args, **kwargs):
  super().__init__(*args, **kwargs)
  self.helper = FormHelper()
  self.helper.form_method = 'post'
  self.helper.add_input(Submit('submit', 'Submit'))
  self.helper.layout = Layout(

      Div(
        Div(
            Div('first_name', css_class="col-sm-4"),
            Div('last_name', css_class="col-sm-4"),
            Div('middle_name', css_class="col-sm-4"),
            

            css_class='row',
        ),

        Div(
            Div('fathers_name', css_class="col-sm-7"),
            Div('fathers_occupation', css_class="col-sm-5"),
            
            

            css_class='row',
        ),

       Div(
            Div('mothers_name', css_class="col-sm-7"),
            Div('mothers_occupation', css_class="col-sm-5"),
            
            

            css_class='row',
        ),

                Div(
                  
            Div('dob', css_class="col-sm-4"),
            Div('gender', css_class="col-sm-4"),
            Div('category', css_class="col-sm-4"),
            

            css_class='row',
        ),
 Div('address', css_class='col-sm-12'),


       Div(
            Div('city', css_class="col-sm-5"),
            Div('state', css_class="col-sm-5"),
            Div('pin', css_class="col-sm-2"),
            
            

            css_class='row',
        ),

     Div(
            Div('mobile', css_class="col-sm-4"),
            Div('mobile2', css_class="col-sm-4"),
            Div('email', css_class="col-sm-4",  placeholder="e-mail"),
            
            

            css_class='row',
        ),




      Div(
            Div('lateral', css_class="col-sm-2"),
            Div('session_start', '<b>----</b>', 'session_end', css_class="col-sm-2"),
            Div('course', css_class="col-sm-2"),
            Div('department', css_class="col-sm-3"),

            
            css_class='row',
        ),





        Div(
            Div('mark10_obtained', css_class="col-sm-4"),
            Div('mark10_total', css_class="col-sm-4"),
            FieldWithButtons('mark10', css_class="col-sm-4"),
            
            

            css_class='row',
        ),


     Div(
            Div('mark12_obtained', css_class="col-sm-4"),
            Div('mark12_total', css_class="col-sm-4"),
            FieldWithButtons('mark12', css_class="col-sm-4"),

            
            

            css_class='row',
        ),

      Div(
            Div('mark_diploma_obtain', css_class="col-sm-4"),
            Div('mark_diploma_total', css_class="col-sm-4"),
            FieldWithButtons('mark_diploma', css_class="col-sm-4"),
            
            
            

            css_class='row',
        ),


         Div(
            Div('mark_graduation_obtained', css_class="col-sm-4"),
            Div('mark_graduation_total', css_class="col-sm-4"),
            FieldWithButtons('mark_graduation', css_class="col-sm-4"),
           
            
            
            

            css_class='row',
        ),

          Div(
            
            FieldWithButtons('photo', css_class="col-sm-6"),
            FieldWithButtons('sign', css_class="col-sm-6"),
            
            
            
            

            css_class='row',
        ),

        Div(
            
            FieldWithButtons('Adhaar_no', css_class="col-sm-5"),
            FieldWithButtons('Adhaar', css_class="col-sm-7"),
            

            

            css_class='row',
        ),

        
        Div(
            
            FieldWithButtons('pan_no', css_class="col-sm-5"),
            FieldWithButtons('pan', css_class="col-sm-7"),
            

            

            css_class='row',
        ),



         Div(
            
            FieldWithButtons('caste', css_class="col-sm-4"),
            FieldWithButtons('domicile', css_class="col-sm-4"),
            FieldWithButtons('charactor_certificate', css_class="col-sm-4"),

            

            css_class='row',
        ),
                        Div(
            
            FieldWithButtons('total_income', css_class="col-sm-6"),
            FieldWithButtons('income', css_class="col-sm-6"),




            css_class='row',
        ),

                                Div(
            
            FieldWithButtons('scholar_credit', css_class="col-sm-3"),
            FieldWithButtons('number_of_installment', css_class="col-sm-3"),





            css_class='row',
        ),

                                        Div(
            
            FieldWithButtons('installment_1_ammount', css_class="col-sm-3"),
            FieldWithButtons('installment_1_date', css_class="col-sm-3"),





            css_class='row',
        ),

                                               Div(
            
            FieldWithButtons('installment_2_ammount', css_class="col-sm-3"),
            FieldWithButtons('installment_2_date', css_class="col-sm-3"),





            css_class='row',
        ),

                                                       Div(
            
            FieldWithButtons('installment_3_ammount', css_class="col-sm-3"),
            FieldWithButtons('installment_3_date', css_class="col-sm-3"),





            css_class='row',
        ),

                                                       Div(
            
            FieldWithButtons('installment_4_ammount', css_class="col-sm-3"),
            FieldWithButtons('installment_4_date', css_class="col-sm-3"),





            css_class='row',
        ),

                                                       Div(
            
            FieldWithButtons('installment_5_ammount', css_class="col-sm-3"),
            FieldWithButtons('installment_5_date', css_class="col-sm-3"),





            css_class='row',
        ),

                                                               Div(
            
            FieldWithButtons('refrenced_by', css_class="col-sm-7"),
            





            css_class='row',
        ),

        css_class='form-control'

      )

  )



  





  