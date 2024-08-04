from django.shortcuts import render
from accounts.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.urls import path


def joblistings(request):
    return render(request, 'website/index.html')

