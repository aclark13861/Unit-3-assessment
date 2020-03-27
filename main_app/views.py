from django.shortcuts import render
from django.views.generic.edit import DeleteView, CreateView
from .models import Item

# Create your views here.
from django.http import HttpResponse

def items_index(request):
    items = Item.objects.all()
    return render(request, 'items/index.html', { 'items': items })


class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'