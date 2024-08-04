# from datetime import timezone
from django.utils import timezone
from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager 
from website.models import Category

class CustomeUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db),

        return user
    
    def create_user(self, email=None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)

    # ROLES
    ADMINISTRATOR = 1
    CORPORATE = 2
    EMPLOYER = 3
    JOBSEEKER = 4
    ROLE_CHOICES = (
        (ADMINISTRATOR, "Administrator"),
        (CORPORATE, 'Corporate'),
        (EMPLOYER, 'Employer'),
        (JOBSEEKER, 'Jobseeker'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomeUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username or self.email.split('@')[0]


    def __str__(self):
        return self.username

class Tvets(models.Model):
    name= models.CharField(max_length=150)
    class Meta:
        verbose_name_plural = "Tvets"
    
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='images/userprofiles')
    cover_photo = models.ImageField(null=True, blank=True, upload_to='images/coverphoto')
    badge = models.ImageField(null=True, blank=True, upload_to='images/badge')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    ast = (
        ('Path to Pro Skills program through TVET', 'Path to Pro Skills program through TVET'),
        ('Not Applicable', 'Not Applicable'),
    )
    applicable_skills_training = models.CharField(
        null=True, blank=True,
        max_length=50,
        choices=ast,
    )
    tvets = models.ForeignKey(Tvets, null=True, blank=True, on_delete=models.CASCADE)
    location= models.CharField(max_length=50)
    telephone= models.CharField(max_length=50, default='0700000000')
    job_title= models.CharField(max_length=50, blank=True,)
    bio = models.TextField(null=True)
    et_choice = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contractor', 'Contractor')
    )
    employment_type = models.CharField(
        null=True, blank=True,
        max_length=30,
        choices=et_choice,
        default='Full Time'
    )
    yoe = (
        ('Entry level 0-2 years', 'Entry level 0-2 years'),
        ('Intermediate 2-5 years', 'Intermediate 2-5 years'),
        ('Expert 5-10 years', 'Expert 5-10 years'),
        ('Management 10+ years', 'Management 10+ years'),
    )
    years_of_experience = models.CharField(
        null=True, blank=True,
        max_length=30,
        choices=yoe,
        default='Entry level 0-2 years'
    )

    avail = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    )
    availability = models.CharField(
        null=True, blank=True,
        max_length=30,
        choices=avail,
        default='Available'
    )
    is_availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "User Profile"
    
    def __str__(self):
        return self.user.email
    