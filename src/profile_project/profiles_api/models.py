from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            name,
            password
        )

        # Make this user an admin.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        self.name

    def get_short_name(self):

        self.name

    def __str__(self):
        return self.email


# creating profile feed item 

class ProfileFeedItem(models.Model):
    '''profile status update'''
    user_profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    status_text=models.CharField(max_length=250)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text


