from django.contrib import admin

from .models import Customer, Car, Mechanic

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('slug','phone_number', 'car')
    list_display_links = ('slug',)
    search_fields = ('slug'),
    list_per_page = 25
    fields = ('slug','phone_number', 'car')


class CarAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'engine_type', 'make','model', 'year','licence_detail')
    list_display_links = ('id',)
    list_filter = ('category','engine_type', 'make', 'year')
    search_fields = ('make','year', 'engine_type', 'category'),
    list_per_page = 25
    fields = ('id','category', 'engine_type', 'make','model', 'year','licence_detail')


class MechanicAdmin(admin.ModelAdmin):
    list_display = ('id','slug')
    list_display_links = ('id','slug')
    search_fields = ('slug'),
    list_per_page = 25
    fields = ('id','slug')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car,CarAdmin)
admin.site.register(Mechanic, MechanicAdmin)