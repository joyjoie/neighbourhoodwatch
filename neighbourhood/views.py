from django.shortcuts import render
from django.http  import HttpResponse
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
    if request.method == 'POST':
           
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', request.user.profile.id)

    else:
        
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile/profile.html', { "profile":profile, "p_form":p_form })



@login_required(login_url='/accounts/login/')
def profile(request,id):
    profile=Profile.objects.get(id=id)
    
    if request.method == 'POST':
       
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile',profile.id)

    else:
        
        p_form = ProfileUpdateForm(instance=request.user.profile)

    fo=Profile.pro()
    profile=Profile.objects.get(id=id)
    current_profile=Profile.objects.get(user=request.user)

    return render(request, 'profile/profile.html', {"fo":fo,"p_form":p_form,"profile":profile, "current_profile":current_profile})


def image(request, id,slug):
    image=get_object_or_404()
    try: 
        foto = Image.objects.get(id = image_id, slug=slug)

    except DoesNotExist:
        raise Http404()

    

    return render(request,"photos/image.html", {"foto":foto,  "image":image})


