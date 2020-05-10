from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Order, Commodity
from django.template import loader


# Create your views here.
# def index(request):
#     order_list = Order.objects.all()
#     template = loader.get_template('order/index.html')
#     context = {
#         'template_order_list': order_list,
#     }
#     # return HttpResponse(order_list)
#     return HttpResponse(template.render(context, request))
def index(request):
    order_list = Order.objects.all()
    context = {
        'template_order_list': order_list,
    }
    # return HttpResponse(order_list)
    return render(request, 'order/index.html', context)


def kit(request):
    return HttpResponse('This is Kit workshop!')


# def detail(request, customer_id):
#     return HttpResponse('Customer id ' + str(customer_id) + ' name is ' + str(Order.objects.get(pk=customer_id).custom))


def detail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        commodity_list = Commodity.objects.all()
    except Order.DoesNotExist:
        raise Http404("Order does not exist")
    return render(request, 'order/detail.html', {'order': order, 'commodity_list': commodity_list})


class IndexView(generic.ListView):
    template_name = 'order/index.html'
    context_object_name = 'template_order_list'

    def get_queryset(self):
        return Order.objects.order_by('pk')[:5]


class DetailView(generic.DetailView):
    model = Order
    template_name = 'order/detail.html'


def add_item(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    commodity_list = Commodity.objects.all()
    try:
        selected_commodity = Commodity.objects.get(pk=request.POST['new_commodity'])
        order.commodity.add(selected_commodity)
        order.save()
    except (KeyError, Commodity.DoesNotExist):
        return render(request, 'order/detail.html', {
            'order': order,
            'commodity_list': commodity_list,
            'error_message': "You didn't select a commodity to add into the order.",
        })
    else:
        return HttpResponseRedirect(reverse('order:results', args=(order.id,)))


def remove_item(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    commodity_list = Commodity.objects.all()
    try:
        selected_commodity = Commodity.objects.get(pk=request.POST['new_commodity'])
        order.commodity.remove(selected_commodity)
        order.save()
    except (KeyError, Commodity.DoesNotExist):
        return render(request, 'order/detail.html', {
            'order': order,
            'commodity_list': commodity_list,
            'error_message': "You didn't select a commodity to remove into the order.",
        })
    else:
        return HttpResponseRedirect(reverse('order:results', args=(order.id,)))


class ResultsView(generic.DetailView):
    model = Order
    template_name = 'order/results.html'
