from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Business,User,Profile
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Neighbourhood.display_neighbourhood()
    return render(request,'photos/index.html' , {"images":images})


@login_required(login_url='/accounts/login/')
def my_profile(request):
    profile = request.user.profile   
    # images = Project.objects.all().filter(id = profile.user.id)
   
    return render(request, 'profile/profile.html', { "profile":profile})
