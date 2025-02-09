from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "NavJeevan Admin"
admin.site.register(Patent)
admin.site.register(Doctor)
admin.site.register(Blood)
admin.site.register(Organ)
admin.site.register(Medicine)
admin.site.register(Prescription)