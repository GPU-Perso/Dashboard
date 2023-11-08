from django.shortcuts import render, HttpResponse

from currency import api

# Create your views here.
def dashboard(request, days_range = 2, currencies="USD"):
    days, rates = api.get_rates(currencies=currencies.split(","), days=days_range)
    return render(request, "currency/index.html", context={"data": rates["USD"], "days_labels": days})