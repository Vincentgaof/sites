from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from lists.models import Item

def home_page(request):
    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()

    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()

    return render(request, 'list.html', {'items': items})