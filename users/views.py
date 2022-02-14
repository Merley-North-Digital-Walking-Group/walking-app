from django.shortcuts import get_object_or_404, render
from .models import App_User
from groups.models import Group


# Create your views here.
def login_email(request):
    return render(request, 'users/login_email.html', {})

def login_facebook(request):
    return render(request, 'users/login_facebook.html', {})

def login_google(request):
    return render(request, 'users/login_google.html', {})

def create_user(request):
    return render(request, 'users/create_user.html', {})

def user_homepage(request, pk):
    user = get_object_or_404(App_User, pk=pk)
    return render(request, 'users/user_homepage.html', {'user': user}) 
    

    
    