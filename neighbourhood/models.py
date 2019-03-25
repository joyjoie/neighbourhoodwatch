from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image/")
    location = models.TextField()
    # pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}' 


    def save_neighbourhood(self):
        self.save()

    @classmethod
    def display_neighbourhood(cls):
        return cls.objects.all()

    def delete_neighbourhood(self):
        Neighbourhood.objects.all().delete()
    
   
    



class Business(models.Model):
    name = models.CharField(max_length=60)
    user= models.ForeignKey(User)
    nei = models.ForeignKey(Neighbourhood)
    bemail= models.TextField()

    def __str__(self):
        return f'{self.name}' 

    def save_business(self):
        self.save()

    @classmethod
    def display_business(cls):
        return cls.objects.all()

    def delete_business(self):
        Neighbourhood.objects.all().delete()
    
    def update(self): 
       Neighbourhood.objects.filter(id = 2).update()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=60 ,blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.TextField(blank=True)
    neighbourhoodname = models.ForeignKey(Neighbourhood,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
       self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, bio):
        self.bio = bio
        self.save()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def pro(self):
        return self.objects.all()

 


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Comments(models.Model):
    img = models.ForeignKey(Neighbourhood)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=60)

    @classmethod
    def display_comments(cls):
        return cls.objects.all()

    def save_comments(self):
        self.save()


