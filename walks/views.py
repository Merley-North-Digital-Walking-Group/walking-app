from django.shortcuts import render

# Create your views here.
def walks(request):
    return render(request, 'walks/walks.html', {})