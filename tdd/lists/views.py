from django.shortcuts import render, redirect

# Create your views here.
from .models import Item


def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST.get("item_text"))
        return redirect('/')
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'lists/home.html', context)
