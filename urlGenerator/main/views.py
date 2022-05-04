from django.shortcuts import render

# Create your views here.
def Make(request):
    return render(request, 'home.html')
