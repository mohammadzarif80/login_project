from django.http.response import HttpResponse
from . import models
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request,'login/home.html')
       
           
    
def login(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       user=models.UserModel.objects.filter(username=username,password=password)
       if user:
          return HttpResponse('success')
       else:
           user=get_object_or_404(models.UserModel,username=username)
           if user:
             passwords=[]
             for password_object in user.passwords.all():
                 passwords.append(password_object.password)
             if passwords:
               if password in passwords:
                   return HttpResponse(user.username) 
               else:
                  return HttpResponse('کاربر  وجود ندارد')
             else:
               return HttpResponse('کاربر  وجود ندارد')
           else:
                return HttpResponse('کاربر  وجود ندارد')
    
    return render(request,'login/login.html')

        
  