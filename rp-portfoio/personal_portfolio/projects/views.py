from django.shortcuts import render
from .models import project
# Create your views here.

def project_index(request):
    projects = project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    projects = project.objects.get(pk= pk)
    context = {
        'project': projects
    }
    return render(request, 'project_detail.html', context)

