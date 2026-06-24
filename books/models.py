from django.db import models

class Book(models.Model):
    name = models.charfield(max_length=100)
    author = models.charfield(max_length=100)
    pages = models.IntegerField()
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name