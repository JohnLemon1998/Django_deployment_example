from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from re_projectapp.forms import UserProfileInfo,UserProfileInfoForm


def index(request):
        return render(request,'re_projectapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request,'re_projectapp/form_page.html',{'form':form})

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_date['name'])
            print(form.cleaned_date['email'])
            print(form.cleaned_date['text'])

    return render(request,'re_projectapp/form_page.html',{'form':form})
# Create your views here.
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form =UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print("ERROR")

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'re_projectapp/registration.html')

def relative(request):
    return render(request,'re_projectapp/relative.html')
