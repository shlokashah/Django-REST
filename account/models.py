from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .manager import UserManager
# Create your models here.
	
class User(AbstractUser): # create own custom User Model extending default django User
	objects = UserManager() 
	username = None
	email = models.EmailField(unique=True) #each user should have a unique email as it is the username field

	USERNAME_FIELD = 'email'  #setting email as the username field
	REQUIRED_FIELDS = []
	def __str__(self):
		return self.email

@receiver(post_save,sender=User)
def create_auth_token(sender,instance=None,created=False,**kwargs):
	if created:
		Token.objects.create(user=instance)  #everytime a new user registers create a new token for authentication 



