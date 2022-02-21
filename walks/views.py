from ast import walk
from django.shortcuts import render, get_object_or_404
from .models import Walk #required to import information about the database table called 'Walk' in walks/models 
# from reviews.models import Review

# Create your views here.
def walks_list(request):
    walk_list = Walk.objects.all()#creates an object that refers back to the database table created in models called 'Walk' and assigns it a variable name 'walk_list'
    return render(request, 'walks/walks_list.html', {'walk_list': walk_list})

def walks_detail(request, pk):
    walk = get_object_or_404(Walk, pk=pk)
    return render(request, 'walks/walks_detail.html', {'walk': walk})

def walk_photo(request):
    walk_photo = Walk.photo()
    return render(request, 'walks/walks_detail.html', {'walk': walk_photo})


# def review_list(request):
#     review_list = Review.objects.all()
#     return render(request, 'walks/walks_detail.html', {'review_list': review_list})