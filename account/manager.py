from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError("No email") # raise error if email not present
		user = self.model(email=self.normalize_email(email),**extra_fields)  #setting email as unique and the username field
		user.set_password(password) # set the user password
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		user = self.create_user(email, password=password, **extra_fields)
		return user
