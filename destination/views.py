from django.shortcuts import render

from .models import Destination
# Create your views here.
def destination_detail_view(request, *args, **kwargs):
    queryset = Destination.objects.all()
    context = {
        'object_list': queryset
    }

    return render(request, "destination/details.html", context)