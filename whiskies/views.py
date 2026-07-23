from django.shortcuts import render, redirect, get_object_or_404
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
    {
        "form": form,
        "title": "ウイスキー登録"
    }
)
def whisky_detail(request, pk):

    whisky = get_object_or_404(
        Whisky,
        pk=pk
    )

    return render(
        request,
        "whiskies/whisky_detail.html",
        {"whisky": whisky}
    )


def whisky_update(request, pk):

    whisky = get_object_or_404(
        Whisky,
        pk=pk
    )

    if request.method == "POST":

        form = WhiskyForm(
            request.POST,
            instance=whisky
        )

        if form.is_valid():
            form.save()
            return redirect(
                "whisky_detail",
                pk=whisky.pk
            )

    else:

        form = WhiskyForm(
            instance=whisky
        )

    return render(
        request,
        "whiskies/whisky_form.html",
        {
            "form": form,
            "title": "ウイスキー編集"
        }
    )