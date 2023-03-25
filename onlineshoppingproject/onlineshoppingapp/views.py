from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import Profile



# Create your views here.


def demo(request):
    obj=place.objects.all()
    obj1=Profile.objects.all()

    return render(request, "index1.html", {'result': obj, 'result1': obj1})


#def addition(request):
   # x = int(request.GET['num1'])
   # y = int(request.GET['num2'])
   # add1 = x + y
   # sub = x-y
  #  mul=x*y

 #   return render(request, "result.html", {'addition1': add1,'subtact': sub,'multiplication':mul})


# def contact(request):
#  return render(request, "contact.html")




# def detail(request):
# return render(request, "detail.html")


# def thanks(request):
#  return render(request, "thanks.html")
