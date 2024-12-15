from django.http import HttpResponseRedirect
from django.shortcuts import render
from portfolio.base.forms import Comentario

def home(request):
    if request.method == 'POST':
        form = Comentario (request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reversed('portfolio:home'))
        else:
            return render(request, 'portfolio/projeto01.html', {'form':form}, status=400)
    return render(request, 'portfolio/projeto01.html')

