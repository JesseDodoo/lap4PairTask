from django.shortcuts import render
from .models import short_url
from .forms import UrlForm
from .shortener import shortener

# Create your views here.
def Make(request):
    form = UrlForm(request.POST)
    a = ''
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortener().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid Url"  
    return render(request, 'home.html', {'form': form, 'a': a})
