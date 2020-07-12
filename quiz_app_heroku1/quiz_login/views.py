from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm as ucf
from django.contrib.auth import login, authenticate
# Create your views here.
def login_1(request):
    if request.method =='POST':
       form=ucf(request.POST)
       if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(request,username=username, password=raw_password)
          login(request,user)
          return redirect('home')
    else:
       form=ucf()
    return render(request,'login.html',{'form':form})