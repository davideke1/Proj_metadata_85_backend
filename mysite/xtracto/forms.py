from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import fileUpload

# Create your forms here.
from django.forms import models


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class FileForm(forms.ModelForm):
    class Meta:
        model = fileUpload
        fields = ['description', 'document']

        widgets = {
            'description' : forms.TextInput(attrs={'class': 'upload-file'}),
            'document' : forms.FileInput(attrs={'class': 'file-submit'}),
        }
