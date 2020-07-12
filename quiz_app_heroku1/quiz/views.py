from django.shortcuts import render,redirect
from django.http import HttpResponse
from quiz_handle.models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context={
        'posts' : Post.objects.all()
    }
    if request.method =='POST':
        count = 0
        try:
            y=len(context['posts'])
            for i in range(y):
                if request.POST[f'{i+1}'] == context['posts'][i].answer :
                    count=count+1
                else:
                    print('got wrong')
            return HttpResponse(f'<div><h1>your score is {count}/10</h1><h1>You did well</h1></div>')
        except :
            return render(request,'neew.html',context)
    return render(request,'neew.html',context)







