from atexit import register
from django.contrib import admin
from .models import product,order
from django.contrib.auth.models import Group

admin.site.site_header = 'Inventory Dashboard'

class productAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity',)
    list_filter=('category',)

# Register your models here.
admin.site.register(product, productAdmin)
admin.site.register(order)
#admin.site.unregister(Group)