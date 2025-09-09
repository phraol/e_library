from django.db import models
from users.models import User

# College & Department for categorization
class College(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return f"{self.name} ({self.college.name})"

# Book model
class Book(models.Model):
    FORMAT_CHOICES = (
        ('PDF', 'PDF'),
        ('HARDCOPY', 'Hardcopy'),
    )

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    book_file = models.FileField(upload_to='books/', blank=True, null=True)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default='PDF')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='books')
    hardcopy_available = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.format})"