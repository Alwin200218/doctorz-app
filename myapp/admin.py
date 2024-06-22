from django.contrib import admin
from .models import Userdata,Doctorinfo,Appointmentinfo

# Register your models here.

admin.site.register(Userdata)
admin.site.register(Doctorinfo) 
admin.site.register(Appointmentinfo) 
