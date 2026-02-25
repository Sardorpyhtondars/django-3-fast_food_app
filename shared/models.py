from django.db import models

class Banner(models.Model):
    image = models.ImageField()
    discount = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=64)
    info = models.CharField(max_length=255)

    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
