from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.contrib import  auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.contrib.auth import get_user_model

from .models import Customer, Mechanic
from appointments.models import Appointment, Service

from .forms import NewAppointmentForm, UserRegisterForm

import json


User = get_user_model()


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

def newAppointment(request, slug):
    form = NewAppointmentForm(request.POST, request.FILES)
    if form.is_valid():
        app = form.save(commit=False)
        app.customer = Customer.objects.get(User=request.user)
        app.mechanic = Mechanic.objects.order_by('?').first()
        for s in app.service_type:
            app.total_cost = s.cost
    else:
        print(':(')
        form = NewAppointmentForm()
    print(form.errors)
    return render(request, 'users/home.html', {'form': form})


class AppointmentListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'users/home.html'
    context_object_name = 'appointments'
    paginate_by = 12
    def get_context_data(self, **kwargs):
        context = super(AppointmentListView, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('slug'))
        p = Customer.objects.filter(user=user).first()
        app_list = Appointment.objects.filter(customer=p).order_by('-created_at')
      
        for a in app_list:
            service_list = []
            for s in a.service_type.all():
                service_list.append(s)
            a.service_list = service_list
            a.mechanic_name = a.mechanic.first()

        all_available_services = Service.objects.filter().all()
        context['u'] = user
        context['appointments'] = app_list
        context['allservices'] = all_available_services
        return context
    
    def get_queryset(self):
        user = get_object_or_404(Customer, slug=self.kwargs.get('slug'))
        return Appointment.objects.filter(customer=user).order_by('-created_at')