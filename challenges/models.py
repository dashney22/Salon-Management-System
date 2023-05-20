from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(max_length=255, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    publishedDate = models.DateField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(blank=True, upload_to='covers/')

    def __str__(self):       # This code helps modify the look o
        return self.name