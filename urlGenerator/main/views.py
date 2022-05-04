from django.shortcuts import render, redirect
from .models import short_url
from .forms import UrlForm
from .shortener import shortener

# Create your views here.
def Home(request, token):
    long_url = short_url.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

def Make(request):
    form = UrlForm(request.POST)
    a = ''
    data = short_url.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortener().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid Url"  
    return render(request, 'home.html', {'form': form, 'a': a, 'data': data})
