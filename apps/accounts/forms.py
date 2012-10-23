__author__ = 'Derek Stegelman'
__date__ = '9/5/12'


from django import forms
from django.forms.widgets import PasswordInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field

class RegistrationForm(forms.Form):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.help_text_inline = True
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Field('username'),
            Field('company_name'),
            Field('email'),
            Field('password'),
            Field('password_confirm'),
        )


        super(RegistrationForm, self).__init__(*args, **kwargs)

    username = forms.CharField()
    company_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password_confirm = forms.CharField()

class UserProfileForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        
        super(UserProfileForm, self).__init__(*args, **kwargs)

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    change_password = forms.CharField(required=False, widget=PasswordInput)
    change_password_confirm = forms.CharField(required=False, widget=PasswordInput)

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()
        if cleaned_data.get('password', None):
            password = cleaned_data.get('change_password')
            confirm = cleaned_data.get('change_password_confirm')
            if password != confirm:
                raise forms.ValidationError('Password and Confirm password must match.')

        return cleaned_data