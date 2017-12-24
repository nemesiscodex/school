from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Render login page
    """
    return render(request=request, template_name='index.html')


def do_login(request):
    """
    Do authentication
    """
    if request.method == 'GET':
        return "GET"
    elif request.method == 'POST':
        return "POST"
    return ""