from django.shortcuts import render
from .models import Hero, Media, Technology, Tools, Project

# Create your views here.
def home(request):
    hero = Hero.objects.filter().first();
    media = Media.objects.filter().first();
    technologies = Technology.objects.all();
    tools = Tools.objects.all();
    projects = Project.objects.all();
    context = {
        'hero': hero,
        'media': media,
        'technologies': technologies,
        'tools': tools,
        'projects': projects,
    }
    return render(request, 'home.html', context);
