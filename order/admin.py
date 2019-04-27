from django.contrib import admin
from .models import  *
# Register your models here.
class orderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date','updated')

admin.site.register(order, orderAdmin)
