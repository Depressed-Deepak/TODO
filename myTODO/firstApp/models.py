from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = [
    ('not_started', 'Not Started'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
]

class TODO(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=50)
    date= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,  # Dropdown choices here
        default='not_started',  # Default value
    )
    def __str__(self):
        return f"{self.user}"