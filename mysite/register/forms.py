from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	OCCUPATION_CHOICES = [
    ("1", "Criminal lawyer"),
    ("2", "Environmental lawyer"),
    ("3", "Family lawyer"),
    ("4", "Corporate lawyer"),
    ("5", "Civil lawyer"),
	("6", "Tax lawyer"),
	("7", "Cyber lawyer"),
	("8", "Government lawyer"),
	("9", "Military lawyer"),
	("10", "Others")
    ]
	email = forms.EmailField()
	occupation = forms.ChoiceField(choices = OCCUPATION_CHOICES, required=False)
	bio = forms.CharField(max_length=1000, required=False)
	phone = forms.IntegerField(required=False)
	class Meta:
		model = User
		fields = ["username","first_name", "last_name", "email", "password1", "password2", "bio"]