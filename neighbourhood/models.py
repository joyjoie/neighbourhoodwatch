from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image/")
    location = models.TextField()
    # pub_date = models.DateTimeField(auto_now_add=True)

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def display_neighbourhood(cls):
        return cls.objects.all()

    def delete_neighbourhood(self):
        Neighbourhood.objects.all().delete()
    
    def update(self): 
       Neighbourhood.objects.filter(id = 2).update(name ='Kim')

class User(models.Model):
    name = models.CharField(max_length=60)
    nhood= models.ForeignKey(Neighbourhood)
    email= models.TextField()

class Business(models.Model):
    name = models.CharField(max_length=60)
    user= models.ForeignKey(User)
    nei = models.ForeignKey(Neighbourhood)
    bemail= models.TextField()

    def save_business(self):
        self.save()

    @classmethod
    def display_business(cls):
        return cls.objects.all()

    def delete_business(self):
        Neighbourhood.objects.all().delete()
    
    def update(self): 
       Neighbourhood.objects.filter(id = 2).update(name ='Kim')