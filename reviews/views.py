from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Walk

# Create your views here.

# class WalkReviewsView(ListView):
#     model = Review
#     template_name = 'walks_detail.html'

def walk_reviews(request):
    walk_reviews = Walk.reviews()
    return render(request, 'walks/walks_detail.html', {'walk': walk_reviews})