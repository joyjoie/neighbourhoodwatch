from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import ProfileUpdateForm,CommentsForm,NhoodForm
from .models import Neighbourhood,Business,Profile,Comments


@login_required(login_url='/accounts/login/')
def index(request):
    images = Neighbourhood.display_neighbourhood()
    comments=Comments.display_comments()
    
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            image_id=int(request.POST.get('image_id'))
            image=Neighbourhood.objects.get(id=image_id)
            comment=form.save(commit=False)
            comment.img=image
            comment.user=request.user
            comment.save()
            return redirect('index')
    else:
        form=CommentForm()


   

    context ={"images":images, "comments":comments , "form":form, }
        
    return render(request, 'photos/index.html',context )





@login_required(login_url='/accounts/login/')
def my_profile(request):
    profile = request.user.profile   
  
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

    return render(request, "profile/profile.html", {"fo":fo,"p_form":p_form,"profile":profile, "current_profile":current_profile})


def image(request, id,slug):
    image=get_object_or_404()
    try: 
        foto = Image.objects.get(id = image_id, slug=slug)

    except DoesNotExist:
        raise Http404()

    

    return render(request,"photos/image.html", {"foto":foto,  "image":image})


def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'photos/search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'photos/search.html', {'message':message})


def upload(request):
    if request.method =='POST':
        form=NhoodForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile',request.user.profile.id)
    else:
        form=NhoodForm()
    return render(request, 'photos/addimg.html', {"form":form})


@login_required(login_url='/accounts/login/')
def neighbourhood(request,id):
    nhood=Neighbourhood.objects.get(id=id)

    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            neighbourhood_id=int(request.POST.get('neighbourhood_id'))
            neighbourhood=Neighbourhood.objects.get(id=neighbourhood_id)
            comment=form.save(commit=False)
            comment.img=neighbourhood
            comment.user=request.user
            comment.save()
            return redirect('neighbourhood', nhood.id)
    else:
        form=CommentsForm()

    comments= Comments.objects.filter(img=nhood)


   
    return render(request, 'photos/neighbourhood.html', { "nhood":nhood ,"form":form,"comments":comments}) 