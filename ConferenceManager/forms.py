from django.contrib.auth import get_user_model
from django import forms

ACC_CHOICES = (
    ('Listener', 'Listener'),
    ('Speaker', 'Speaker'),
    ('Chair', 'Chair'),
)


class SignupForm(forms.Form):
    first_name = forms.ChoiceField(choices=ACC_CHOICES)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.save()
