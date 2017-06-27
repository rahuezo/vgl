from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

    # def __init__(self):
    #     super(SignUpForm, self).__init__()
    #
    #     for field in self.fields:
    #         self.fields[field].widget.attrs = {
    #             'class': 'form-control input-lg'
    #         }
