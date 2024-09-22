from django.http import HttpResponse
import datetime

def test(request):
    print("test function is called from view")
    date=datetime.datetime.now()
    return HttpResponse("<h1>hello this is index page</h1>"+str(date))

def about(request):
    return HttpResponse("<h1>this is about page<h1/>")

def services(request):
    return HttpResponse("<h1>this is services page<h1/>")