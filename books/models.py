from django.db import models

# Create your models here.

from django.db import models
from users.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='books/', blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

