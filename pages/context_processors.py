from .models import Page

def pages(request):
    """Add all pages to the template context so the site nav can iterate them.

    This keeps the navigation consistent across all views without having to
    pass `pages` from every view function.
    """
    return {"pages": Page.objects.all().order_by("title")}
