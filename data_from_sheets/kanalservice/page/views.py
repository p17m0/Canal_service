from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Orders
# Create your views here.


def pagina(request, posts):
    paginator = Paginator(posts, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def view_order(request):
    orders = Orders.objects.all()

    context = {
       'page_obj': pagina(request, orders)
    }
    return render(request, 'orders/index.html', context)
