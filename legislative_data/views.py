from django.shortcuts import render
from .utils import get_legislator_data, get_bill_data


def index(request):
    return render(request, 'index.html')


def legislator_data(request):
    context = {
        "legislator_data": get_legislator_data()
    }
    return render(request, 'legislator_data.html', context=context)


def bill_data(request):
    context = {
        "bill_data": get_bill_data()
    }
    return render(request, 'bill_data.html', context=context)
