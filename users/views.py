from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect

# Create your views here.
#messages display
from django.contrib import messages
#our own created form and user update form
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
#to make profile page login restricted
from django.contrib.auth.decorators import login_required
# for favourites
from movie.models import Movie

# Create your views here.
#get request means display blank form , post request menas save data
def register(request):
    if request.method=='POST':
        # form=UserCreationForm(request.POST)
        form=UserRegisterForm(request.POST)

        if form.is_valid():
            # saving user
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! You are now able to Login')
            return redirect('login')
    else:
        # form=UserCreationForm()
        form=UserRegisterForm()

    return render(request,'users/register.html',{'form':form})

# login required to access this
@login_required
def profile(request):
    # profile update(model form means they expect filled data of current instance)
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Account has been updated')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
        }

    return render(request,'users/profile.html',context)

# favourites
@login_required
def favourite_add(request,id):
    movie=get_object_or_404(Movie,id=id)
    if movie.favourites.filter(id=request.user.id).exists():
        movie.favourites.remove(request.user)
    else:
        movie.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def favourite_list(request):
    # user=request.user
    # favourite_movies=Movie.favourites.filter(user)
   
    # return render(request,'users/favourites.html',context)
    favourite_movies=Movie.newmanager.filter(favourites=request.user)
    context={
        'favourite_movies':favourite_movies
    }
    return render(request,'users/favourites.html',context)
    # favourite_movies=Movie.favourites(favourites=request.user)
