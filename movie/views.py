from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Movie

API_KEY = 'api_key=30ed42564c56a79f475e2260542cea69'
BASE_URL = 'https://api.themoviedb.org/3'
API_URL = BASE_URL + '/discover/movie?sort_by=popularity.desc&' + API_KEY
IMG_URL = 'https://image.tmdb.org/t/p/w500'
search_URL = BASE_URL + '/search/movie?' + API_KEY

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key='30ed42564c56a79f475e2260542cea69'
serviceurl=API_URL

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen(serviceurl,context=ctx)
data=fhand.read().decode()
# doing again

try:
    js = json.loads(data)
except:
    print('some error occured')

final_data=js.get('results')

for movie in final_data:
    movie=Movie(title=movie['title'],vote_average=movie['vote_average'],overview=movie['overview'],poster_path=movie['poster_path'])
    movie.save()
# to upload

def home(request):
   
    favourite_movies=None
    if request.user.is_authenticated:
    #     movies=Movie.objects.all()
         favourite_movies=Movie.newmanager.filter(favourites=request.user)
        
    context={
        'movies':Movie.objects.all(),
        'fav_movies':favourite_movies
    }
    return render(request,'movie/home.html',context)