from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,)
from django_countries.fields import CountryField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Create and return a `User` with an email, phone number, username and password.
        """
        if not email:
            raise ValueError("Users must have an email.")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if not password:
            raise ValueError("Superusers must have a password.")
        if not email:
            raise ValueError("Superusers must have an email.")

        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='email address')
    username = models.CharField(db_index=True, max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="users", null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=80)
    height = models.DecimalField(max_digits=5, decimal_places=2, default=180)
    phone = models.CharField(max_length=15, null=True, blank=True)
    country = CountryField()
    city = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    object = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Category(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name="category_task", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="author_task", on_delete=models.CASCADE)

class Train(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name="train_author", on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class Followers(models.Model):
    subscriber = models.ForeignKey(User, related_name="subscriber_followers", on_delete=models.CASCADE)
    publisher = models.ForeignKey(User, related_name="publisher_followers", on_delete=models.CASCADE)

class Support(models.Model):
    user = models.ForeignKey(User, related_name="user_support", on_delete=models.CASCADE)
    problem = models.TextField()
    status = models.CharField(max_length=30)
    date_opened = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField()

class Role(models.Model):
    type = models.CharField(max_length=200)

class UserRole(models.Model):
    user = models.ForeignKey(User, related_name="user_userRole", on_delete=models.CASCADE)
    role = models.ForeignKey(Role, related_name="role_userRole", on_delete=models.CASCADE)


    def __str__(self):
        return self.email


