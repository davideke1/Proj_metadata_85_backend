from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import fileUpload
from django.views import generic
from .forms import FileForm

def homepage(request):
    return HttpResponse("HEllo world")

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def UploadFile(request):
    return render(request,'index.html')

def UploadFilea(request):
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = FileForm()
        context = {
            'form':form,
        }
    return render(request, 'xtracto.html', context)


