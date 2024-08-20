from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:job_id>/', views.jobs_detail, name='jobs_detail'),
    path('jobs/', views.jobs, name='jobs'),
    path('faq/', views.faq, name='faq'),
    path('safety/', views.safety, name='safety'),
    path('legal', views.legal, name='legal'),
    path('legal/<int:legal_id>/', views.legal_detail, name='legal_detail'),
    path('jobs/<int:job_id>/', views.jobs_detail, name='jobs_detail'),
    path('premium', views.premium, name='premium'),
    path('premium/<int:premium_id>/', views.premium_detail, name='premium_detail'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:categories_id>/', views.categories_detail, name='categories_detail'),
    path('categories/<int:categories_id>/', views.categories, name='categories'),
    path('application/', views.application, name='application'),
    path('callback/', views.mpesa_callback, name='mpesa_callback'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_results, name='search_results'),
]