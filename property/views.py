from django.shortcuts import render

# Create your views here.
from .models import Property
def property_detail_view(request, *args, **kwargd):
    queryset = Property.objects.all()
    context = {
        'object_list': queryset,
        'points': [1,2,3,4,5]
    }
    return render(request, "property/details.html",context)