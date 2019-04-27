from django.contrib import admin
from .models import  *
# Register your models here.

class userAdmin(admin.ModelAdmin):
    readonly_fields = ('updated',)


admin.site.register(user,userAdmin)

