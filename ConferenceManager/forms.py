from django.contrib.auth import get_user_model
from django import forms

ACC_CHOICES = (
        ('Participant', 'Participant'),
        ('Steering', 'Steering'),
    )

class SignupForm(forms.Form):
    # last_name = forms.CharField(max_length=30, label='Achternaam')
    first_name = forms.ChoiceField(choices = ACC_CHOICES) 


    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        # user.user_type = self.cleaned_data['user_type']
        user.save()