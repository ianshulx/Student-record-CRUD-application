from django.contrib import admin
from .models import Student_data
from django.http import HttpResponse


def download_selected_data(modeladmin, request, queryset):
    import csv
    response = HttpResponse(content_type='text/scv')
    
    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name', 'middle_name', 'fathers_name', 'dob', 'category', 'city', 'mobile', 'course','department','lateral' , 'photo', 'Adhaar','Adhaar_no', 'pan','pan_no', 'mark10','mark12', 'mark_diploma', 'mark_graduation','income', 'caste', 'charactor_certificate'])
    for s in queryset:
        writer.writerow([s.first_name, s.last_name, s.middle_name, s.fathers_name, s.dob, s.category, s.city, s.mobile, s.course, s.department, s.lateral , s.photo, s.Adhaar, s.Adhaar_no,  s.pan, s.pan_no, s.mark10 ,s.mark12,  s.mark_diploma, s.mark_graduation , s.income, s.caste, s.charactor_certificate])

    response['Content-Disposition']= ' attachment; filename="studentsdata.csv" '


    return response



@admin.register(Student_data)
class StudentdataModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'first_name', 'last_name', 'middle_name', 'fathers_name', 'dob', 'category', 'city', 'mobile', 'course','department','lateral' , 'photo', 'Adhaar', 'pan', 'mark10','mark12', 'mark_diploma', 'mark_graduation','income', 'caste', 'charactor_certificate']
 search_fields = ['id', 'first_name', 'last_name', 'dob', 'gender', 'category', 'address', 'pin', 'course','department','lateral', 'mobile' ]
 actions = [download_selected_data]



 



