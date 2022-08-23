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

    def __str__(self):
        return self.email


class Category(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        Category, related_name="tasks", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class TrainProgram(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name="programs", on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, related_name="programs")

    def __str__(self):
        return self.name


class Train(models.Model):

    program = models.ForeignKey(
        TrainProgram, related_name="trains", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, related_name="trains", on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


