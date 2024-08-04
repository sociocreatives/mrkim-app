from django.shortcuts import get_object_or_404, render
from accounts.models import User, Category
from jobs.models import Job
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms import JobForm
from django.http import HttpResponse
from .models import Faq, FaqHeaders, Legal


def index(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()[:4]
    return render(request, 'website/index.html', {'categories': categories, 'jobs': jobs})

def jobs(request):
    current_user = request.user
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 4)  # Show 10 posts per page

    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the paginated page
    return render(request, 'website/jobs.html', { 'jobs': jobs, 'current_user': current_user, 'page_obj': page_obj})

def jobs_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'website/jobs_detail.html', {'job': job})

def categories(request):
    categories = Category.objects.all()
    # subcategory = SubCategory.objects.all()[:21]
    return render(request, 'website/categories.html', {'categories': categories})

def faq(request):
    faqs = FaqHeaders.objects.prefetch_related('faqheaders').all()
    return render(request, 'website/faq.html', {'faqs': faqs})

def safety(request):
    # faqs = FaqHeaders.objects.prefetch_related('faqheaders').all()
    return render(request, 'website/safety.html', {})

def legal(request):
    legal = Legal.objects.all()
    return render(request, 'website/legal.html', {'legal': legal})

def legal_detail(request, legal_id):
    legals = get_object_or_404(Legal, id=legal_id)
    return render(request, 'website/legal_detail.html', {'legals': legals})

def categories_detail(request, categories_id):
    category = get_object_or_404(Category, id=categories_id)
    subcategories = category.subcategories.all()
    return render(request, 'website/categories_detail.html', {'category': category, 'subcategories': subcategories})

def application(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return HttpResponse('Form submitted successfully!')
    else:
        form = JobForm()
    return render(request, 'website/application.html', {'form': form})

def mpesa_callback(request):
    if request.method == 'POST':
        data = request.body
        # Process callback data here
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'})