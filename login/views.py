from django.shortcuts import render

# Create your views here.

def login_index_view(request, *args, **kwargs):
    return render(request, "login/index.html",{})