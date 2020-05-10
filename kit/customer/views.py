from django.shortcuts import render
from .models import Customer
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('This is Django workshop!')


def kit(request):
    return HttpResponse('This is Kit workshop!')


# def detail(request, customer_id):
#     return HttpResponse('You are querying customer id %s!' % customer_id)
def detail(request, customer_id):
    return HttpResponse('Customer id ' + str(customer_id) + ' name is ' + Customer.objects.get(id=customer_id).name)



def query(request):
    customer_list = Customer.objects.all()
    return HttpResponse(customer_list)
