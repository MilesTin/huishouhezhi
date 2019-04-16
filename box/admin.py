from django.contrib import admin
from .models import heZhi
# Register your models here.



class dateAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
   # list_display = ('id','iconPath','latitude','longitude','width','height','name','address')

admin.site.register(heZhi,dateAdmin)
