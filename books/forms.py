from django.forms import ModelForm
from .models import Book, Raiting
from django import forms


class BookForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
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


class RateForm(forms.ModelForm):
    CHOICES = (
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5)
    )
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    rate = forms.ChoiceField(choices=CHOICES, widget=forms.Select(
        attrs={'class': 'form-select'}))

    class Meta:
        model = Raiting
        fields = ('rate', 'comment')
