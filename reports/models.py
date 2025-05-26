from django.db import models
from accounts.models import User

# Report Model
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.ForeignKey('ReportType', on_delete=models.CASCADE, null=False)
    other_report_type = models.CharField(max_length=500, null=True)
    report_content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.report_type}"

# ReportType Model
class ReportType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name