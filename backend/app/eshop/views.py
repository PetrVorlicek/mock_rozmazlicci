from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView
from eshop.models import Item

# Create your views here.


def index(request):
    return render(
        request,
        "index.html",
    )


class ItemView(DetailView):
    model = Item

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
