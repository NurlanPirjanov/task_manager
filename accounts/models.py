from django.db import models
from django.contrib.auth.models import AbstractUser
class RoleUser(models.Model):
	short_name = models.CharField(max_length=10)
	full_name = models.CharField(max_length=60)
	def __str__(self):
		return self.full_name

class CustomUser(AbstractUser):
	role_user = models.ForeignKey(RoleUser, on_delete=models.CASCADE, blank=True, null=True)
	phone_number = models.CharField(max_length=13, blank=True, null=True, default='998901234567')
	avatar = models.ImageField(upload_to='media/', null=True)