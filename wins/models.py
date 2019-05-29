from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from pyuploadcare.dj.models import ImageField
from django import forms


class Profile(models.Model):
    '''
    Method to create profile table
    '''
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    pic = ImageField(blank=True, manual_crop="")
    bio = models.CharField(default="Hi!", max_length = 30)
    
    def save_profile(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    
    @classmethod
    def search_user(cls,name):
        return User.objects.filter(username__icontains = name)

class Image(models.Model):
    image = ImageField(blank=True, manual_crop="")    
    title = models.CharField(max_length = 31, blank = True)
    posted_by = models.CharField(max_length = 50, blank = True)
    # likes = models.ManyToManyField(User, related_name = "likes", blank = True)
    user = models.ForeignKey(User,null = True , blank = True , on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True, blank = True)
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200,)

    def save_image(self):
        self.save()

    def delete_image(self):
        cls.objects.get(id = self.id).delete()

    def update_posted_by(self,new_posted_by):
        self.posted_by = new_caption
        self.save()