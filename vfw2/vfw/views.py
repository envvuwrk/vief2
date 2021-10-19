from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def sponsors(request):
    return render(request,'sponsors.html')
def designers(request):
    return render(request,'designers.html')

def register(request):
    return render(request,'register.html')
def designer(request):
    return render(request,'designer.html')
def categoryd(request):
    return render(request,'categoryd.html')
def passport(request):
    return render(request,'passport.html')
def submit(request):
    return render(request,'submit.html')

def model(request):
    return render(request,'model.html')
def measurement(request):
    return render(request,'measurement.html')
def model(request):
    return render(request,'model.html')
def mp(request):
    return render(request,'mp.html')
def msubmit(request):
    return render(request,'msubmit.html')

def exhibitor(request):
    return render(request,'exhibitor.html')
def excat(request):
    return render(request,'excat.html')
def expayment(request):
    return render(request,'expayment.html')
def expassport(request):
    return render(request,'expassport.html')

def exsubmit(request):
    return render(request,'exsubmit.html')




def contact(request):
    return render(request,'contact.html')
def gallery(request):
    return render(request,'gallery.html')
def seven(request):
    return render(request,'seven.html')
def nine(request):
    return render(request,'nine.html')

