from django.db import models

# Create your models here.
class User(models.Model):
    user_username=models.CharField(max_length=50,null=True)
    user_email=models.EmailField(max_length=20,null=True)
    user_password=models.CharField(max_length=20,null=True)
    user_confirmpassword=models.CharField(max_length=50,null=True)

def __self__(self):
    return self.user_username


