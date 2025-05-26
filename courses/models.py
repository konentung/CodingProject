from django.db import models
from accounts.models import User

# Courses model
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    apply_url = models.URLField(null=True, blank=True)
    max_people = models.IntegerField(null=True, blank=True)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    course_start_datetime = models.DateTimeField(null=True, blank=True)
    course_end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class CourseApply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    apply_datetime = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    is_completed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.status}"