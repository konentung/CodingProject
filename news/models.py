from django.db import models
from accounts.models import User

class NewsUnit(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_show = models.BooleanField(default=True)
    click_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='news_images', null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name

class NewsComment(models.Model):
    news = models.ForeignKey(NewsUnit, on_delete=models.CASCADE, null=False)
    author = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]