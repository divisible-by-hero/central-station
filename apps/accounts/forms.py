__author__ = 'Derek Stegelman'
__date__ = '9/5/12'


from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field

class RegistrationForm(forms.Form):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Field('username'),
            Field('sub_domain'),
            Field('email'),
            Field('password'),
            Field('password_confirm'),
        )


        return super(RegistrationForm, self).__init__(*args, **kwargs)

    username = forms.CharField()
    sub_domain = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password_confirm = forms.CharField()

