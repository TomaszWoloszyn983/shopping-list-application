from django.shortcuts import render

# Create your views here.
def say_hello(request):
    print("Hello world")
    return render(request, "../templates/hello.html")