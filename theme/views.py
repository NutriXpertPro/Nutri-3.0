from django.shortcuts import render

# Create your views here.


def landing_page_view(request):
    """Esta view renderiza a página de entrada."""
    return render(request, "landing_page.html")
