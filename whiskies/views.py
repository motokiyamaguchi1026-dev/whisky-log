from django.shortcuts import render, redirect
from .models import Whisky
from .forms import WhiskyForm


def whisky_list(request):
    whiskies = Whisky.objects.all()

    return render(
        request,
        "whiskies/whisky_list.html",
        {"whiskies": whiskies}
    )


def whisky_create(request):
    if request.method == "POST":
        form = WhiskyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("whisky_list")

    else:
        form = WhiskyForm()

    return render(
        request,
        "whiskies/whisky_form.html",
        {"form": form}
    )