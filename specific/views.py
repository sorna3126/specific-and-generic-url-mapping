from django.shortcuts import render

# Create your views here.
def mubi(request):
    return render(request,'mubi.html')

def krish(request):
    return render(request,'krish.html')