from django.forms import ModelForm
from .models import Book
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(ModelForm):
	title = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
	author = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
	publish_year = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
	publisher = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
	descritpion = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))


	class Meta:
		model = Book
		fields = '__all__'

        
class NewUserForm(UserCreationForm):
	email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'}))
	username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
	
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	
	def __init__(self, *args, **kwargs):
		super(NewUserForm, self).__init__( *args, **kwargs)
		
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user