from django.db import models

# Create your models here.
class text(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    update_day = models.DateField(auto_now=True)
    create_day = models.DateField(auto_now_add=True)
