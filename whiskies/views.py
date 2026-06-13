from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Whisky


def whisky_list(request):
    whiskies = Whisky.objects.all()

    return render(
        request,
        'whiskies/whisky_list.html',
        {'whiskies': whiskies}
    )