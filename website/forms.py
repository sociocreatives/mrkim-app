from django import forms
from django.forms import ModelForm
from jobs.models import Job

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['recruiter', 'title', 'company', 'company', 'location', 'description', 'category', 'amount', 'job_type', 'link', 'telephone']