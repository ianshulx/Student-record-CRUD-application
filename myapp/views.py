from datetime import date, datetime
from pickle import FALSE
import re
from turtle import home
from urllib import response
from django import http
from django.forms import DateField
from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import Student_data_form
from .models import Student_data
from django.views import View
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import csv
from .models import Student_data
import datetime
import winsound
from datetime import datetime, timedelta




class HomeView(View):
 def get(self, request):
  form = Student_data_form()
  candidates = Student_data.objects.all()
  return render(request, 'myapp/add_data.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = Student_data_form(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return redirect('list')

   
@login_required
def application_form(request, pk):
  candidate = Student_data.objects.get(pk=pk)
  
  return render(request, 'myapp/candidate.html', {'candidate':candidate})


@login_required
def export(request):
    response = HttpResponse(content_type='text/scv')
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Middle Name', 'Fathers Name', 'Date Of Birth', 'Category',  'City', 'Mobile','Course','Department','Lateral Entry','Photo', 'Adhaar','Adhaar No.', 'PAN','PAN No.' ,'10th Marksheet', '12th Marksheet', 'Diploma Marksheet', 'Degree', 'Income Cerificate', 'Caste Certificate', 'Character Certificate' ])
    

    for student in Student_data.objects.all().values_list('first_name', 'last_name', 'middle_name', 'fathers_name', 'dob', 'category', 'city', 'mobile', 'course','department','lateral' , 'photo', 'Adhaar','Adhaar_no', 'pan','pan_no', 'mark10','mark12', 'mark_diploma', 'mark_graduation','income', 'caste', 'charactor_certificate' ):
        writer.writerow(student)

    response['Content-Disposition']= ' attachment; filename="studentsdata.csv" '


    return response




@login_required
def stu_list(request):
   student=Student_data.objects.all()
   return render(request, 'myapp/list.html', {'student': student})


@login_required
def fee(request):
    student=Student_data.objects.all()

    return render(request, 'myapp/fee.html', {'student': student})
@login_required
def export_fee(request):
    response = HttpResponse(content_type='text/scv')
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Middle Name', 'Fathers Name', 'Date Of Birth', 'Category',  'Mobile','Course','Department','Lateral Entry','Installment 1 date', 'Installment 1 ammount', 'Installment 2 date', 'Installment 2 ammount', 'Installment 3 date', 'Installment  ammount', 'Installment 4 date', 'Installment 4 ammount', 'Installment 5 date', 'Installment 5 ammount', ])
    

    for student in Student_data.objects.all().values_list('first_name', 'last_name', 'middle_name', 'fathers_name', 'dob', 'category',  'mobile', 'course','department','lateral' ,'installment_1_date','installment_1_ammount','installment_2_date','installment_2_ammount','installment_3_date','installment_3_ammount','installment_4_date','installment_4_ammount','installment_5_date','installment_5_ammount'  ):
        writer.writerow(student)

    response['Content-Disposition']= ' attachment; filename="installments.csv" '


    return response
@login_required
def notice(request):   
    data1=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_1_date','installment_1_ammount' )
    data2=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_2_date','installment_2_ammount' )
    data3=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_3_date','installment_3_ammount' )
    data4=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_4_date','installment_4_ammount' )
    data5=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_5_date','installment_5_ammount' )
    
    list1 =[]
    

    aajkadin=date.today()
    print('aajkadin:::', aajkadin)
    print(data1)

    w2 = (date.today() + timedelta(days=1))
    w3 = (date.today() + timedelta(days=2))
    w4 = (date.today() + timedelta(days=3))
    w5 = (date.today() + timedelta(days=4))
    w6 = (date.today() + timedelta(days=5))
    w7 = (date.today() + timedelta(days=6))

    print('timedaketi ::', w2, w3, w4, w5, w6, w7)

    
    for i in data1:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
        
                print("working")
                list1.append(i)
                
    for i in data2:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
        
                print("working")
                list1.append(i)

    for i in data3:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
        
                print("working")
                list1.append(i)


    for i in data4:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
        
                print("working")
                list1.append(i)


    for i in data5:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
        
                print("working")
                list1.append(i)

               
    return render(request, 'myapp/fee_notice.html', {'list1': list1})

@login_required
def noticefile(request):   
    
    # date1=Student_data.objects.all().values_list('installment_1_date')
    data1=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_1_date','installment_1_ammount' )
    data2=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_2_date' )
    data3=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_3_date' )
    data4=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_4_date' )
    data5=Student_data.objects.all().values_list( 'first_name', 'last_name', 'middle_name', 'fathers_name', 'category',  'mobile', 'course','department','installment_5_date' )
    



    aajkadin=date.today()
    print('aajkadin:::', aajkadin)
    print(data1)

    w2 = (date.today() + timedelta(days=1))
    w3 = (date.today() + timedelta(days=2))
    w4 = (date.today() + timedelta(days=3))
    w5 = (date.today() + timedelta(days=4))
    w6 = (date.today() + timedelta(days=5))
    w7 = (date.today() + timedelta(days=6))

    response = HttpResponse(content_type='text/scv')
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Middle Name', 'Fathers Name', 'Category',  'Mobile','Course','Department','Installment 1 date', 'Installment 1 ammount' ])
    
    for i in data1:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
                print("working")
                
                writer.writerow(i)
    for i in data2:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
                print("working")
                
                writer.writerow(i)

    for i in data3:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
                print("working")
                
                writer.writerow(i)


    for i in data4:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
                print("working")
                
                writer.writerow(i)


    for i in data5:
        print(i)
        for j in i:
            print(j)
            if j==aajkadin or j==w2 or j==w3 or j==w4 or j==w5 or j==w6 or j==w7:
                print("working")
                
                writer.writerow(i)

    response['Content-Disposition']= ' attachment; filename="pendinginstallments.csv" '
    return response
                




@login_required
def delete_data(request, id):
   if request.method == 'POST':
      pi = Student_data.objects.get(pk=id)
      pi.delete()
      return redirect(stu_list)

@login_required
def update_data(request, id):
   if request.method == 'POST':
      pi=Student_data.objects.get(pk=id)
      form = Student_data_form(request.POST, request.FILES, instance=pi)
      if form.is_valid():
         form.save

   else:
      pi=Student_data.objects.get(pk=id)
      form = Student_data_form(instance=pi)
   return render(request, "myapp/updatedata.html", {'form': form})


@login_required
def menu(request):
    return render(request, 'myapp/home.html')



#Authentication 

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        
        
        
        
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        
        
        
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! please admins to activate your account")

        
        return redirect(signin)
        
        
    return render(request, "myapp/signup.html")





def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            
            return redirect(menu)
        else:
            messages.error(request, "Bad Credentials!! Please check username or password ")
            return redirect(signin)
    
    return render(request, "myapp/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')

   

