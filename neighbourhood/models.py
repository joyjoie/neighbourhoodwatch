from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image/")
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)