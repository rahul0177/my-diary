from django.shortcuts import render,redirect,get_object_or_404
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic import ListView,DetailView
import requests


# Create your views here.

def first(request):
    try:
        url='https://api.unsplash.com/photos/?client_id=c85822cd88daf26838bcef9e1cc322ff768663add37afdf25e2fbfea73de5945'
        response=requests.get(url).json()
        images=[]
        for item in response:
            images.append(item['urls']['regular'])
        return render(request,'first.html',{'images':images})
    except ConnectionError:
        return render(request,'first.html')
@login_required
def index(request):
    entries=Entry.objects.all()
    return render(request,'index.html',{'entries':entries})

def add(request):
    if request.method=='POST':
        form=EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=EntryForm()
    return render(request,'add.html',{'form':form})
def diaryview(request,pk):
    diary=get_object_or_404(Entry,pk=pk)
    template_name='diary_detail.html'
    return render(request,'diary_detail.html',{'object':diary})
def updatediary(request,pk):
    diary=get_object_or_404(Entry,pk=pk)
    template_name='add.html'
    form=EntryForm(request.POST,instance=diary)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form=EntryForm()
        return render(request,template_name,{'form':form})
def deletediary(request,pk):
    diary=get_object_or_404(Entry,pk=pk)
    template_name='entry_delete_confirm.html'
    if request.method=='POST':
        diary.delete()
        return redirect('home')
    else:
        return render(request, template_name, {'object':diary})



class Signup(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='signup.html'



