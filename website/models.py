from django.db import models
from ckeditor.fields import RichTextField
# from accounts.models import User
from django.utils.translation import activate
from django.utils import timezone
from autoslug import AutoSlugField


CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)

# Create your models here.
class Category(models.Model):
    header_image = models.ImageField(null=True, blank=True, upload_to='main_categories')
    image = models.ImageField(null=True, blank=True, upload_to='main_categories')
    name= models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Main Categories"
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name

class ExpertTips(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/blog/')

    class Meta:
        verbose_name_plural = "Expert Tips"
    
    def __str__(self):
        return self.title

class FaqHeaders(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Faq Headers"
    
    def __str__(self):
        return self.title

class Faq(models.Model):
    headers = models.ForeignKey(FaqHeaders, related_name='faqheaders', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Faqs"
    
    def __str__(self):
        return self.title
    
class Legal(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Legal"
    
    def __str__(self):
        return self.title

class PremiumTitles(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='premium')
    name= models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Premium Categories"
    
    def __str__(self):
        return self.name

class Premium(models.Model):
    maintitle = models.CharField(max_length=50, default="premium header")
    premium_headers = models.ForeignKey(PremiumTitles, related_name='premiumheaders', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='premium')
    body = RichTextField()

    class Meta:
        verbose_name_plural = "Premium Services"
    
    def __str__(self):
        return self.maintitle
