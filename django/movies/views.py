from django.shortcuts import render
from .models import Movies

# Create your views here.

# def movie_request(request):
#     movies= Movies.objects.all()
#     return render(request, "movies/index.html" , context= movies)


#create command
# Movies.objects.create(key="value") #done
# #show all data
# Movies.objects.all()  #done
# #get a specific data
# movies= Movies.objects.get(key="value")
# movies.name=""
# #delete a specific data
# Movies.objects.get(key="value").delete()
# #delete all the data
# Movies.objects.all().delete()
# #Update a specific data
# Movies.objects.filter(key="value").update(key="NewValue")
# #update a key in all rows
# Movies.objects.all().update(key="value")