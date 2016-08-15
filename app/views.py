from django.shortcuts import render
from .models import MenuItem

def main_page(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'app/index.html', {'menu_items':menu_items})
# Create your views here.
