from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
class AddMovie(forms.Form):
 title =  forms.CharField(max_length=40)
 description = forms.CharField(max_length=500)
 tag = forms.CharField(max_length=40)




class AddReview(ModelForm):
    class Meta:
        model = Review
        fields =   ['title', 'stars','text']
        widgets ={
            'review': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Dejar MovieReview' }),
            
        }

class AddNewReview(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['user']
        widgets ={
            'review': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Dejar MovieReview' }),
            
        }



class AddReply(ModelForm):
    class Meta:
        model = Review
        fields =   '__all__'
        widgets ={
            'review': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Dejar MovieReview' }),
            
        }


class FindMovie(forms.Form):
 title = forms.CharField()
 

 class UserCreationForm(UserCreationForm):
    username = forms.CharField(label = 'Username', widget= forms.TextInput(attrs = {'class':'form-input'}))
    email = forms.EmailField(widget= forms.TextInput(attrs = {'class':'form-input'}))
    password1 = forms.CharField(label = 'Password', widget= forms.PasswordInput(attrs = {'class':'form-input','placeholder': '********'}))
    password2 = forms.CharField(label = 'Repeat password', widget = forms.PasswordInput(attrs = {'class':'form-input','placeholder': '********'}))
   
class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}


class UserEditForm(forms.Form):
   username = forms.CharField(widget= forms.TextInput(attrs = {'class':'form-input'}))
   email = forms.EmailField(widget= forms.TextInput(attrs = {'class':'form-input'}))
   name = forms.CharField(widget= forms.TextInput(attrs = {'class':'form-input'}))
   lastname= forms.CharField(widget= forms.TextInput(attrs = {'class':'form-input'}))
   
class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'last_name']
        help_texts = {k:'' for k in fields}
       


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = '__all__'
        exclude = ['user']