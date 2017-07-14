from django.core.mail import EmailMessage
from django.shortcuts import render
from models import Review

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from math import floor
import os


def index(request):
    context = {}

    return render(request, 'valley_green_landscape/index.html', context)


def gallery(request):
    badge_template = """<button class="{0}" type="button" onclick="set_gallery_category('{1}');">{2} <span class="badge">{3}</span></button>"""
    
    badge_types = ['btn btn-primary', 'btn btn-warning', 'btn btn-danger', 'btn btn-success', 'btn btn-info', 'btn btn-muted']
    
    categories_path = 'valley_green_landscape/static/valley_green_landscape/img/gallery'
    
    categories = [i for i in os.listdir(categories_path)]
    
    badges = []
    
    for i in range(len(categories)):
        number_of_items = len(os.listdir(os.path.join(categories_path, categories[i])))
        badges.append(badge_template.format(badge_types[i%len(badge_types)], categories[i], categories[i], number_of_items))
        
    context = {
        'badges': badges,
        'main_image': '',
        'thumbnails':'', 
    }

    return render(request, 'valley_green_landscape/gallery.html', context)


def reviews(request):

    all_reviews = Review.objects.all().order_by('-pk')

    overall_score = sum([review.score for review in all_reviews]) / float(len(all_reviews))
    overall_score_star = int_to_star(floor(overall_score))

    context = {
        'overall_score_star': overall_score_star,
        'overall_score': round(overall_score, 1),
        'reviews': all_reviews,

    }

    return render(request, 'valley_green_landscape/reviews.html', context)


def contact(request):
    context = {}

    return render(request, 'valley_green_landscape/contact.html', context)


def about(request):
    context = {}

    return render(request, 'valley_green_landscape/about.html', context)


def send_email(request):
    if request.method == "POST":
        user_name = request.POST.get('user-name')
        user_email = request.POST.get('user-email')
        user_subject = request.POST.get('user-subject')
        user_message = request.POST.get('user-message')

        email = EmailMessage("{0} - {1}".format(user_name.upper(), user_subject.capitalize()), user_message,
                             to=[user_email])

        email.send()

        messages.add_message(request, messages.INFO, "Thank you for your email {0}!<br>\
        We will get in touch with you within 24 hours.".format(user_name))

        return HttpResponseRedirect(reverse('valley_green_landscape:contact'))


def add_review(request):
    user_name = request.POST.get('user-name')
    photo_url = request.POST.get('profile-img')
    review_text = request.POST.get('review-text')
    score = request.POST.get('review-score')

    new_review = Review() #user=user_name, photo=photo_url, text=review_text)

    new_review.user = user_name

    if len(photo_url) > 0:
        new_review.photo = photo_url

    new_review.text = review_text
    new_review.score = score
    new_review.star_score = int_to_star(int(score))

    new_review.save()

    messages.add_message(request, messages.INFO, user_name)

    return HttpResponseRedirect(reverse('valley_green_landscape:reviews'))


def int_to_star(score):
    html_tag = ""

    filled_star = '<span class="glyphicon glyphicon-star" aria-hidden="true" ></span>'
    empty_star = '<span class="glyphicon glyphicon-star-empty" aria-hidden="true" ></span>'

    if score == 1:
        filled_no = 1
        empty_no = 4

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no
    elif score == 2:
        filled_no = 2
        empty_no = 3

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no
    elif score == 3:
        filled_no = 3
        empty_no = 2

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no
    elif score == 4:
        filled_no = 4
        empty_no = 1

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no
    elif score == 5:
        filled_no = 5
        empty_no = 0

        html_tag += filled_star * filled_no
        html_tag += empty_star * empty_no

    return html_tag
