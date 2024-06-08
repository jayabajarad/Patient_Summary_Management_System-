from django.contrib import admin
from .models import *
admin.site.register(UserProfile)
admin.site.register(Hospital)
admin.site.register(Patient)
admin.site.register(Report)
