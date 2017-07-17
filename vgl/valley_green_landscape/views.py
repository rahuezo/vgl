from django.core.mail import EmailMessage
from django.shortcuts import render
from models import Review, GalleryContainer, GalleryImage

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from math import floor
import os


def index(request):
    context = {}

    return render(request, 'valley_green_landscape/index.html', context)

def services(request):
    context = {}

    return render(request, 'valley_green_landscape/services.html', context)

def gallery(request):

    context = {
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

        user_address = request.POST.get('address-line')
        user_city = request.POST.get('city-line')
        user_state = request.POST.get('state-line')
        user_zip = request.POST.get('zip-line')

        user_subject = request.POST.get('user-subject')
        user_message = request.POST.get('user-message')

        to_email = 'rahuezo@ucdavis.edu'

        email_subject = user_subject.upper()

        location = """
        {0}
            {1}
            {2},{3}
        """.format(user_address, user_city, user_state, user_zip)

        email_body = """
        Subject:
            {0}
        Email:
            {1}

        Name:
            {2}

        Location:
            {3}

        Content:
            {4}

        """.format(email_subject, user_email, user_name.upper(), location, user_message)


        email = EmailMessage("{0} - {1}".format(user_name.upper(), email_subject), email_body,
                             to=[to_email])

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
