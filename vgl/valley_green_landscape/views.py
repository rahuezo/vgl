from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from models import Review


def index(request):
    context = {}

    return render(request, 'valley_green_landscape/index.html', context)


def gallery(request):
    context = {}

    return render(request, 'valley_green_landscape/gallery.html', context)


def reviews(request):

    all_reviews = Review.objects.all()
    all_reviews.reverse()

    context = {
        'reviews': all_reviews,
    }

    return render(request, 'valley_green_landscape/reviews.html', context)


def contact(request):
    context = {}

    return render(request, 'valley_green_landscape/contact.html', context)


def about(request):
    context = {}

    return render(request, 'valley_green_landscape/about.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user, template_name='registration/login.html')
            return redirect('valley_green_landscape:reviews')
    else:
        form = SignUpForm()
    return render(request, 'valley_green_landscape/signup.html', {'form': form})
