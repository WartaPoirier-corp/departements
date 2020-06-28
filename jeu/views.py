from django.http import HttpResponse


def index(request):
    return HttpResponse("Bienvenue dans le jeu des départements")
