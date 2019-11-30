from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Userr
from first_app import forms
from first_app.forms import NewUserForm, UserForm, UserProfileInfoForm, FormName
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello I am from views.py"}
    return render(request,'first_app/index.html',context=my_dict)

def special(request):
    return HttpResponse("You are logged out. Nice!!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:special'))

# def userdata(request):
#     user_list = User.objects.order_by('first_name')
#     user_dict = {'users':user_list}
#     return render(request,'first_app/users.html',context=user_dict)

# For printing form data in a console by creating a new form and taking user inputs to it
def form(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

    if form.is_valid():
        print("VALIDATION SUCCESS!!")
        print("Name: "+form.cleaned_data['name'])
        print("Email: "+form.cleaned_data['email'])
        print("Text entered is: "+form.cleaned_data['text'])
    
    return render(request,'first_app/forms.html',{'form':form})

# For saving form data to model by using all fields of a pre-defined model.
def users(request):
    formModel = NewUserForm()
    if request.method == "POST":
        formModel = NewUserForm(request.POST)

        if formModel.is_valid():
            formModel.save(commit=True)
            return index(request)
        else:
            print("Error Form Invalid")
    return render(request,'first_app/users.html',{'formModel':formModel})


def authoreg(request):
    print("authoreg called")
    registered = False
    if request == "POST":
        print("Inside POST")
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            print("Saved data of user")
            profile = profile_form.save(commit=False)
            profile.user = user


            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            print("Saved data of profile")

            registered = True
            print("Updated registered tag!!")
        
        else:
            print(user_form.errors, profile_form.errors)
    else:
        print("Get portion executed!!")
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/authoreg.html', {'user_form':user_form, 'profile_form':profile_form,
                                                        'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get ('username')
        password = request.POST.get ('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('first_app:index'))
            else:
                return HttpResponse("Account not active.")
        else:
            print("Invalid username: {} or password: {}".format(username, password))
            return HttpResponse("Invalid login details!!")
    else:
        return render(request, 'first_app/authologin.html',{})