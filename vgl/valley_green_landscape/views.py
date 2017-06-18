from django.shortcuts import render

def index(request):
	context = {}
	
	return render(request, 'valley_green_landscape/index.html', context)

def gallery(request):
	context = {}
	
	return render(request, 'valley_green_landscape/gallery.html', context)

def reviews(request):
	context = {}
	
	return render(request, 'valley_green_landscape/reviews.html', context)

def contact(request):
	context = {}
	
	return render(request, 'valley_green_landscape/contact.html', context)

def about(request):
	context = {}
	
	return render(request, 'valley_green_landscape/about.html', context)


