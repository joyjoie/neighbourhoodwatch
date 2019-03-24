from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Business,User
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Neighbourhood.display_neighbourhood()
    return render(request,'photos/index.html' , {"images":images})