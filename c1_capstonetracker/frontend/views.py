from django.shortcuts import render

# Create your views here.


def index(request):
    """Return Homepage for Capstone Tracker."""
    return render(request, 'index.html')

def home_page(request):
	"""Return openning page for Capstone Tracker."""
	return render(request, '../projectTracker/templates/home_page.html')
