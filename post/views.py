from django.shortcuts import render, redirect
from post.models import UserInfo
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth import logout


def my_view(request):
    context = {'warning': 'User is not found'}
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signup')
    else:
        return render(request, 'signin.html', context)


def signin(request):
    context = {'warning': 'User is not found'}
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        name = request.POST.get('Name')
        password = request.POST.get('Password')
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')
        else:
            return render(request, 'signin.html', context)



def logout_view(request):
    logout(request)
    return redirect('signin')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def registr(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # name = request.POST.get('Name')
        # password = request.POST.get('Password')
        # email = request.POST.get('Email')
        # day = request.POST.get('sel_day')
        # month = request.POST.get('sel_month')
        # year = request.POST.get('sel_year')
        # birthday = str(year) + '-' + str(month) + '-' + str(day)
        # country = request.POST.get('Country')
        # city = request.POST.get('City')
        # user_all = UserInfo(email=email, login=name, password=password, birthday=birthday, country=country, city=city)
        # user_all.save()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        return redirect('home')
    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'registr.html', {'form': form})


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        return render(request, 'home.html')

