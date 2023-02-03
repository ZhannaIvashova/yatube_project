from django.shortcuts import render

from django.http import HttpResponse

def index (request):
    return HttpResponse ('Главная страница социальной сети YATUBE')

def group_posts (request, slug): 
    return HttpResponse (f'Страница для размещения постов {slug}')   
