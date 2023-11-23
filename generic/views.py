from django.shortcuts import render

# Create your views here.
def rainy(request):
    return render(request,'rainy.html')

def thanvi(request):
    return render(request,'thanvi.html')