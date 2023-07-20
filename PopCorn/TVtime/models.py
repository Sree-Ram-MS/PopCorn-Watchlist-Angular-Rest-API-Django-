from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
    movie_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    dob = models.DateField()
    options=(
        ("Male","Male"),
        ("Female","Female"),
        ("other","other")
    )
    gender=models.CharField(max_length=100,choices=options,default="Male")
    phone = models.CharField(max_length=10,)
