from django.shortcuts import render

# Create your views here.


def index(request):
    """Return Homepage for Capstone Tracker."""
    return render(request, 'index.html')
