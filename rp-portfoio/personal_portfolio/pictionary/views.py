from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Picture

# Create your views here.
def piction(request):
    display = Picture.objects.all()
    context  = {
        "display" : display,
    }
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            indeed = redirect('success')
            return indeed
    else:
        form = ImageForm()
    return render(request, 'piction.html', context = {'form': form, 'display':display})

def success(request):
    return HttpResponse('successfuly uploaded')