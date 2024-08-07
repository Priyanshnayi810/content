from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello jii")

def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def aboutus(request):
    return render(request,"aboutus.html")

def blog(request):
    return render(request,"blog.html")

def single_post(request):
    return render(request,"single_post.html")