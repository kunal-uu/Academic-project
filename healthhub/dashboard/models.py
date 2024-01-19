from django.db import models

# Create your models here.
class details(models.Model):
    st_fullname=models.CharField(max_length=50,null=False)
    st_weight=models.IntegerField(null=False)
    st_height=models.IntegerField(null=False)
    st_age=models.IntegerField(null=False)
    st_goal=models.IntegerField(null=False)
    st_time=models.IntegerField(null=False)
    #st_time=models.IntegerField(null=True)

def __self__(self):
    return self.st_fullname

