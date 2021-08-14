from django.urls import path, include
from users import views as user_views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.AppointmentListView.as_view()), name='home'),
    path('appointment/new/', views.newAppointment, name='newApp'),


]