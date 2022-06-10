from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class addBookForm(forms.Form):
    name = forms.CharField(label='book name', max_length=100)