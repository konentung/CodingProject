from django.db import models
from django.contrib.auth.models import AbstractUser

# User model
class User(AbstractUser):
    name = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    permission = models.IntegerField(default=0, null=True, blank=True) # 0: user, 1: admin, 2: super admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

def get_default_level():
    return Level.objects.first().id if Level.objects.exists() else None
    
# UserInfo model
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    cname = models.CharField(max_length=50, null=True, blank=True)
    ename = models.CharField(max_length=100, null=True, blank=True)
    identification_number = models.CharField(max_length=10, null=True, blank=True)
    job = models.ForeignKey('Job', on_delete=models.CASCADE, null=True, blank=True)
    company = models.TextField(null=True, blank=True)
    school = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, default=get_default_level, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Level(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name