from django.shortcuts import render
from .models import MenuItem
from django.template import RequestContext

def main_page(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'app/index.html', {'menu_items':menu_items},context_instance=RequestContext(request))

def contact_detail(request):
    return render(request, 'app/iletisim.html', {},context_instance=RequestContext(request))

def about_us(request):
    
    return render(request, 'app/hakkimizda.html', {},context_instance=RequestContext(request))
