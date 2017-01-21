from django.shortcuts import render

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'form/index.html')

def result(request):
    request.session['counter'] = request.session['counter'] + 1

    name = request.POST['name']
    city = request.POST['city']
    language = request.POST['language']
    comment = request.POST['comment']

    context = {
        'name':name,
        'city':city,
        'language': language,
        'comment': comment,
        'counter': request.session['counter']
        }

    return render(request, 'form/result.html', context)
