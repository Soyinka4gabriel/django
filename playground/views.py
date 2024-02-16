from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request):
    return HttpResponse("Hello there !!!")
def good(request):
    y = 3
    x = 34
    return render(request, 'hello.html')
# Create your views here.
