from django.shortcuts import render
from .forms import Form

articles = [
    {
        'title': 'title',
        'content': 'content',
        'img': 'https://s1.1zoom.ru/big3/984/Canada_Parks_Lake_Mountains_Forests_Scenery_Rocky_567540_3840x2400.jpg'
    },
    {
        'title': 'title',
        'content': 'content',
        'img': 'https://s1.1zoom.ru/big3/984/Canada_Parks_Lake_Mountains_Forests_Scenery_Rocky_567540_3840x2400.jpg'
    },
    {
        'title': 'title',
        'content': 'content',
        'img': 'https://s1.1zoom.ru/big3/984/Canada_Parks_Lake_Mountains_Forests_Scenery_Rocky_567540_3840x2400.jpg'
    },
]


def index(request):
    return render(request, 'index.html', context={'articles': articles})


def form(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            return render(request, 'form.html', context={
                'form': form,
                'data': request.POST
            })
    else:
        form = Form()
    
    print([i for i in form])
    
    return render(request, 'form.html', {'form': Form})
