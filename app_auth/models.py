from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django_countries.fields import CountryField

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        
        if not email:
            raise ValueError('Desolé, veuillez saisir un email')
        
        email=self.normalize_email(email)
        user=self.model(email=email,username=username)
        
        user.set_password(password)
        
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user=self.create_user(email,username,password)
        
        user.is_admin=True
        
        user.save(using=self._db)
        return user   

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, default='Anonymous', unique=True)
    email = models.EmailField(max_length=254, unique=True,blank=True,null=True)
  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # USERNAME_FIELD='email'
    # REQUIRED_FIELDS=['username']

    USERNAME_FIELD='username'
    # REQUIRED_FIELDS=['username']
    
    objects= UserProfileManager()
    
    class Meta:
        verbose_name="Profil"

    def __str__(self) -> str:
        return self.username

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin