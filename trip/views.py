from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def trips_index_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Hello World </h1>")
    return render(request, "trip/index.html", {})
