# from django.http import HttpResponse
from django.shortcuts import render
from . models import Plants,Team

# Create your views here.
def demo(request):
    obj=Plants.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
# def home(request):
#     # name = 'india'
#     return render(request,'home.html')

#
# def about(request):
#     return render(request, "about.html")
#
#
# def contact(request):
#     return HttpResponse("helloo, this is my contact details")
#
#
# def details(request):
#     return HttpResponse(" details of this website")
#
#
# def thanks(request):
#     return render(request, "thanks.html")


# def result(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#
#     return render(request,"result.html",{'result1':add,'result2':sub,"result3":mul,'result4':div})
