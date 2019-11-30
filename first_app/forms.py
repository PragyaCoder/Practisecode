from django import forms
from first_app.models import Userr
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with Z")

# Form to print model fields on HTML page and then take user input and save it to Model
class NewUserForm(forms.ModelForm):
    class Meta():
        model = Userr
        fields = '__all__'

# Custom defined form and taking user inputs, validating them (botcapture too) and printing them on console
class FormName(forms.Form):
    name = forms.CharField(max_length=264)
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcapture = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(16)])

    def clean_botcapture(self):
        botcapture = self.cleaned_data['botcapture']

        if len(botcapture) >0:
            raise forms.ValidationError("GOTCHA BOT!!")

        return botcapture
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure emails match!!")

# Form defined to display authorization feature. Created corresponding to UserProfileInfo model.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio', 'picture')