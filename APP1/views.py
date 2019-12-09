from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def index_y(request):
    return render(request,'yaopeng.html')