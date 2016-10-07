from django.shortcuts import render

# Create your views here.

def affichage(request):
    return render(request, 'ex01/content.html', {
        'title': 'Ex01 : Processus d’affichage d’une page statique.',
        'stylesheet': 'ex01/style1.css',
        'iframe_src': 'http://orm.bdpedia.fr/mvc.html'}
    )

def django(request):
    return render(request, 'ex01/content.html', {
        'title': 'Ex01 : Django, framework web.',
        'stylesheet': 'ex01/style1.css',
        'iframe_src': 'https://fr.wikipedia.org/wiki/Django_%28framework%29'}
    )

def templates(request):
    return render(request, 'ex01/content.html', {
        'title': 'Ex01 : Moteur de templates.',
        'stylesheet': 'ex01/style2.css',
        'iframe_src': 'https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django/les-templates-3'}
    )