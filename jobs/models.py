from django.db import models
from accounts.models import User
from ckeditor.fields import RichTextField
from website.models import Category, SubCategory
from django.utils import timezone
from autoslug import AutoSlugField

CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)

class Job(models.Model):
    recruiter = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField(default="Default")
    category = models.ManyToManyField(SubCategory, blank=True, default="1")
    amount = models.CharField(max_length=255, default="0000")
    job_type = models.CharField(
        max_length=30, choices=CHOICES, default='Full Time', null=True)
    link = models.URLField(null=True, blank=True)
    telephone= models.CharField(max_length=50, default='0700000000')
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Applicants(models.Model):
    job = models.ForeignKey(
        Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField(default="Default")
    category = models.ManyToManyField(Category, blank=True)
    bid_amount = models.CharField(max_length=255, default="0000")

    def __str__(self):
        return self.applicant.email

class Selected(models.Model):
    job = models.ForeignKey(
        Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
