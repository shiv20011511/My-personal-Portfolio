from django.shortcuts import render
from portfolio.forms import shivpquery
from portfolio.models import query
# Create your views here.
def home(request):
    if request.method=="POST":
        que=shivpquery(request.POST)
        if que.is_valid():
            try:
                que.save()
            except:
                pass
    else:
        que=shivpquery()
    return render(request,'main.html',{'port':que})
