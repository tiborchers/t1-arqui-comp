from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from ipware import get_client_ip
from .models import Message
from .forms import PostForm
import datetime

def main(request):
    if request.method=="POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.timestamp= datetime.datetime.now()
             ip,_=get_client_ip(request)
             post.author_ip=ip
             post.save()
             return redirect('/')
    else:
        messages = Message.objects.all().reverse()
        form= PostForm()
        context = {'messages': messages, 'form': form}
        return render(request, 'chat.html', context)
