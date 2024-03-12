import os
from django.conf import settings
from django.core.files import File
from django.shortcuts import render
from .models import UserProfile
from .forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
        return render(request,'basic_app/index.html')

def users(request):
    users_list = UserProfile.objects.order_by("user")
    return render(request, 'basic_app/users.html', {"users_list": users_list})

@login_required
def special(request):
    return HttpResponse('You are logged in.')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_pic_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_pic_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) 
            user.save()

            profile = profile_pic_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            else:
                default_image_path = os.path.join(settings.MEDIA_ROOT, 'profile_pics/default.jpg')
                with open(default_image_path, 'rb') as f:
                    profile.profile_pic.save('default.jpg', File(f), save=False)

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_pic_form.errors)
    else:
        user_form = UserForm()
        profile_pic_form = UserProfileForm()

    return render(request,'basic_app/registration.html',{'user_form':user_form,
                                                        'profile_pic_form':profile_pic_form,
                                                        'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
        else:
            print('Someome tried to login and failed!')
            print(f'Username: {username}, password: {password}')
            return HttpResponse('Invalid login details')
    else:
        return render(request,'basic_app/login.html')
