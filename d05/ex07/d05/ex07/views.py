from django.shortcuts import render
from django.http import HttpResponse
from django.forms import Form
from .forms import UpdateForm
from ex07.models import Movies

# Create your views here.
def populate(request):
    buf = ""
    data = [
        {
            'title': "The Phantom Menace",
            'episode_nb': 1,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "Attack of the Clones",
            'episode_nb': 2,
            'opening_crawl': "",
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-16"
        },
        {
            'title': "Revenge of the Sith",
            'episode_nb': 3,
            'opening_crawl': None,
            'director': "George Lucas",
            'producer': "Rick McCallum",
            'release_date': "2005-05-19"
        },
        {
            'title': "A New Hope",
            'episode_nb': 4,
            'opening_crawl': None,
            'director': "George Lucas",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1999-05-19"
        },
        {
            'title': "The Empire Strikes Back",
            'episode_nb': 5,
            'opening_crawl': None,
            'director': "Irvin Kershner",
            'producer': "Gary Kutz, Rick McCallum",
            'release_date': "1980-05-17"
        },
        {
            'title': "Return of the Jedi",
            'episode_nb': 6,
            'opening_crawl': None,
            'director': "George Lucas",
            'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
            'release_date': "1983-05-25"
        },
        {
            'title': "The Force Awakens",
            'episode_nb': 7,
            'opening_crawl': "",
            'director': "J. J. Abrams",
            'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            'release_date': "2015-12-11"
        },
    ]
    for movie in data:
        try:
            new_row = Movies(**movie)
            new_row.save()
            buf += "OK<br>"
        except Exception as e:
            buf += "Error: %s :: %s<br>" % (movie['title'], e)
    return HttpResponse(buf)

def display(request):
    try:
        response = Movies.objects.all()
    except Exception as e:
        return HttpResponse("No data available")
    if response:
        return render(request, 'ex07/display.html', {'data': response})
    else:
        return HttpResponse("No data available")

def remove(request):
    form = Form()

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid() and request.POST['select'][0]:
            Movies.objects.filter(pk=request.POST['select'][0]).delete()

    response = Movies.objects.all()
    if response:
        return render(request, 'ex07/remove.html', {'data': response, 'form': form})
    else:
        return HttpResponse("No data available")
    return HttpResponse("No data available")

def update(request):
    form = UpdateForm()

    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid() and request.POST['select'][0]:
            obj = Movies.objects.get(pk=request.POST['select'][0])
            obj.opening_crawl = request.POST['opening_crawl']
            obj.save()

    response = Movies.objects.all()
    if response:
        return render(request, 'ex07/update.html', {'data': response, 'form': form})
    else:
        return HttpResponse("No data available")
    return HttpResponse("No data available")
