from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from post.models import UserInfo


def registr(reqest):
    if reqest.method == 'POST':
        name = reqest.POST.get('Name')
        password = reqest.POST.get('Password')
        email = reqest.POST.get('Email')
        day = reqest.POST.get('sel_day')
        month = reqest.POST.get('sel_month')
        year = reqest.POST.get('sel_year')
        birthday = str(year) + '-' + str(month) + '-' + str(day)
        country = reqest.POST.get('Country')
        city = reqest.POST.get('City')
        user_all = UserInfo(email=email, login=name, password=password, birthday=birthday, country=country, city=city)
        user_all.save()
        return redirect('home')
    elif reqest.method == 'GET':
        return render(reqest, 'registr.html')


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        return render(request, 'home.html')

