from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})

def about(request):
    return render(request, 'pages/about.html', {})

def contact(request):
    return render(request, 'pages/contact.html', {})

def weather(request):
    return render(request, 'pages/weather.html', {})

def news(request):
    return render(request, 'pages/news.html', {})

def admin(request):
    return render(request, 'pages')



# def user_homepage(request):
#     user = get_object_or_404(App_User)
#     return render(request, 'users/user_homepage.html', {'user': user}) 