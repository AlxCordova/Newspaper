from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import	CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'gender', 'age',) # define el orden en que se visualice
        # help_texts = {
        #     'username': None,
        #     'password1': None,
        # }
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','password1',]:
            self.fields[fieldname].help_text = None


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'age',)