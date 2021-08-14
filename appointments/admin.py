from django.contrib import admin

from .models import Appointment, Service

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'comments','created_at', 'scheduled_at','total_cost')
    list_display_links = ('id',)
    list_filter = ('scheduled_at','mechanic', 'customer', 'status', 'service_type')
    search_fields = ('customer','mechanic'),
    list_per_page = 25
    fields = ('service_type', 'customer', 'mechanic', 'status', 'comments','created_at', 'scheduled_at','total_cost')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost')
    list_display_links = ('name',)
    list_filter = ('name','cost')
    search_fields = ('name', 'cost')
    list_per_page = 25
    fields = ('id', 'name', 'cost')

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Service, ServiceAdmin)