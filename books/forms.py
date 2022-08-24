from django.forms import ModelForm
from .models import Book
from django import forms


class BookForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    publish_year = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    publisher = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control '}))
    descritpion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control '}))

    class Meta:
        model = Book
        fields = ('title', 'author', 'publish_year',
                  'publisher', 'descritpion', 'cover')
