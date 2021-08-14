
from appointments.models import Appointment, Service
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class NewAppointmentForm(forms.ModelForm):
	service_type = forms.ModelChoiceField(queryset=Service.objects.all(), initial=0)
	class Meta:
		model = Appointment
		fields = ['service_type', 'scheduled_at', 'comments']