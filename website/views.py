from django.shortcuts import render
from .models import Item


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "website/item_list.html", context)

def index(request):
    return render (request, 'website/index.html')
    
def rice(request):
    return render (request, 'website/rice.html')    

def pulses(request):
    return render (request, 'website/pulses.html')   

def oil(request):
    return render (request, 'website/oil.html')   
    
def dry_fruits(request):
    return render (request, 'website/dry_fruits.html')   

def Ghee(request):
    return render (request, 'website/Ghee.html')       
     
def spice(request):
    return render (request, 'website/spice.html')       
     
def sugar(request):
    return render (request, 'website/sugar.html')         