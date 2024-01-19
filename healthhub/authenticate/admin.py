from django.contrib import admin

# Register your models here.
from authenticate.models import User
class UserAdmin(admin.ModelAdmin):
    list_display=['user_username','user_email','user_password','user_confirmpassword']
admin.site.register(User,UserAdmin)   

