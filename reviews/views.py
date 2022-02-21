from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Review
# from .models import Walk
# from .models import App_User

# Create your views here.

def review_list(request):
    review_list = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'review_list': review_list})

def review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews/review.html', {'review': review})

# def review(request):
#     review = Review.walk_title() #creates an object listing all reviews for a particular walk
#     return review
