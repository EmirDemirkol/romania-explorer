from django.shortcuts import render, get_object_or_404
from .models import Page
from datetime import date


def home(request):
    today = date.today()
    formatted_date = today.strftime("%A %d %B %Y")
    return render(request, "pages/home.html", {"formatted_date": formatted_date})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    pages = Page.objects.all().order_by("title")
    return render(request, "pages/page_detail.html", {"page": page, "pages": pages})







