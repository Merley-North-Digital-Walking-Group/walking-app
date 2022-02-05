from django.shortcuts import render

# Create your views here.
def walks_list(request):
    return render(request, 'walks/walks_list.html', {})

def walks_detail(request):
    return render(request, 'walks/walks_detail.html', {})