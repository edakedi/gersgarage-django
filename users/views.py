from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib import  auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
import json

from .models import Customer
from appointments.models import Appointment

from .forms import UserRegisterForm

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            context = {'status': 1, 'message' : 'Success'}
            return HttpResponse(json.dumps(context), content_type='application/json')
        else:
            return redirect('login')
    else:
        return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.username = str(form_instance.username).lower()
            form_instance.save()
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class AppointmentListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'users/home.html'
    context_object_name = 'appointments'
    paginate_by = 12
    def get_context_data(self, **kwargs):
        context = super(AppointmentListView, self).get_context_data(**kwargs)
        user = get_object_or_404(Customer, username=self.kwargs.get('slug'))
        p = Customer.objects.filter(user=user).first()
        app = Appointment.objects.filter(customer=p).order_by('-created_at')
        
        context['u'] = user
        context['appointments'] = app
        return context
    
    def get_queryset(self):
        user = get_object_or_404(Customer, username=self.kwargs.get('slug'))
        return Appointment.objects.filter(customer=user).order_by('-created_at')