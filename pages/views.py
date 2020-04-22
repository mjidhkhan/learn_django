from django.http import HttpResponse
from django.shortcuts import render


from destination.models import Destination
   

# Create your views here.
def home_view(request, *args, **kwargs):
    queryset = Destination.objects.all()
    context = {
        'object_list': queryset
    }
    #return HttpResponse("<h1> Hello World </h1>")
    return render(request, "pages/home.html", context)

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Contact Page </h1>")
    return render(request, "contact.html", {})