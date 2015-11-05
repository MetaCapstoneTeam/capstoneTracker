from django.shortcuts import render


def index(request):
    """Return Homepage for Capstone Tracker."""
    return render(request, 'index.html')
