from django.shortcuts import render,redirect
from myapp.models import contactForms


# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def contact(request):
    return render(request,'contact.html')
def addData(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        obj = contactForms()
        obj.Name = name
        obj.Email = email
        obj.Subject = subject
        obj.Message = message

        obj.save()

        return redirect('contact')
    return render(request,"contact.html")
