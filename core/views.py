from django.shortcuts import render, redirect, reverse


def home_or_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('accounts:home'))
    else:
        return redirect(reverse('accounts:login'))
