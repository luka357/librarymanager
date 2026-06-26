from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.firs_name} {self.last_name}"