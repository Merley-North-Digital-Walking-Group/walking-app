from django.shortcuts import render
from .models import Walk #required to import information about the database table called 'Walk' in walks/models 

# Create your views here.
def walks_list(request):
    return render(request, 'walks/walks_list.html', {})

def walks_detail(request):
    walk_list = Walk.objects.all()#creates an object that refers back to the database table created in models called 'Walk' and assigns it a variable name 'walk_list'
    return render(request, 'walks/walks_detail.html', {'walk_list': walk_list})# this creates a dict object here with the variable name assigned above