from django.contrib import admin
from dashboard.models import *
# Register your models here.
class detailsAdmin(admin.ModelAdmin):
    list_details=['st_fullname','st_weight','st_height','st_age','st_goal','st_time']
admin.site.register(details,detailsAdmin)
