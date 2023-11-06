from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, "currency/index.html", context={"list": range(10)})