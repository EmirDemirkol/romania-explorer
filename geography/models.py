from django.db import models

class Area(models.Model):
    name = models.CharField(max_length=200)
    area_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Attraction(models.Model):
    name = models.CharField(max_length=200)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='attractions/', blank=True, null=True)

    def __str__(self):
        return self.name
